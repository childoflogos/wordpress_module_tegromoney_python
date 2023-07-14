from setuptools import setup

setup(
    name='wordpress_tegromoney_python',
    version='1.0.0',
    author='childoflogos',
    description='A Python module for integrating Tegro Money into your website',
    packages=['wordpress_tegromoney_python'],
    install_requires=[
        'requests',
        'flask',
    ],
)