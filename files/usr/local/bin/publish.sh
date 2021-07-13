#!/usr/bin/env bash

set -e
set -x

# set version here. tag-version will blow the script up if it is not a clean working copy.
VERSION=$(tag-version)
export VERSION=$VERSION
echo $VERSION

DIST_DIR=/usr/local/src/project/dist
python setup.py sdist --dist-dir $DIST_DIR
twine upload dist/wayscript-legacy-$VERSION.tar.gz
