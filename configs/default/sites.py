# 网站域名设置（请正确填写，不然订阅功能会失效：
HOST = "http://yxorp.xyz/"

# 网站密钥
SECRET_KEY = "aasdasdas"

# 是否开启注册
ALLOW_REGISTER = True

# 默认的theme
# 可选列表在 apps/constants.py 里的THEME_CHOICES里
DEFAULT_THEME = "default"

# 域名设置
ALLOWED_HOSTS = ["*"]

# SS面板设置：
MB = 1024 * 1024
GB = 1024 * 1024 * 1024
DEFAULT_TRAFFIC = 5 * GB
START_PORT = 1024

# 默认加密混淆协议
DEFAULT_METHOD = "aes-256-cfb"

# 签到流量设置
MIN_CHECKIN_TRAFFIC = 50 * MB
MAX_CHECKIN_TRAFFIC = 500 * MB

# 网站title
TITLE = "XYZ"
SUBTITLE = "Faster, cheaper, friendly"

# 用户邀请返利比例
INVITE_PERCENT = 0.2
# 用户能生成的邀请码数量
INVITE_NUM = 5

# 网站邀请界面提示语
INVITEINFO = "Click on the invitation code to go to the registration page or copy "


# 部分API接口TOKEN
TOKEN = "youowntoken"

# 是否开启用户到期邮件通知
EXPIRE_EMAIL_NOTICE = True

# SHORT_URL_ALPHABET 请随机生成,且不要重复
DEFAULT_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"

# FOR SIMPLE UI
SIMPLEUI_HOME_INFO = False
SIMPLEUI_DEFAULT_ICON = False
