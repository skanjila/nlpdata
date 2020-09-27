from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Natural language processing datasets',
    long_description=readme,
    author='ludwig nlpdata dev team',
    author_email='sxk1969@hotmail.com',
    url='https://github.com/skanjila/nlpdata',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)