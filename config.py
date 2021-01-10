import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDER_LIST = [
    {
        'name': 'index.jinja2',
        'context': {},
        'type': 'html'
    }
]
GLOBAL_CONTEXT = {
    'social_links': [
        ('https://linkedin.com/in/areebbeigh/', 'linkedin.svg', 'LinkedIn'),
        ('https://instagram.com/areebbeigh/', 'instagram.svg', 'Instagram'),
        ('https://t.me/xnihpue/', 'telegram.svg', 'Telegram'),
        ('mailto:areebbeigh@gmail.com', 'gmail.svg', 'GMail'),
    ]
}
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')
