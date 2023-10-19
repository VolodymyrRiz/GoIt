from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',    
    description='Програма для впорядкування папки',
    url='http://github.com/dummy_user/useful',
    author='Volodymyr Rizun',
    author_email='v.v.rizun@gmail.com',
    license='***',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
)