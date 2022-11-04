from setuptools import setup

install_requires = [
]

extra_require = {
    'test': ['pytest'],
}


def readme():
    with open('README.md', 'r') as f:
        return f.read()


def set_entry_points():
    r = {}
    #r['console_scripts'] = [
    #    'parse_lpp=lppParser.tools:main',
    #]
    return r

setup(
    name='lppParser',
    version='0.0.7',
    description='Parse .lpp file format',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/archman/lppParser',
    author='Tong Zhang',
    author_email='zhangt@frib.msu.edu',
    packages=[
        'lpp_parser.tests',
        'lpp_parser.data',
        'lpp_parser'],
    package_dir={
        'lpp_parser.tests': 'tests',
        'lpp_parser.data': 'main/data',
        'lpp_parser': 'main'
    },
    include_package_data=True,
    install_requires=install_requires,
    extra_require=extra_require,
    entry_points=set_entry_points(),
    license='GPL3+',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Physics'],
)
