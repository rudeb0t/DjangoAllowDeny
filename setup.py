import ez_setup
ez_setup.use_setuptools()

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
    description=open('README.rst').read(),
)
