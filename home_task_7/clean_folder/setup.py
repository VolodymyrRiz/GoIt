from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',    
    description='Програма для впорядкування папки',
    url='https://github.com/VolodymyrRiz/GoIt/tree/main/home_task_7/clean_folder',
    author='Volodymyr Rizun',
    author_email='v.v.rizun@gmail.com',
    license='NNN',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
)