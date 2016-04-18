import os
from setuptools import setup, find_packages
import hero_slider


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-hero-slider",
    version=hero_slider.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, gallery, slider, bootstrap, frontpage, generic',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold@bitmazk.com',
    url="https://github.com/bitmazk/django-hero-slider",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        'pillow',
        'django-hvad',
        'django-filer',
        'django-libs',
    ],
)
