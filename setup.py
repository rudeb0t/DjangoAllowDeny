from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup
from django_allowdeny import NAME, VERSION

setup(
    name=NAME,
    version=VERSION,
    author='Nimrod A. Abing',
    author_email='nimrod.abing@gmail.com',
    packages=['django_allowdeny'],
    package_data={
        'django_allowdeny': ['templates/allowdeny/*.html'],
    },
    url='https://github.com/rudeb0t/DjangoAllowDeny',
    license='LICENSE.txt',
    description='Simple allow/deny access control for Django projects.',
    long_description=open('README.rst').read(),
)
