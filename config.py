
"""
配置文件：爬虫运行参数设置
本配置适用于所有 JD 爬虫脚本，可导入后统一调用
"""

# 是否启用慢速模式（更友好地模拟人类行为，适合开源环境）
SLOW_MODE = True

# 爬取商品时的最大数量限制（可防止意外/误操作爬过多）
MAX_PRODUCTS = 200

# 评论爬虫中连续多少个商品无有效评论后终止（防止反爬封锁）
MAX_EMPTY_COMMENTS_TRIGGER = 20

# 每爬多少页或商品就进行一次随机暂停（模拟“用户离开”）
PAGE_PAUSE_FREQUENCY = 5         # 商品页爬虫
PRODUCT_PAUSE_FREQUENCY = 10     # 评论爬虫

# 每次请求间的延迟范围（单位：秒）
NORMAL_DELAY_RANGE = (1.5, 3)    # 默认非慢速模式
SLOW_DELAY_RANGE = (5, 8)        # 慢速模式

# 间歇性“用户暂停”的延迟范围
PAUSE_DELAY_RANGE = (10, 20)

# 设置 user-agent（可选，用于更真实的浏览器模拟）
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/118.0.5993.90 Safari/537.36"
)

# 输出日志级别（未来可拓展 debug/info/warning）
LOG_LEVEL = "INFO"
