import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDER_LIST = [
    {
        'name': 'index.jinja2',
        'context': {},
        'type': 'html'
    }
]
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')
