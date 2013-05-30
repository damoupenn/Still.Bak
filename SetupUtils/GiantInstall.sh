#! /bin/bash

#apt-get install -y git gfortran python-numpy python-matplotlib python-pyfits cython xfonts-100dpi

cd /usr/share/fonts/X11/
mkfontdir
xset fp+ /usr/share/fonts/X11/100dpi
echo "FontPath /usr/share/fonts/X11/100dpi" >> ~/.xinitrc
cd -
#apt-get install -y gridengine-client gridengine-exec
