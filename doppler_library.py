#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def load_signal(filename, color='royalblue', plot=False, clip=None, fig=None, ax=None):

    """
    The load signal function loads a `.wav` file and returns the time-series information and the sample rate.

    Parameters:
    -----------
    • filename: A string pointing to the location of the .wav file.
    • clip: A two-element list [a,b] and clips the input signal between 
            the times a and b (in seconds) and returns the signal. This can be useful if you want
            to remove the first a seconds or the last b seconds of your sound file. By default, no
            clipping is done.
    • plot: This is a boolean variable that can either be True or False, based on whether
            you want to plot the resulting signal or not. By default, the signal is not plotted.
    • color: sets the colour of this plot. By default, the colour is royalblue
    • fig and ax decide which canvas to plot your result on. This is a little advanced, don’t
            worry about it yet.

    Returns:
    --------
    The function returns three values (in this order):
    • samplerate: The sample rate of the signal. This is defined as the number of datapoints
                of the input signal per second. Typically, most recordings are taken at 44,100 Hz,
                meaning that there are 44,100 samples in each second.
    • times: An array of each individual time-point of the data.
    • signal: An array containing the value of the amplitude of the signal at each time-step
            in times.

    Usage:
    ------
    sr,times,sig = load signal("./filename.wav", clip=[3,20], plot=True, color=’firebrick’, fig=None, ax=None)
    """


    samplerate, signal = wavfile.read(filename)
    
    if(signal.ndim > 1):
        signal = np.mean(signal, axis=1)
    
    if(plot and ax==None):
        fig, ax = plt.subplots()
        
    T = len(signal)/samplerate
    times = np.linspace(0,T,len(signal))
    
    if(clip!=None):
        if(clip[0] > clip[1]):
            raise ValueError("Clipping Error: the `clip` array should be in ascending order, i.e. the code requires clip[0]<clip[1].")
        mask = (times>clip[0]) & (times<clip[1])
        
        times = times[mask]
        times = times-times[0]
        signal = signal[mask]
    
    if(plot):
        ax.plot(times, signal, color=color)
    
    return samplerate, times, signal


def chunk_signal(times, signal, size=2048, step=128):

    """
    This function breaks up a signal (given in the `signal` array) into individual pieces
    (or chunks) of size `size`, whose left-edges are separated by a `step` samples. The splitting 
    is thus done with significant overlap. For each of these chunks, it returns the average time 
    at which the chunk was taken, and the amplitude values within that chunk.

    Parameters:
    -----------
    • times: An array of times, usually the output of the `load_signal` function.
    • signal: An array of amplitudes for each of the times given above, also one of the
              outputs of the `load_signal` function.
    • size and step: The number of samples in the interval, and the number of steps between
                     samples, as described above. The default values are 2048 and 128 respectively.

    Returns:
    --------
    • avg_t: A one-dimensional array containing the average time values for each of the
             chunks.
    • chunks: A two-dimensional array. The first dimension is the chunk-number. For each
              chunk, it returns size number of amplitude values.

    Usage:
    ------
    avg_t,chunks = chunk signal(times, sig)

    """

    n_steps = len(signal)
    
    n_chunks = (n_steps-size) // step
    
    array = np.zeros((n_chunks, size))
    t = np.zeros(n_chunks)
    
    counter = 0
    while(counter < n_chunks):
        start = counter*step
        end = start + size
        
        array[counter] = signal[start:end]
        t[counter] = (times[start]+times[end])/2
        
        counter += 1
    
    return t, array


def power_spectrum(chunk, samplerate, color='tomato', plot=False, fig=None, ax=None,  label=None, lowx=1000, highx=5000):

    """
    This function accepts a signal and computes its power spectrum, returning the dominant
    frequency in the range [`lowx`, `highx`]. Ideally, this range should be centered around your stationary frequency, and should be
    wide enough contain all the variation in the frequency during the object’s motion.

    Parameters:
    -----------
    • chunk: An array of amplitude values, usually a specific chunk that was returned by the
             of the chunk signal function.
    • samplerate: The original samplerate of the signal, obtained from the load signal
                  function.
    • lowx and highx: This is the range of frequencies within which to look for a maximum.
    • plot: A boolean variable that can either be True or False, based on whether you want 
            to plot the resulting power spectrum or not. By default, the power spectrum is not plotted.
    • color and label: sets the colour and label of this plot. By default, the colour is `tomato`, 
                       and the no label is sent in.
    • fig and ax decide which canvas to plot your result on. This is a little advanced, don’t
                 worry about it yet.


    Returns:
    --------
    • maxfreq: The frequency in the range [`lowx`,`highx`] that contributes the greatest deal to our signal
               in the given range of frequencies.

    Usage:
    ------
    dominant frequency=power spectrum(chunks[0], samplerate, lowx=2000, highx=4000)
    """
    
    signal = chunk - np.mean(chunk)
    
    signal = signal*np.hamming(len(signal))
    
    
    if(plot==True and ax==None):
        fig, ax = plt.subplots()
        
    N = len(signal)

    ft_array = np.abs(np.fft.fft(signal))
    fftfreqs = np.fft.fftfreq(len(signal), d=1/samplerate)
    
    mask = (fftfreqs>lowx) & (fftfreqs<highx)
    clipped_freqs = fftfreqs[mask]
    clipped_ft = ft_array[mask]
    
    if(plot==True):
        ax.plot(clipped_freqs, clipped_ft, color=color, label= label)
    
    max_ps = np.max(clipped_ft)
    
    max_freq = clipped_freqs[clipped_ft==max_ps][0]
    
    return max_freq



