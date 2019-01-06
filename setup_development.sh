#!/usr/bin/env bash
sudo apt-get update
sudo apt-get --assume-yes install python3-pip python3-venv
if [ ! -d "venv" ]; then
	python3 -m venv venv
	source venv/bin/activate
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade Flask
	deactivate
fi
