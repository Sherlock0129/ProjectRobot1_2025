"""
POS系统启动脚本
允许用户选择启动CLI或GUI版本
"""

import sys


def show_menu():
    """显示启动菜单"""
    print("=" * 50)
    print("          超市收银系统 (POS System)")
    print("=" * 50)
    print("请选择启动方式：")
    print("1. 图形界面 (GUI) - 推荐")
    print("2. 命令行界面 (CLI)")
    print("0. 退出")
    print("=" * 50)


def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请输入选项 (0-2): ").strip()
        
        if choice == "1":
            print("\n正在启动图形界面...")
            try:
                from main_gui import main
                main()
                break
            except ImportError as e:
                print(f"错误: 无法导入GUI模块 - {e}")
                print("请确保已安装Tkinter")
                input("\n按回车键继续...")
            except Exception as e:
                print(f"错误: {e}")
                input("\n按回车键继续...")
        
        elif choice == "2":
            print("\n正在启动命令行界面...")
            try:
                from main import main
                main()
                break
            except Exception as e:
                print(f"错误: {e}")
                input("\n按回车键继续...")
        
        elif choice == "0":
            print("\n再见！")
            sys.exit(0)
        
        else:
            print("\n无效的选择，请重试")
            input("按回车键继续...")


if __name__ == "__main__":
    main()

