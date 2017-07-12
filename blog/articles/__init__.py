"""
Gestion of generic articles written in markdown.
"""

import os
import yaml


desc_file = os.path.dirname(__file__) + '/index.yaml'

with open(desc_file, 'r') as f:
    descs = yaml.load(f)
