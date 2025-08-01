#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
板式家具工艺流程管理系统 - 演示版本
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """主页"""
    html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>板式家具工艺流程管理系统</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
            }
            .header h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            .header p {
                font-size: 1.2rem;
                opacity: 0.9;
            }
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin-bottom: 40px;
            }
            .feature-card {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 12px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                transition: transform 0.3s ease;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-card h3 {
                font-size: 1.5rem;
                margin-bottom: 15px;
                color: #ffeb3b;
            }
            .nav-links {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }
            .nav-link {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                padding: 15px 30px;
                border-radius: 8px;
                font-weight: 500;
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            .nav-link:hover {
                background: rgba(255, 255, 255, 0.3);
                border-color: #ffeb3b;
                transform: scale(1.05);
            }
            .status {
                background: rgba(76, 175, 80, 0.2);
                padding: 20px;
                border-radius: 8px;
                margin-top: 30px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🏠 板式家具工艺流程管理系统</h1>
                <p>专业的可视化工艺流程编排与成本计算平台</p>
            </div>
            
            <div class="features">
                <div class="feature-card">
                    <h3>🎨 工艺流程设计器</h3>
                    <p>拖拽式可视化工艺流程编排，支持切割、封边、打孔、组装等多种工艺节点，实时配置参数和成本信息。</p>
                </div>
                
                <div class="feature-card">
                    <h3>📊 成本分析报表</h3>
                    <p>多维度成本分析，包含材料成本、人工成本、设备成本等，提供趋势图表和详细数据报告。</p>
                </div>
                
                <div class="feature-card">
                    <h3>🗄️ 材料库管理</h3>
                    <p>完整的板材、五金、辅料库管理，自动损耗率计算，支持供应商信息和价格管理。</p>
                </div>
            </div>
            
            <div class="nav-links">
                <a href="/workflow-designer" class="nav-link">🎨 工艺流程设计器</a>
                <a href="/cost-analysis" class="nav-link">📊 成本分析报表</a>
                <a href="/api/demo" class="nav-link">🔌 API接口演示</a>
            </div>
            
            <div class="status">
                <h3>✅ 系统状态</h3>
                <p>系统正在运行中，所有功能模块已加载完成！</p>
                <p><strong>访问地址：</strong> http://localhost:5000</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/workflow-designer')
def workflow_designer():
    """工艺流程设计器"""
    html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>工艺流程设计器</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: #f5f5f5;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                text-align: center;
            }
            .container {
                max-width: 1200px;
                margin: 20px auto;
                padding: 20px;
            }
            .demo-info {
                background: #e3f2fd;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 20px;
                border-left: 4px solid #2196f3;
            }
            .feature-list {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
            }
            .feature-list h3 {
                color: #667eea;
                border-bottom: 2px solid #667eea;
                padding-bottom: 10px;
            }
            .feature-item {
                margin: 15px 0;
                padding: 10px;
                background: #f8f9fa;
                border-radius: 6px;
            }
            .back-link {
                display: inline-block;
                background: #667eea;
                color: white;
                text-decoration: none;
                padding: 12px 24px;
                border-radius: 6px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🎨 工艺流程设计器</h1>
            <p>拖拽式可视化工艺流程编排工具</p>
        </div>
        
        <div class="container">
            <div class="demo-info">
                <h3>📋 功能演示</h3>
                <p>这是工艺流程设计器的演示页面。在完整版本中，您可以：</p>
            </div>
            
            <div class="feature-list">
                <h3>🔧 核心功能</h3>
                
                <div class="feature-item">
                    <strong>🎯 拖拽式节点编排</strong><br>
                    从节点面板拖拽工艺节点（开始、切割、封边、打孔、组装、质检、包装、结束）到画布
                </div>
                
                <div class="feature-item">
                    <strong>⚙️ 实时参数配置</strong><br>
                    选择节点可在右侧面板编辑工艺参数、预估时间、人工成本、设备成本
                </div>
                
                <div class="feature-item">
                    <strong>🔗 智能流程连接</strong><br>
                    自动识别节点连接点，生成工艺流程路径
                </div>
                
                <div class="feature-item">
                    <strong>💰 成本实时预览</strong><br>
                    设计过程中实时显示成本估算和分解
                </div>
                
                <div class="feature-item">
                    <strong>💾 模板保存管理</strong><br>
                    一键保存工艺流程模板，支持版本管理和复用
                </div>
            </div>
            
            <a href="/" class="back-link">← 返回主页</a>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/cost-analysis')
def cost_analysis():
    """成本分析报表"""
    html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>成本分析报表</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: #f5f5f5;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                text-align: center;
            }
            .container {
                max-width: 1200px;
                margin: 20px auto;
                padding: 20px;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .stats-card {
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
                text-align: center;
            }
            .stats-value {
                font-size: 2rem;
                font-weight: bold;
                margin: 10px 0;
            }
            .chart-placeholder {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
                margin-bottom: 20px;
                text-align: center;
                border: 2px dashed #ddd;
            }
            .back-link {
                display: inline-block;
                background: #667eea;
                color: white;
                text-decoration: none;
                padding: 12px 24px;
                border-radius: 6px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 成本分析报表</h1>
            <p>多维度成本分析与趋势监控</p>
        </div>
        
        <div class="container">
            <div class="stats-grid">
                <div class="stats-card">
                    <h3>💰 总成本</h3>
                    <div class="stats-value" style="color: #667eea;">¥12,580</div>
                    <p>本月累计</p>
                </div>
                
                <div class="stats-card">
                    <h3>📦 材料成本</h3>
                    <div class="stats-value" style="color: #f093fb;">¥5,660</div>
                    <p>占比 45%</p>
                </div>
                
                <div class="stats-card">
                    <h3>👥 人工成本</h3>
                    <div class="stats-value" style="color: #4facfe;">¥3,770</div>
                    <p>占比 30%</p>
                </div>
                
                <div class="stats-card">
                    <h3>⚙️ 设备成本</h3>
                    <div class="stats-value" style="color: #43e97b;">¥3,150</div>
                    <p>占比 25%</p>
                </div>
            </div>
            
            <div class="chart-placeholder">
                <h3>📈 成本趋势图表</h3>
                <p>在完整版本中，这里将显示：</p>
                <ul style="text-align: left; display: inline-block;">
                    <li>📉 成本趋势分析图表</li>
                    <li>🥧 成本结构饼图</li>
                    <li>📊 工艺节点成本对比</li>
                    <li>📋 详细数据表格</li>
                    <li>📤 Excel/PDF导出功能</li>
                </ul>
            </div>
            
            <a href="/" class="back-link">← 返回主页</a>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/api/demo')
def api_demo():
    """API接口演示"""
    demo_data = {
        "system_info": {
            "name": "板式家具工艺流程管理系统",
            "version": "1.0.0",
            "status": "running",
            "features": [
                "工艺流程可视化编排",
                "成本计算引擎", 
                "材料库管理",
                "数据分析报表"
            ]
        },
        "workflow_templates": [
            {
                "id": 1,
                "name": "标准衣柜加工流程",
                "description": "适用于标准规格衣柜的完整加工流程",
                "nodes": ["开始", "切割", "封边", "打孔", "组装", "质检", "包装", "结束"],
                "estimated_cost": 580.50,
                "estimated_time": 180
            }
        ],
        "materials": [
            {
                "id": 1,
                "code": "E0-18MM-WH",
                "name": "E0级白色三聚氰胺板",
                "category": "板材",
                "unit_price": 280.0,
                "unit": "张"
            },
            {
                "id": 2,
                "code": "HINGE-35",
                "name": "35杯铰链",
                "category": "五金", 
                "unit_price": 12.5,
                "unit": "个"
            }
        ],
        "cost_analysis": {
            "total_cost": 12580.0,
            "material_cost": 5660.0,
            "labor_cost": 3770.0,
            "machine_cost": 3150.0,
            "cost_breakdown": {
                "material_percentage": 45,
                "labor_percentage": 30,
                "machine_percentage": 25
            }
        }
    }
    
    return jsonify(demo_data)

@app.route('/health')
def health_check():
    """健康检查"""
    return jsonify({
        "status": "healthy",
        "message": "板式家具工艺流程管理系统运行正常",
        "timestamp": "2024-01-01T00:00:00Z"
    })

if __name__ == '__main__':
    print("🏠 板式家具工艺流程管理系统 - 演示版本")
    print("=" * 60)
    print("🚀 服务器启动成功！")
    print()
    print("📱 访问地址:")
    print("   🏠 主页: http://localhost:5000")
    print("   🎨 工艺流程设计器: http://localhost:5000/workflow-designer")
    print("   📊 成本分析报表: http://localhost:5000/cost-analysis")
    print("   🔌 API接口演示: http://localhost:5000/api/demo")
    print("=" * 60)
    print("💡 这是演示版本，展示系统的核心功能和界面设计")
    print("📚 完整版本包含拖拽式流程编排、实时成本计算等高级功能")
    print()
    print("按 Ctrl+C 停止服务器")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)