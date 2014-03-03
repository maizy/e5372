from setuptools import setup

setup(
    name='e5372',
    version='0.0.1',
    packages=['e5372'],
    install_requires=['requests'],
    tests_require=['nose>=1.3', 'pep8>=1.3'],
    test_suite='nose.collector',
    scripts=['bin/e5372_status'],
    exclude=['e5372_tests/*'],
    author='Nikita Kovaliov',
    author_email='nikita@maizy.ru',
    description='Huawei E5372 API (also known as MegaFon MR100-3)',
    license='GPLv3',
    keywords='e5372 mr100-3',
    url='https://github.com/maizy/e5372',
)
