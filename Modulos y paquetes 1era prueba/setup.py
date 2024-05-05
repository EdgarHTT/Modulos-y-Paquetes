from setuptools import setup

setup(
    name='Mensajes',
    version='2.0',
    description='Un paquete para saludar y despedir',
    author='Edgar Humberto Tijerina Tamez',
    author_email='Edgarhumberto1999@gmail.com',
    url='https://github.com/EdgarHTT',
    packages=['mensajes','mensajes.hola','mensajes.adios'],
    scripts=['test.py']
)