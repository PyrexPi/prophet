# prophet

An audio guide for destroying oracles in Destiny's Vault of Glass raid.

This project allows you to make any encounter with oracles without having to look at them when spawning.
Lots of players can do this by ear-training but some are more proficent than others and there is always room for error.
With prophet you can take a look at the order so you don't need to memorize.

# Installation

You'll need the [latest release](https://github.com/PyrexPi/prophet/releases/latest) of the project and an audio source with the game.
This can be a stream from YouTube, Discord, Twitch, the game itself, etc. This works best if you get the audio clean, without any voices or background noise.

The best way you can accomplish this is with VAC ([Virtual Audio Cable](https://vac.muzychenko.net/)) or [VB-Cable](https://vb-audio.com/Cable/).
I have only tried the last one, but any solution that routes the audio to a microphone will work (even a microphone to speaker but be mindful of the noise).

To configure VB-Cable with Destiny 2 follow these steps:

1. Reboot after installing and reset your microphone and speakers to your previous configuration (when installed it'll default to CABLE)
2. Go to Settings -> System -> Sound

![settings](https://i.imgur.com/ahtgRk3.png)

3. Click on App volume and device preferences

![preferences](https://i.stack.imgur.com/GIPfJ.png)

4. Change the output of the application you want to monitor (usually Destiny 2) to CABLE Input. It has to be running for it to appear.

![preferences_2](https://i.stack.imgur.com/QcQvp.png)

_Note: Make sure you choose the output of the application and select CABLE Input (VB-Audio Virtual Cable)_

5. Go back to the Sound settings and select Sound control panel on the right

![sound control panel](https://imgur.com/iFVw3k5.png)

6. Select the Recording tab and right click on CABLE Input -> Properties.

![properties](https://imgur.com/Vp6O2DO.png)

7. Then go to the Listen tab and check the Listen to this device and then select where you want to hear the game (usually the default device).

![properties_2](https://imgur.com/srW2YTL.png)

All set and done! Now just open both executables (prophet.exe and interface.exe) and go to an encounter in the raid. Be sure to wait around 20 seconds before starting the encounter for best performance.
If you fail the oracles encounter it's better to reset the program just to be sure. For Atheon and Templar encounters isn't necessary.

# Possible future improvements

1. A way to route the application audio without external software.
2. A webapp running locally to replace the interface so you can see the order in your smartphone if you don't have a second screen.
3. Make some quality code adjustments to better organize and improve usability of it.
4. Test some solutions for console players.

Thanks and good luck!

# Notes

- If running on Windows, you will need to run the [following commands](https://stackoverflow.com/a/59594881/884296) to get the audio package `pyaudio` installed correctly:
  ```
  pip install pipwin
  pipwin install pyaudio
  ```
