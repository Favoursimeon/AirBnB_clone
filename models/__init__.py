#!/usr/bin/python3
""" THIS imports the FileStorage module."""
from models.engine.file_storage import FileStorage as fs

storage = fs()
storage.reload()
