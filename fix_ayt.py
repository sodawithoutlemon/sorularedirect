import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

nav_re = re.compile(r'(<a href=\"/tyt/\"[^>]*>TYT</a>)(?!\s*<a href="\/ayt\/")')

for file in html_files:
    if file.startswith('android/') or file.startswith('ios/'):
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_content = content
        
    # Inject AYT into Desktop nav
    if '<a href="/ayt/"' not in content:
        content = content.replace('<a href="/tyt/" class="text-sm text-gray-500 hover:text-gray-900 transition-colors font-medium">TYT</a>', '<a href="/tyt/" class="text-sm text-gray-500 hover:text-gray-900 transition-colors font-medium">TYT</a>\n                        <a href="/ayt/" class="text-sm text-gray-500 hover:text-gray-900 transition-colors font-medium">AYT</a>')

    if '<a href="/tyt/" class="text-sm text-gray-900 font-bold">TYT</a>' in content and 'ayt/"' not in content:
         content = content.replace('<a href="/tyt/" class="text-sm text-gray-900 font-bold">TYT</a>', '<a href="/tyt/" class="text-sm text-gray-900 font-bold">TYT</a>\n                        <a href="/ayt/" class="text-sm text-gray-500 hover:text-gray-900 transition-colors font-medium">AYT</a>')

    # Inject AYT into footer
    if '<li><a href="/tyt/"' in content and '<li><a href="/ayt/"' not in content:
        content = content.replace('<li><a href="/tyt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">TYT\n                Hazırlık</a></li>', '<li><a href="/tyt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">TYT Hazırlık</a></li>\n            <li><a href="/ayt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">AYT Hazırlık</a></li>')
        content = content.replace('<li><a href="/tyt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">TYT Hazırlık</a></li>', '<li><a href="/tyt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">TYT Hazırlık</a></li>\n            <li><a href="/ayt/" class="text-sm text-gray-400 hover:text-gray-600 transition-colors font-medium">AYT Hazırlık</a></li>')

    # General Footer Link
    if '<a href="/tyt/" class="hover:text-gray-600 transition-colors">TYT</a>' in content and 'ayt/"' not in content:
        content = content.replace('<a href="/tyt/" class="hover:text-gray-600 transition-colors">TYT</a>', '<a href="/tyt/" class="hover:text-gray-600 transition-colors">TYT</a>\n                    <a href="/ayt/" class="hover:text-gray-600 transition-colors">AYT</a>')
    
    if old_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

