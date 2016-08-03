from setuptools import setup, find_packages

setup(
    name='google-search-console',
    version='1.0.0',
    url='https://bitbucket.org/maksymcherevko/google-search-console',
    packages = [
        'sc-crawl-errors',
    ],
    install_requires = [
        'google-api-python-client>=1.5',
    ],
    package_data = {
        'sc-crawl-errors' : ['*.json']
    },
    include_package_data = True,
)