ElpAPI
======

Welcome to ElpAPI the python API for the Elphel cameras

this API serves the purpose of helping developers create applications that use the Elphel camera.
in this repository there are two kinds of script, the scripts, and the meta scripts,

scripts are the code that use the matascripts of the API, and the metadcripts are the code that conforms the API

the core of the API is in the matascript ElpAPI.py, and autosetup.py is the script that autosetups the camera,
if you want to know how it works you might chek both of those scripts

install
-----------------
type: "git clone git://github.com/BielBdeLuna/ElpAPI.git" form the folder you want the code in.


autosetup.py
-----------------
in order tot est it, you need to create a "elphel" directory in your user directory:

/home/yourusernamedir/elphel/

then there you need to have a XML that controls your wanted values to send to the camera, 
you can create that file straight from the camera by doing the following:

setup the camera with the Exposure of your liking form within the php program in the camera.

then in the "elphel" directory in your computer cll the following lines in the terminal:

"
cameraIP = insert your camera's IP here

wget 'http://cameraIP/parsedit.php?immediate&EXPOS&' -O wanted_settings.xml
"

once you have a correct wanted_settings.xml in your folder 
you can reboot the camera, so it will have it's default EXPOS value (exposure value) then you can 
call autosetup.py form the directory you have it, and the camera will change it's EXPOS value to
the one you have in the XML.
