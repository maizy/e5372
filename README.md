# Huawei E5372 API

Also known as Megafon MR100-3.

Currently only tested with Megafon MR100-3.

Alpha version.


## Usage

_TODO_


## Included binaries

_TODO_


## Installation
```
python setup.py install
```


## Installation on external server

Build an .egg and install it through easy_install.

```
python setup.py bdist_egg
scp dist/e5372-*-py2.7.egg user@host:~/
ssh user@host
easy_install e5372-*-py2.7.egg
```


## Installation with pip and git

```
pip install git+git://github.com/maizy/e5372.git
```


## Development

```
python setup.py develop
```

Hack.

Run tests:

```
python setup.py test
```

for more verbose output:

```
nosetest e5372_tests
```

Send pull request.
