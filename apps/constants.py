METHOD_CHOICES = (
    ("aes-256-cfb", "aes-256-cfb"),
    ("aes-128-ctr", "aes-128-ctr"),
    ("rc4-md5", "rc4-md5"),
    ("salsa20", "salsa20"),
    ("chacha20", "chacha20"),
    ("none", "none"),
    ("chacha20-ietf-poly1305", "chacha20-ietf-poly1305"),
    ("aes-128-gcm", "aes-128-gcm"),
    ("aes-256-gcm", "aes-256-gcm"),
)


AEAD_METHODS = {"chacha20-ietf-poly1305", "aes-128-gcm", "aes-256-gcm"}

COUNTRIES_CHOICES = (
    ("US", "United States of America"),
    ("CN", "China"),
    ("GB", "United Kingdom"),
    ("SG", "Singapore"),
    ("TW", "Taiwan"),
    ("HK", "Hong Kong"),
    ("JP", "Japan"),
    ("FR", "France"),
    ("DE", "Germany"),
    ("KR", "Korea"),
    ("JE", "泽西岛"),
    ("NZ", "New Zealand"),
    ("MX", "Mexico"),
    ("CA", "Canada"),
    ("BR", "Brazil"),
    ("CU", "Cuba"),
    ("CZ", "Czech Republic"),
    ("EG", "Egypt"),
    ("FI", "Finland"),
    ("GR", "Greece"),
    ("GU", "Guam"),
    ("IS", "Iceland"),
    ("MO", "Macao"),
    ("NL", "Netherlands"),
    ("NO", "Norway"),
    ("PL", "Poland"),
    ("IT", "Italy"),
    ("IE", "Ireland"),
    ("AR", "Argentina"),
    ("PT", "Portugal"),
    ("AU", "Australia"),
    ("RU", "Russian Federation"),
    ("CF", "Central African Republic"),
)

THEME_CHOICES = (
    ("default", "default"),
    ("darkly", "darkly"),
    ("flatly", "flatly"),
    ("journal", "journal"),
    ("materia", "materia"),
    ("minty", "minty"),
    ("spacelab", "spacelab"),
    ("superhero", "superhero"),
)


# 判断节点在线时间间隔
NODE_TIME_OUT = 75
