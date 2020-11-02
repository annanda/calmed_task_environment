#!/usr/bin/python
import sys
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_folder)

from app import app

if __name__ == "__main__":
    app.run()
