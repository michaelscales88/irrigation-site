#!/bin/bash

python get-pip.py

venv="test/"

if ! [ -d "$venv" ]
then
   mkdir "$venv"
fi

python3.5 -m venv "$venv"
source "$venv/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt
python main.py 8080 development.cfg
