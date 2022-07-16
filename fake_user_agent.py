from fake_useragent import UserAgent


user = UserAgent(verify_ssl=False).random # Создаём переменную user и суём туда рандомный user-agent.
header = {'user-agent': user} # В заголовок суём наш user-agent

print(header)

# ua.firefox
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0'
# ua.chrome
# 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36'
# ua.opera
# 'Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00'
# ua.random
# 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36'
# ua.random
# 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'