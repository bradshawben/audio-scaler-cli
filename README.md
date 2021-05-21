# audio-scaler-cli
A simple command line utility for stretching audio files

# Installation
- Make sure you have a reasonably recent installation of python3 on your machine
- Install a virtualenv and source it if you don't want to clutter your global python installation
- `./setup.sh`

# Usage
The audio-scaler CLI is pretty bare bones at this point. It does two things:
1. It allows you to slice an audio file between two time points
2. It allows you to scale the sliced audio to a set of rates

After doing (1) and (2) it will write N .wav files, one for each rate specified. Currently only .wav file exports are supported since I didn't want to require ffmpeg.
You can pass in mp3 files or wav files.

```
# Halp!
python audio_scale.py --help
```

```
# Example usage
> python audio_scaler.py --infile my_audio.mp3 --outfile my_outfile --interval-start 00:05 --interval-end 00:10 --rates 0.6,0.7,0.8

> ls
my_outfile_60.wav   my_outfile_70.wav   my_outfile_80.wav
```
