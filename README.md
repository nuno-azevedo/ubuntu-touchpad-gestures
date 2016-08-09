# Ubuntu Touchpad Gestures

### Dependencies
```bash
$ sudo apt-get -y install --no-install-recommends xdotool
```

#### [Only for Ubuntu 14.04 and above] Install older version of Synaptics driver to have access to touchpad event logging
```bash
$ sudo apt-get -y install --no-install-recommends autoconf automake build-essential libevdev-dev libmtdev-dev xorg-dev xutils-dev libtool
$ sudo apt-get -y autoremove --purge xserver-xorg-input-synaptics
$ git clone https://github.com/Chosko/xserver-xorg-input-synaptics.git
$ cd xserver-xorg-input-synaptics
$ ./autogen.sh
$ ./configure --exec_prefix=/usr
$ make
$ sudo make install
$ cd ..
$ rm -rf xserver-xorg-input-synaptics
```

#### Install
```bash
$ git clone https://github.com/nuno-azevedo/ubuntu-touchpad-gestures.git
$ sudo mv ubuntu-touchpad-gestures/touchpad-gestures.py /usr/local/bin/touchpad-gestures
$ sudo chmod 755 /usr/local/bin/touch-gestures
$ sudo mkdir -p /etc/X11/xorg.conf.d/
$ sudo mv ubuntu-touchpad-gestures/50-synaptics.conf /etc/X11/xorg.conf.d/50-synaptics.conf
$ mv ubuntu-touchpad-gestures/touchpad-gestures.desktop ~/.config/autostart/
$ chmod 775 ~/.config/autostart/touchpad-gestures.desktop
$ rm -rf ubuntu-touchpad-gestures
$ reboot
```
