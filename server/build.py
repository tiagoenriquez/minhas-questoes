import os
import shutil


shutil.rmtree('templates')
os.mkdir('templates')
shutil.rmtree('static')
os.mkdir('static')
template_name = 'templates/index.html'
shutil.move('dist/index.html', template_name)
statics = os.listdir('dist/assets')
for static in statics:
    shutil.move(f'dist/assets/{static}', 'static')
    content = ''
    with open(template_name, 'r') as template:
        content = template.read()
    content = content.replace(f'/assets/{static}', "{{ url_for('static', filename='" + static + "') }}")
    with open(template_name, 'w') as template:
        template.write(content)
print('Template and statics updated.')