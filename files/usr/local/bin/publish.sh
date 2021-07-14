#!/usr/bin/env bash

set -e
set -x

PROJECT_DIR=/usr/local/src/project

# set version here. tag-version will blow the script up if it is not a clean working copy.
VERSION=$(tag-version)
export VERSION=$VERSION
echo $VERSION

VERSION_PLACEHOLDER="version='0.0.0',"
sed -i "s/$VERSION_PLACEHOLDER/version='$VERSION',/" $PROJECT_DIR/setup.py


DIST_DIR=$PROJECT_DIR/dist
python setup.py sdist --dist-dir $DIST_DIR
twine upload dist/wayscript-legacy-$VERSION.tar.gz
