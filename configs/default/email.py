# 是否开启邮件功能
USE_SMTP = True

ANYMAIL = {"MAILGUN_API_KEY": "", "MAILGUN_SENDER_DOMAIN": ""}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "xyz.reset.noreply@gmail.com"
