# mac_changer
MAC Changer for Linux Distros

##INSTALLATION
apt-get install git
git clone https://github.com/neon-l/mac_changer.git


##USAGE
python mac_changer.py [options]


##OPTIONS
-i , --interface  > Interface to change its MAC Address
-m , --mac        > New MAC Address
-h , --help       > View this help

##Example
python mac_changer.py -i wlan0 -m aa:11:22:33:bb
