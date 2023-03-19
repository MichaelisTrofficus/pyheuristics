#!/usr/bin/env bash

# Get Package Name and Version to configure a name (It will also need a BUILD)
PACKAGE_VERSION=$(python setup.py --version 2>/dev/null)
echo -e "${PACKAGE_VERSION}" | sort -r -V | head -n 1
