#!/bin/bash
# Maintainer: Michael Scales
# This script runs the irrigation-site
# In addition to running the site this script
# will attempt to install all the requirements.

# Ensure pip is installed, or provide a copy of
# get-pip in this directory.
if [ -f get-pip.py ]
then
   python get-pip.py
fi

venv="venv/"

if ! [ -d "$venv" ]
then
   mkdir "$venv"
fi

python -m venv "$venv"
source "$venv/Scripts/activate"
pip install --upgrade pip
pip install -r requirements.txt
python main.py 8080 development.cfg
