# 是否开启邮件功能
USE_SMTP = True

ANYMAIL = {"MAILGUN_API_KEY": "f09d9734eec1e0d8fbe75fd2a57060b1-e5e67e3e-531e91a4", "MAILGUN_SENDER_DOMAIN": "sandbox49adc3f9a1a249e59526a6f0bec6ec70.mailgun.org"}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@yxorp.xyz"
