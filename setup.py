from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'InnuendoAgent',
    version = '0.1.1',
    packages = find_packages(),
    install_requires=['PyYAML>=3.11', 'future>=0.16.0'],

    # Metadata for upload to PyPI
    author = 'Juan Urrego',
    author_email = 'juancho088@gmail.com',
    description = 'Python Agent for innuendo.io. It profiles and monitors a runtime code and it\'s capable to patch the code remotely',
    long_description = README,
    license = 'MIT License',
    keywords = 'newrelic graphite patch hotfix monitor health',
    url = 'https://github.com/juancho088/innuendo-agent-python',
    entry_points = {
        'console_scripts': [
            'innuendo-agent = innuendo:main'
        ]
    }
)
