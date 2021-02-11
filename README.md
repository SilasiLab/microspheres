# Microspheres
Python scripts and hardware assembly instructions for reproducing microsphere experiments

# General Info
To conduct our experiment we used a Raspberry Pi v3 to do our imaging and Ubuntu 16.04LTS to do our data processing. The instructions for the setup of our hardware can be found below under Assembly, and the instructions for running our custom Python script for imaging can be found below under get_image.py instructions.

After our imaging was complete we utilized a custom Python data processing script to map the microsphere locations in each mouses' brain to different regions as specified in the Allen Brain Atlas. The general usage of this custom script is explained below under localization.py instructions.

NOTES: Our scripts run on Python3 on Ubuntu and have not been tested with other Python versions or operating systems. The localization.py script was written with cross-platform use in mind, but has only been tested on Ubuntu.

When you are running $ python, please make sure that $ which python, points to your python3 installation. If running $ which python points to /usr/bin/python27 or another path suffixed with a number containing "2", please try running the scripts with $ python3.

# Hardware Assembly

# Cloning the Repo
1. make sure git is installed
2. press ctrl+alt+t to open a terminal window
3. $ cd ~
4. $ git clone https://github.com/silasilab/microspheres.git

# get_image.py Instructions
1. press ctrl+alt+t to open a terminal window
2. $ cd ~
3. $ cd microspheres
4. inspect the imports of this script and pip install whatever you are missing
5. $ python get_image.py
6. to take an image press spacebar

# localization.py Instructions
1. press ctrl+alt+t to open a terminal window
2. $ cd ~
3. $ cd microspheres
3. open up localization.py in a text editor and change the variable named "base_dir" at the top of the file to point to where your input directory is. You can do this with $ vim localization.py, $ nano localization.py, or with whichever other text editor you like using.
4. $ python localization.py
5. inspect the output files
