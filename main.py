import sys
from Pipeline import JD_review_scraper_Selenium, JD_product_scraper_DrissionPage, Merge_data

def show_menu():
    print("""
🧠 可用操作指令：
  r  - 根据url爬取评论数据
  p  - 爬取商品url
  m  - 数据合并
  q  - 退出程序
""")

def main():
    actions = {
        'r': lambda: JD_review_scraper_Selenium.run(),
        'p': lambda: JD_product_scraper_DrissionPage.run(),
        'm': lambda: Merge_data.run(),
        'q': lambda: sys.exit(0)
    }

    while True:
        show_menu()
        cmd = input("请输入操作指令：").strip().lower()
        action = actions.get(cmd)

        if action:
            print(f"✅ 正在执行：{cmd}")
            action()
        else:
            print("❌ 无效指令，请重新输入。")

if __name__ == "__main__":
    main()
