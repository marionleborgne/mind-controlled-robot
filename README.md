I hacked a toy robot to control it with my brain:
* If I concentrate the robot goes forward. 
* If I meditate, the robot turns left.

Here's a little video :-)

![Mind Controlled Robot](http://img.youtube.com/vi/zlUZ6bhUcBk/0.jpg)](http://www.youtube.com/embed/zlUZ6bhUcBk)

The EEG headset I am using to analyze my brainwaves is the Neurosky Mindwave Mobile.

The remote of the toy robot - aka "The Bug" - is hacked and connected to an Arduino microcontroller.

####To control the robot I used these 2 simple principles:
* Meditation produces alpha waves (frequency range: 7.5-12.5 Hz)
* Attention produces beta waves (frequency range: 12.5-30 Hz)

So by isolating these 2 frequencies in my brainwaves, I can trigger the right signals to control the robot. 

####Here is the chain of events:
* The EEG headset records my brainwaves.
* The brainwaves are analyzed on my computer to isolate the right frequencies.
* The computer is connected to an Arduino microcontroller. The Arduino gets a specific input for each frequency detected.
* The Arduino is connected to the robot remote (hacked)
