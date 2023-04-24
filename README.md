# Doppler-Effect

Google Drive link to recorded audio files: https://drive.google.com/drive/folders/1yQQneIKmCHn39_ZXuQjp2Wj56uRJ_0WB?usp=share_link

## Aim
To study the Doppler effect in sound due to a rotating object and compute the speed of sound using the data collected.

## Theory
One might have noticed an ambulance sounding louder and more high pitched while moving towards an observer and when it moves away, the pitch seems lower. This is essentially the Doppler effect of sound. The frequency of sound emitted by an object with respect to the observer increases as the object moves towards the observer and decreases as it moves away. The observed frequency is related to the emitted frequency through the following equation –

$\nu = \left(\frac{c_{s} \pm v_{o}}{c_{s} \pm v_{s}}\right) \nu_{0}$

Where $c_{s}$ is the speed of sound, $\nu$ is the observed frequency, $\nu_{0}$ is the emitted frequency, $v_{o}$ is the velocity relative to observer, and $v_{s}$ is the velocity relative to the source. This can be simplified to –

$\nu = \left(\frac{c_{s}}{c_{s} - v}\right) \nu_{0} \approx \left(1 + \frac{v}{c_{s}}\right)\nu_{0}$

Now, for a rotating object, the speed is the same but the velocity keeps changing. So, one can use the velocity along the line of sight as reference. Consider the following diagram – 

<img width="204" alt="dop" src="https://user-images.githubusercontent.com/129873515/233897537-a60a56be-ee47-4daa-8b46-79d6a5bbf57d.png">

Figure 1. An object (here, a speaker) is rotating at a constant angular velocity $\omega$ = v/r. It emits a wave with a constant frequency $\nu_{0}$. The speaker moves from a maximum frequency at A to a minimum frequency at C.

Using equation (2), we get –

$\frac{\nu_{\text{max}}}{\nu_{0}} - \frac{\nu_{\text{min}}}{\nu_{0}} = \left(1 + \frac{v}{c_{s}}\right) - \left(1 - \frac{v}{c_{s}}\right) \Rightarrow \frac{2v}{c_{s}} = \frac{\nu_{\text{max}} - \nu_{\text{min}}}{\nu_{0}}$

Here, $v = \frac{2\pi r}{T}$, where $r$ is the radius and $T$ is the time period. The above relation could be used to find the speed of sound.

Apparatus
1. A custom Doppler Effect set-up with a rotating arm and speed control,
2. Two smartphones – one to play a particular frequency of sound and the other to record the emitted sound,
3. A Bluetooth speaker attached to this arm that can be paired with a phone,
4. A 12V, 9A battery to drive the motor,
5. A retort stand to clasp the phone.

## Experimental Set-up 
To ensure proper execution of the experiment, a stool should be placed on a level surface, onto which the custom Doppler Effect apparatus can be mounted. The apparatus comprises a rotating arm, a Bluetooth speaker attached to it, and a speed control mechanism. Next, one of the smartphones should be connected to the Bluetooth speaker on the apparatus. Simultaneously, a retort stand must be set up, and another smartphone should be secured to it, with the purpose of recording the sounds produced during the experiment. his methodology ensures the consistency and reproducibility of results, allowing for the accurate investigation of the Doppler Effect phenomenon.

## Procedure
### Data Collection
After assembling the apparatus and connecting the smartphone to the Bluetooth speaker, a 4000 Hz signal was transmitted through the speaker. To establish a baseline, the zero reading of the set-up (sound emitted without rotation) as recorded by aligning the smartphone with the orientation of the rotating arm, ensuring that they lie on the same plane. A frequency of 4000 Hz was selected for its high frequency, which minimizes the impact of low-frequency background noise on the results. The position of the smartphone at this point was considered to be on the "line of sight".

Using the speed control mechanism, the speed of the rotating arm was increased gradually at regular intervals. For each speed increment, the sound emitted by the set-up was recorded with respect to the position of the smartphone recording the sound. The sound signals were captured as audio files in the ***.m4a*** format, which were subsequently converted to \textbf{.wav} file type for processing using Python.

### Data Analysis
After loading the files onto Google Colaboratory in ***.wav*** format, relevant packages and libraries, such as NumPy, Matplotlib, and a user-defined *doppler_library*, were imported to analyse and process the data. First, using appropriate commands from *doppler_library*, a part of the signal data was loaded for the audio files of each of the speeds using the *load_signal* suction of the library, and the sample rate of the signal (number of samples per second), an array of individual time-points of the data and an array containing the values of amplitude at each time step were stored in separate variables (the loaded data was 'unpacked' into variables).

Then, the signal was broken up into various chunks (arrays of amplitude values) of default size 2048, and the dominant frequencies for each chunk were found using the *chunk_signal* (which returns the average time per chunk and the amplitudes) and the *power_spectrum* function (returns the dominant frequency for a particular chunk in the argument) respectively. Once this was done, the dominant frequencies were plotted against average time for each reading.

It was observed that faster graphs 'looked better' than the graphs for lower speeds as they were more uniform and had many steps. In the graphs, each step corresponds to some frequency, and the minimum change in frequency that can be detected is the frequency resolution of the graph. In the graphs, the resolution was close to 20 Hz which was not enough for the graphs for slower speeds as some frequencies overlapped. Therefore, the chunk size was modified for each reading by increasing the number of steps using the relation

$\text{Resolution} =  \frac{\Delta \nu}{N_{s}} = \frac{\text{Sample Rate}}{\text{Chunk Size}}$

Using the modified chunk sizes, the graphs were plotted again.
