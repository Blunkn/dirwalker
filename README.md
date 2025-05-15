# DirWalker 
Version 0.2.0
---

A simple recursive directory scanner and searcher.

Script inspired by a moment in a previous CTF where I had to script something to scrape a directory on the fly. I did not manage that and am still salty to this day.

WARNING: DirWalker is in its initial stages of development. Highly unstable and non-functional at the moment.

## Features
---
- Scrapes a given directory(takes current directory if not), and outputs directories & files.
- Searches for a specific file name or extension in a given directory(takes current directory otherwise).

## Dependencies
---

filling this up later

## How to Use
---
- Download as .zip, extract the .py file.
- When your File Explorer is on the directory the .py program is on, click on the directory bar and type "cmd".
- Type in the command "py dirwalker.py" to run it.

## Issues
---
N/A

## Roadmap
---
- find a way to have scan function output a text visualisation of larger directories
- expand search function to be able to search extensions

## Version Control
---
0.2.0 - additions
- scanning is now recursive but can accummulate noise depending on size of subdirectories
- search added

0.1.0 - initial commit