# whisper-frontend
a Flask+JS frontend for communicating with a [whisper-docker](https://github.com/mitlabence/whisper-docker) container

# How-to
1. Make sure to have ffmpeg (tested on Windows 11 with ffmpeg version 2025-05-05-git-f4e72eb5a3-full_build-www.gyan.dev). Run `ffmpeg -version` to check the version.
2. Use `pip install -r requirements.txt` to create a python (e.g. anaconda) environent (python 3.13 is supported; tested on windows 11 with python 3.13.3 (v3.13.3:6280bb5)).
3. Start the Flask server with `python whisper-frontend.py`
