"""
Vercel serverless entry point for Django.

Vercel's @vercel/python builder looks for an `app` variable (WSGI callable)
in this file and wraps it in its own HTTP adapter — no gunicorn needed.
"""
import sys
import os
from pathlib import Path

# Make the project root importable from inside api/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IN16_Study_Manager.settings')

from IN16_Study_Manager.wsgi import application

# Vercel expects a variable named `app`
app = application
