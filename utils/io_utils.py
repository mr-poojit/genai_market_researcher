# utils/io_utils.py
import os, json
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_markdown(path, content):
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def write_json(path, data):
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
