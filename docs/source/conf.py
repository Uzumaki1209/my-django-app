# Configuration file for the Sphinx documentation builder.
import os
import sys
import django

# Add the path to your Django project
sys.path.insert(0, os.path.abspath(r'C:\Users\Kevin Pather\Desktop\Hyperion SE\Hyperion Course\Level 3\Task 10'))

# Set the Django settings module environment variable correctly
os.environ['DJANGO_SETTINGS_MODULE'] = 'political_candidate.settings'

# Initialize Django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Political Candidate App'
copyright = '2024, Kevin Pather'
author = 'Kevin Pather'
release = '28/08/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

