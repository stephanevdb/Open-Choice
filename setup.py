from setuptools import setup, find_packages

setup(
    name='Open-Choice',
    version='1.0.0',
    description='A web application for creating and managing polls',
    author='Stéphane Van den Broeck',
    author_email='mail@stephanevdb.com',
    url='https://github.com/stephanevdb/Open-Choice',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.0.0',
        'sqlite3'
    ],
    entry_points={
        'console_scripts': [
            'open-choice=app:main',
        ],
    },
)