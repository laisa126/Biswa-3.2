#!/usr/bin/env bash
# Vercel runs this script automatically during the build phase.
# It generates the staticfiles/ directory so WhiteNoise can serve them at runtime.

set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete."
