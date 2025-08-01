#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
板式家具工艺流程管理系统 - 简化启动版本
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objs as go
import plotly.utils
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product_status.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 原有产品数据模型
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String(50), nullable=False)
    spu = db.Column(db.String(50), nullable=False)
    sku = db.Column(db.String(50), nullable=False)
    file_control = db.Column(db.String(20), nullable=False)
    standardization = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'series': self.series,
            'spu': self.spu,
            'sku': self.sku,
            'file_control': self.file_control,
            'standardization': self.standardization
        }

# 创建数据库表
with app.app_context():
    db.create_all()
    
    # 初始化示例数据
    if Product.query.count() == 0:
        sample_data = [
            ('Zina', 'HSR170', 'HSR170W01', '未受控', '已落地'),
            ('Zina', 'HSR170', 'HSR170B01', '已受控', '未落地'),
            ('Zina', 'HSR180', 'HSR180W01', '已受控', '已落地'),
            ('York', 'YRK200', 'YRK200W01', '未受控', '未落地'),
            ('York', 'YRK200', 'YRK200B01', '已受控', '已落地'),
        ]
        
        for data in sample_data:
            product = Product(
                series=data[0],
                spu=data[1],
                sku=data[2],
                file_control=data[3],
                standardization=data[4]
            )
            db.session.add(product)
        
        db.session.commit()

# 路由定义
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/workflow-designer')
def workflow_designer():
    """工艺流程设计器页面"""
    return render_template('workflow_designer.html')

@app.route('/cost-analysis')  
def cost_analysis():
    """成本分析报表页面"""
    return render_template('cost_analysis.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        data = request.get_json()
        product = Product(
            series=data['series'],
            spu=data['spu'],
            sku=data['sku'],
            file_control=data['file_control'],
            standardization=data['standardization']
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({'success': True, 'message': '产品添加成功'})
    
    return render_template('add_product.html')

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        data = request.get_json()
        product.series = data['series']
        product.spu = data['spu']  
        product.sku = data['sku']
        product.file_control = data['file_control']
        product.standardization = data['standardization']
        db.session.commit()
        return jsonify({'success': True, 'message': '产品更新成功'})
    
    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'success': True, 'message': '产品删除成功'})

@app.route('/api/products')
def api_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/api/dashboard_data')
def dashboard_data():
    products = Product.query.all()
    
    # 计算统计数据
    total_products = len(products)
    file_controlled = len([p for p in products if p.file_control == '已受控'])
    standardized = len([p for p in products if p.standardization == '已落地'])
    
    # 按系列分组
    series_data = {}
    for product in products:
        if product.series not in series_data:
            series_data[product.series] = 0
        series_data[product.series] += 1
    
    # 状态分布
    status_data = {
        'file_control': {
            '已受控': file_controlled,
            '未受控': total_products - file_controlled
        },
        'standardization': {
            '已落地': standardized, 
            '未落地': total_products - standardized
        }
    }
    
    return jsonify({
        'total_products': total_products,
        'file_controlled': file_controlled,
        'standardized': standardized,
        'series_data': series_data,
        'status_data': status_data
    })

# 模拟工艺流程API接口
@app.route('/api/workflow/templates')
def get_workflow_templates():
    """获取工艺流程模板（模拟数据）"""
    mock_templates = [
        {
            'id': 1,
            'name': '标准衣柜加工流程',
            'description': '适用于标准规格衣柜的完整加工流程',
            'product_series': 'HSR170',
            'version': '1.0',
            'status': 'active',
            'created_at': '2024-01-01T00:00:00',
            'nodes_count': 8
        }
    ]
    return jsonify({'templates': mock_templates})

@app.route('/api/workflow/materials')
def get_materials():
    """获取材料列表（模拟数据）"""
    mock_materials = [
        {
            'id': 1,
            'code': 'E0-18MM-WH',
            'name': 'E0级白色三聚氰胺板',
            'category': '板材',
            'unit_price': 280.0,
            'unit': '张'
        },
        {
            'id': 2,
            'code': 'HINGE-35',
            'name': '35杯铰链', 
            'category': '五金',
            'unit_price': 12.5,
            'unit': '个'
        }
    ]
    return jsonify({'materials': mock_materials})

if __name__ == '__main__':
    print("🏠 板式家具工艺流程管理系统启动中...")
    print("=" * 50)
    print("📱 访问地址:")
    print("   主页: http://localhost:5000")
    print("   工艺流程设计器: http://localhost:5000/workflow-designer")
    print("   成本分析报表: http://localhost:5000/cost-analysis")
    print("=" * 50)
    print("按 Ctrl+C 停止服务器")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)