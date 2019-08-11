# ev3dev python starter
Basic Starter [ev3dev] + [Visual Studio Code][code] + [Python]


## Overview
This is a git repository to help you get started programming an EV3 robot using
ev3dev in Visual Studio Code using the Python programming language.



## Step-by-Step

### Create SD Card Image
1. Download Etcher
2. download ev3dev image from https://www.ev3dev.org/downloads/
3. write image onto SD card using etcher.
4. insert into ev3, and restart EV3. you should see 'brickman' when it boots

### Set up Development Environment (vscode+python)

1. Download and install python 3  https://www.python.org/downloads/release/python-374/
	Use advanced options to add it to your path

2. install python-ev3dev libraries using a command prompt

        C:\Users\dcowden>python
        Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> quit()

        C:\Users\dcowden>pip install python-ev3dev2
        Requirement already satisfied: python-ev3dev2 in c:\users\dcowden\appdata\local\programs\python\python37\lib\site-packages (2.0.0b3)
        Requirement already satisfied: Pillow in c:\users\dcowden\appdata\local\programs\python\python37\lib\site-packages (from python-ev3dev2) (6.1.0)
        You are using pip version 19.0.3, however version 19.2.2 is available.
        You should consider upgrading via the 'python -m pip install --upgrade pip' command.

        C:\Users\dcowden>python
        Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import ev3dev2
        >>> quit()

3. Download and install vscode. Use the user installer https://code.visualstudio.com/download

### Run Starter project

1. Download this project and unzip it to your computer

2. Open it using vscode Open Folder

3. Install the extensions recommended by the starter project: python and ev3d-browser

4. Connect the ev3 via USB

5. in the ev3dev device brower, connect to the brick. it should diplay a green circle when ready.

6. Press f5 to compile and run on the brick!



[ev3dev]: http://www.ev3dev.org
[code]: https://code.visualstudio.com/
[python]: https://www.python.org/
[git]: https://git-scm.com/
[github]: https://desktop.github.com/
