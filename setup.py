import sys
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name        = 'xsd_validator',
    version     = '0.0.3',
    description = 'Validates XML file against XSD, supporting XSD versionj 1.1',
    author      = 'Mike Kroutikov',
    author_email= 'mkroutikov@innodata.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url         ='https://github.com/innodatalabs/xsd-validator',
    license     ='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['xsd_validator'],
    package_data={'xsd_validator': ['resources/*.jar']},
    python_requires='>=3.6',
)
