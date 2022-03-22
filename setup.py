from setuptools import setup

setup(
    name='ipfsvault',
    version='0.1.0',
    description=
    "decentralize storage for authenticatino process package it uses ipfs for storing the data and multihash, md5, sha256, sha512 for authentication",
    url='https://github.com/rahulraikwar00/IpfaVault',
    author='Rahul Raikwar',
    author_email='rr200636@gmail.com',
    license='BSD 2-clause',
    packages=['ipfsvault'],
    install_requires=[
        'mpi4py>=2.0',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)