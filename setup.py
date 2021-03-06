from setuptools import find_packages
from setuptools import setup

setup(
    name='ocfweb',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://www.ocf.berkeley.edu/',
    author='Open Computing Facility',
    author_email='help@ocf.berkeley.edu',
    install_requires=[
        'cachetools',
        'django>=1.8,<1.8.999',
        'gunicorn',
        'libsass',
        'lxml',
        'mistune',
        'ocflib',
        'python-dateutil',
    ],
    sass_manifests={
        'ocfweb': ('static/scss'),
    },
)
