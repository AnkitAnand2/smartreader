from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='Smartreader',
    version='0.1',
    install_requires=required,
    description='Package for PDF text to Speech',
    author='Ankit_Anand',
    author_email='ankitanand5024@gmail.com',
    license='unlicense',
    packages=['Smartreader'],
    zip_safe=False
)