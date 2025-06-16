#!/usr/bin/env python3
"""
数据初始化脚本
用于创建示例数据
"""

from app import app, db, Product
import random


def create_sample_data():
    """创建示例数据"""

    # 示例产品数据
    sample_products = [
        # Zina系列
        {'series': 'Zina', 'spu': 'HSR170', 'sku': 'HSR170W01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Zina', 'spu': 'HSR170', 'sku': 'HSR170B01', 'file_control': '已受控', 'standardization': '未落地'},
        {'series': 'Zina', 'spu': 'HSR170', 'sku': 'HSR170G01', 'file_control': '未受控', 'standardization': '已落地'},
        {'series': 'Zina', 'spu': 'HSR180', 'sku': 'HSR180W01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Zina', 'spu': 'HSR180', 'sku': 'HSR180B01', 'file_control': '未受控', 'standardization': '未落地'},
        {'series': 'Zina', 'spu': 'HSR190', 'sku': 'HSR190W01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Zina', 'spu': 'HSR190', 'sku': 'HSR190G01', 'file_control': '已受控', 'standardization': '未落地'},
        {'series': 'Zina', 'spu': 'HSR200', 'sku': 'HSR200W01', 'file_control': '未受控', 'standardization': '已落地'},

        # Wivor系列
        {'series': 'Wivor', 'spu': 'WVR100', 'sku': 'WVR100W01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Wivor', 'spu': 'WVR100', 'sku': 'WVR100B01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Wivor', 'spu': 'WVR110', 'sku': 'WVR110W01', 'file_control': '未受控', 'standardization': '未落地'},
        {'series': 'Wivor', 'spu': 'WVR110', 'sku': 'WVR110G01', 'file_control': '已受控', 'standardization': '未落地'},
        {'series': 'Wivor', 'spu': 'WVR120', 'sku': 'WVR120W01', 'file_control': '已受控', 'standardization': '已落地'},
        {'series': 'Wivor', 'spu': 'WVR120', 'sku': 'WVR120B01', 'file_control': '未受控', 'standardization': '已落地'},
        {'series': 'Wivor', 'spu': 'WVR130', 'sku': 'WVR130W01', 'file_control': '已受控', 'standardization': '未落地'},
    ]

    print("正在创建示例数据...")

    # 清空现有数据
    Product.query.delete()

    # 添加示例产品
    for product_data in sample_products:
        product = Product(**product_data)
        db.session.add(product)

    # 生成更多随机数据
    series_list = ['Zina', 'Wivor']
    status_list = ['已受控', '未受控']
    standardization_list = ['已落地', '未落地']

    for i in range(50):  # 生成50个额外的产品
        series = random.choice(series_list)
        spu_num = random.randint(100, 999)
        color_code = random.choice(['W', 'B', 'G', 'R', 'Y'])
        variant = random.randint(1, 9)

        spu = f"{series[:3].upper()}{spu_num}"
        sku = f"{spu}{color_code}{variant:02d}"

        product = Product(
            series=series,
            spu=spu,
            sku=sku,
            file_control=random.choice(status_list),
            standardization=random.choice(standardization_list)
        )
        db.session.add(product)

    db.session.commit()

    total_products = Product.query.count()
    print(f"成功创建 {total_products} 个产品记录")

    # 显示统计信息
    print("\n数据统计:")
    print(f"总产品数: {total_products}")

    for series in series_list:
        count = Product.query.filter_by(series=series).count()
        print(f"{series}系列: {count} 个产品")

    controlled_count = Product.query.filter_by(file_control='已受控').count()
    print(f"已受控文件: {controlled_count} 个")

    standardized_count = Product.query.filter_by(standardization='已落地').count()
    print(f"已标准化: {standardized_count} 个")

    complete_count = Product.query.filter_by(
        file_control='已受控',
        standardization='已落地'
    ).count()
    print(f"完全完成: {complete_count} 个")


def main():
    """主函数"""
    print("=" * 50)
    print("产品状态管理系统 - 数据初始化")
    print("=" * 50)

    with app.app_context():
        # 创建数据库表
        db.create_all()
        print("数据库表创建完成")

        # 询问是否要创建示例数据
        response = input("是否要创建示例数据？(y/N): ").lower()
        if response in ['y', 'yes']:
            create_sample_data()
            print("\n示例数据创建完成！")
            print("您现在可以启动应用程序查看数据。")
        else:
            print("跳过示例数据创建")

    print("=" * 50)


if __name__ == '__main__':
    main()
