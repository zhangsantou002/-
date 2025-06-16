#!/usr/bin/env python3
"""
产品状态管理系统启动脚本
"""

import os
import sys
from app import app, db


def create_app():
    """创建并配置应用"""
    # 确保数据库目录存在
    db_dir = os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # 创建数据库表
    with app.app_context():
        db.create_all()
        print("数据库初始化完成")

    return app


def main():
    """主函数"""
    print("=" * 50)
    print("产品状态管理系统")
    print("=" * 50)
    print("正在启动服务器...")

    app = create_app()

    # 获取启动参数
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'

    print(f"服务器地址: http://{host}:{port}")
    print("按 Ctrl+C 停止服务器")
    print("=" * 50)

    try:
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n服务器已停止")
        sys.exit(0)


if __name__ == '__main__':
    main()
