#!/usr/bin/env bash
source venv/bin/activate
export FLASK_APP=Flask/app.py
export FLASK_ENV=development
python3 -m flask run
