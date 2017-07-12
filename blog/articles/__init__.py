"""
Gestion of generic articles written in markdown.
"""

import os
import yaml
import markdown2

import django.utils.autoreload


# Loads informations about articles from index.yaml
root_dir = os.path.dirname(__file__)
desc_file = root_dir + '/index.yaml'

django.utils.autoreload._cached_filenames.append(desc_file)
with open(desc_file, 'r') as f:
    descs = yaml.load(f)

# Read articles content
for art_key in descs :
    try:
        filename = root_dir + '/' + descs[art_key]['content']
        django.utils.autoreload._cached_filenames.append(filename)
        with open(filename, 'r') as f :
            descs[art_key]['content'] = f.read()
            descs[art_key]['html'] = markdown2.markdown(
                descs[art_key]['content'],
                extras=["fenced-code-blocks", "code-color"]
            )
    except Exception as exc:
        print('An error occured while reading %s\'s content : %s' % (art_key, str(exc)))
