from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='sse_script',
    version='0.1.0',
    description='SSE Consume & Query script',
    long_description=readme,
    author='Kara N.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)