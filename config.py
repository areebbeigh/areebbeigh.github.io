import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDER_LIST = [
    {
        'name': 'index.jinja2',
        'context': {},
        'type': 'html'
    },
    {
        'name': 'projects.jinja2',
        'context': {},
        'type': 'html'
    },
]
GLOBAL_CONTEXT = {
    'social_links': [
        ('https://github.com/areebbeigh/', 'github.svg', 'GitHub'),
        ('https://linkedin.com/in/areebbeigh/', 'linkedin.svg', 'LinkedIn'),
        # ('https://instagram.com/areebbeigh/', 'instagram.svg', 'Instagram'),
        ('https://t.me/xnihpue/', 'telegram.svg', 'Telegram'),
        ('mailto:areebbeigh@gmail.com', 'gmail.svg', 'GMail'),
    ],
    'resume_link': 'https://drive.google.com/file/d/1ODA60rN0ogEABuEz7llyiqsI5_ashRFS/view',
}
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')
