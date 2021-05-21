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
> python audio_scale.py --help
Usage: audio_scaler.py [OPTIONS]

  Slice an audio file to a specific interval and scale the speed by a positive
  factor

Options:
  --infile TEXT          Absolute or relative file path
  --interval-start TEXT  The start of the interval of audio to slice. Should
                         be of the form MM:SS.
  --interval-end TEXT    The end of the interval of audio to slice. Should be
                         of the form MM:SS.
  --rates TEXT           Stretch factor.  If ``rate > 1``, then the signal is
                         sped up. If ``rate < 1``,  then the signal is slowed
                         down. You can specify multiple output rates like so:
                         0.5,0.6,0.7
  --help                 Show this message and exit.
```

```
# Example usage
> python audio_scaler.py --infile my_audio.mp3 --interval-start 00:05 --interval-end 00:10 --rates 0.6,0.7,0.8

> ls
my_audio_60.wav   my_audio_70.wav   my_audio_80.wav
```
