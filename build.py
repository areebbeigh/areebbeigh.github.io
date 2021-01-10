import os
import shutil

from jinja2 import (Environment, FileSystemLoader,
                    select_autoescape, StrictUndefined)

from config import (RENDER_LIST, OUTPUT_DIR, STATICFILES_DIR, GLOBAL_CONTEXT)


def url_for(base, filename):
    # print(base, filename)
    return os.path.join(base, filename)


def static(filename):
    return url_for('static', filename)


def image_url(filename):
    return url_for('static/img', filename)


env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml']),
    undefined=StrictUndefined,
)
env.globals.update({
    'url_for': url_for,
    'static': static,
    'image_url': image_url,
    **GLOBAL_CONTEXT,
})

shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
os.mkdir(OUTPUT_DIR)

for job in RENDER_LIST:
    template = env.get_template(job['name'])

    if job['type'] == 'html':
        filename = f"{os.path.splitext(job['name'])[0]}.html"
    elif job['type'] == 'css':
        filename = f"css/{os.path.splitext(job['name'])[0]}.css"
    else:
        raise NotImplementedError()

    output_file = os.path.join(
        OUTPUT_DIR,
        filename)

    html = template.render(job['context'])
    with open(output_file, 'w') as f:
        print(f"{job['name']}")
        f.write(html)

shutil.copytree(STATICFILES_DIR, os.path.join(OUTPUT_DIR, 'static'))
