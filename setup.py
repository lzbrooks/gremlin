from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    project_license = f.read()

setup(
    name='gremlin',
    version='0.1.0',
    description='Binary array based tagging system',
    long_description=readme,
    author='Lizann Brooks',
    author_email='brooks.lizan@gmail.com',
    url='https://github.com/lzbrooks/gremlin',
    license=project_license,
    packages=find_packages(exclude=('tests', 'docs'))
)
