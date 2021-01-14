#!/bin/bash

# Upload to PyPI
# 1. Delete all the file in dist if exists.
# 2. Build dist by `python setup.py sdist bdist_wheel`.
# 3. Upload by `twine upload dist/*`.
# Note: Login with username not email.

# python -m pip install -U setuptools wheel twine
rm -rf build dist penut_utils.egg-info
python setup.py sdist bdist_wheel
# python -m twine upload --repository testpypi dist/* # Upload to test pypi
python -m twine upload dist/*

# Install from test pypi
# python -m pip install -i https://test.pypi.org/simple/ penut