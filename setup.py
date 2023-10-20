from setuptools import setup, find_packages

setup(
    name='ligPrep',
    version='0.01',
    author="Young",
    author_email="he.yang@siat.ac.cn",
    url='https://github.com/UR-Free/unidock_tools',
    description="A ligand processing tool for AutoDock",
    packages=find_packages(),
    install_requires=['rdkit', 'networkx', 'numpy'],
    include_package_data=True
)
