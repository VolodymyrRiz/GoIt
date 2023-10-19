from setuptools import setup, find_namespace_packages

setup(
    name='vvr',
    version='0.0.1',
    description='Very useful code',
    author='Volodymyr Rizun',
    author_email='flyingcircus@example.com',    
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greet=vvr.main:greeting']}
)