import click
import librosa
import pyrubberband as pyrb
from scipy.io import wavfile


@click.command()
@click.option('--infile', help='Absolute or relative file path')
@click.option('--outfile', help='Absolute or relative file path')
@click.option('--interval-start', default=None, help='The start of the interval of audio to slice. Should be of the form MM:SS.')
@click.option('--interval-end', default=None, help='The end of the interval of audio to slice. Should be of the form MM:SS.')
@click.option('--rates', default=None,
              help='''Stretch factor.  If ``rate > 1``, then the signal is sped up. If ``rate < 1``, 
              then the signal is slowed down. You can specify multiple output rates like so: 0.5,0.6,0.7''')
def audio_scaler(infile, outfile, interval_start, interval_end, rates):
    """Slice an audio file to a specific interval and scale the speed by a positive factor"""

    y, sr = librosa.load(infile)
    rates = [float(x) for x in rates.split(',')]
    
    if interval_start:
        minutes, seconds = [int(x) for x in interval_start.split(':')]
        slice_ix_begin = sr * (60 * minutes + seconds)
    else:
        slice_ix_begin = 0
    
    if interval_end:
        minutes, seconds = [int(x) for x in interval_end.split(':')]
        slice_ix_end = sr * (60 * minutes + seconds)
    else:
        slice_ix_end = -1

    y_slice = y[slice_ix_begin:slice_ix_end]

    for r in rates:
        y_scaled = pyrb.time_stretch(y_slice, sr, r)
        wavfile.write(f'{outfile}_{round(r*100)}.wav', sr, y_scaled)

if __name__ == '__main__':
    audio_scaler()
