from setuptools import setup, find_packages


def read_version():
    version = {}
    with open('arabic2latin/version.py', 'r') as f:
        exec(f.read(), version)
        return version['__version__']


setup(
    name='arabic2latin',
    version=read_version(),
    description='Convert Arabic characters to their Latin (English) homophones.',
    author='rexa222',
    author_email='rexa222@outlook.com',
    packages=find_packages(include=['arabic2latin', 'arabic2latin.*']),
    install_requires=open('requirements.txt').readlines(),
)
