"""pyvesync setup script."""

from os import path
from setuptools import setup, find_packages


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cosmin-cucu_pyvesyncv2',
    version='0.1',
    description='pyvesync is a library to manage Etekcity\
                 Devices, Cosori Air Fryers and Levoit Air \
                     Purifiers run on the VeSync app.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cosmin-cucu/pyvesyncV2',
    author='Mark Perdue, Joe Trabulsy, Tv4you2016',
    author_email='tv4you2016@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=['iot', 'vesync', 'levoit', 'etekcity', 'cosori', 'valceno'],
    packages=find_packages('src', exclude=['tests', 'test*']),
    package_dir={'': 'src'},
    install_requires=['requests>=2.20.0'],
    extras_require={
        'dev': ['pytest', 'pytest-cov', 'yaml', 'tox']
    },
    python_requires='>=3.8',
)
