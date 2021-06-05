#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter, freqz

#Get noisy signal
new_df = pd.read_csv('detailVol.csv')                 
array = new_df.loc[:1884,'Auxiliary' ]
noisy_signal = array.values
amplitude = np.sin(noisy_signal)
time = np.arange(-3*np.pi, 3*np.pi, 0.01)

# Plotting time vs amplitude using plot function from pyplot
plt.plot(time, amplitude)

# Settng title for the plot in blue color
plt.title('Sine Wave', color='b')

# Setting x axis label for the plot
plt.xlabel('Time'+ r'$\rightarrow$')

# Setting y axis label for the plot
plt.ylabel('Sin(time) '+ r'$\rightarrow$')

# Showing grid
plt.grid()

# Highlighting axis at x=0 and y=0
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Finally displaying the plot
plt.show()


# In[9]:


# Performing Low pass filtering of order = 3, cutoff freq = 2 at the rate of 30 Hz
# Parameters were chosen after trial-and-error of values

def butter_lowpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=3):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 3
fs = 30.0       # sample rate, Hz
cutoff = 2  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Demonstrate the use of the filter.
t = np.arange(-3*np.pi, 3*np.pi, 0.01)

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(noisy_signal, cutoff, fs, order)

plt.subplot(2, 1, 2)
plt.plot(t, noisy_signal, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()


# In[10]:


time = np.arange(-3*np.pi, 3*np.pi, 0.01)

# Plotting time vs amplitude using plot function from pyplot
plt.plot(time, y)

# Settng title for the plot in blue color
plt.title('Sine Wave', color='b')

# Setting x axis label for the plot
plt.xlabel('Time'+ r'$\rightarrow$')

# Setting y axis label for the plot
plt.ylabel('Sin(time) '+ r'$\rightarrow$')

# Showing grid
plt.grid()

# Highlighting axis at x=0 and y=0
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Finally displaying the plot
plt.show()


# In[ ]:




