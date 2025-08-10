from setuptools import setup, find_packages

setup(
    name='file-organizer',
    version='1.0.0',
    description='A Python script to organize files into categorized folders',
    author='Vikram Mistry',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'file-organizer=file_organizer.main:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
)