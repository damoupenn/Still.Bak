#$ /bin/bash

echo 'deb http://linux.dell.com/repo/community/deb/latest /' | sudo tee -a /etc/apt/sources.list.d/linux.dell.com.sources.list
gpg --keyserver pool.sks-keyservers.net --recv-key 1285491434D8786F
gpg -a --export 1285491434D8786F | sudo apt-key add -
sudo apt-get update

sudo apt-get install -y srvadmin-all

sudo service dataeng start
sudo python setup_omconfig.py
