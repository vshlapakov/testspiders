from setuptools import setup, find_packages

setup(
    name         = 'testspiders',
    version      = '1.0',
    packages     = find_packages(),
    package_data = {'testspiders': ['resources/*.png']},
    entry_points = {'scrapy': ['settings = testspiders.settings']},
    scripts = ['bin/testargs.py'],
    zip_safe = False,
)
