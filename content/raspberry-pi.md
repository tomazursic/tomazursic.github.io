title: Raspberry Pi
date: 2017-02-10 14:29
category: blog
tags: pi, arm, linux
summary: Setup and usage of Raspian Pi

**Advice is use TMUX! Run all commands in tmux session to prevent catastrophic consequences**

## Setup

### Step 1: Flash Operating System

You need to flash a micro SD image with an operating system.

```sh
    Download Raspian Lite(Stretch) (352MB).
    Follow OS specific guides here.
    Leave micro SD card in your machine and edit/create some files as below:
```

Get the image:

```sh
    https://www.raspberrypi.org/downloads/raspbian/
```

Latest image: `raspbian_lite-2019-09-30/2019-09-26-raspbian-buster-lite.zip`

```sh
    wget https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-09-30/2019-09-26-raspbian-buster-lite.zip
```


bring img on sd card

```sh
    sudo pv -tpreb name.img | sudo dd of=/dev/sdX bs=4M
```

create image from sd card

```sh
    sudo pv -tpreb /dev/sdX | sudo dd of=name.img bs=4M
```

### Step 2: Setup the WiFi for first boot

We can create a special file which will be used to login to wifi on first boot. More reading here, but we will walk you through it.

On Windows, with your memory card image burned and memory disc still inserted, you should see two drives, which are actually two partitions on the mem disc. One is labeled boot. On Mac and Linux, you should also have access to the boot partition of the mem disc. This is formatted with the common FAT type and is where we will edit some files to help it find and log-on to your wifi on its first boot.

```sh
    Note: If boot is not visible right away, try unplugging and re-inserting the memory card reader.

    Start a text editor: gedit on Linux. Notepad++ on Windows. TextEdit on a Mac.
    Paste and edit this contents to match your wifi:

    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="<your network name>"
        psk="<your password>"
    }
```

Replace <your network name> with the ID of your network. Leave the quotes. I've seen problems when the network name contained an apostrophe, like "Joe's iPhone". Replace <your password> with your password, leaving it surrounded by quotes. If it bothers you to leave your password unencrypted, you may change the contents later once you've gotten the pi to boot and log-in.

```sh
    Save this file to the root of boot partition with the filename wpa_supplicant.conf. On first boot, this file will be moved to /etc/wpa_supplicant/wpa_supplicant.conf where it may be edited later. If you are using Notepad on Windows, make sure it doesn't have a .txt at the end.
```

### Step 3: Setup Pi's Hostname

```sh
    Note: This step only possible on a linux host pc. Otherwise you can set it up later in raspi-config after logging in to your pi.
```

We can also setup the hostname so that your Pi easier to find once on the network. If yours is the only Pi on the network, then you can find it with

ping raspberrypi.local

once it's booted. If there are many other Pi's on the network, then this will have problems. If you are on a Linux machine, or are able to edit the UUID partition, then you can edit the /etc/hostname and /etc/hosts files now to make finding your pi on the network easier after boot. Edit those to replace raspberrypi with a name of your choosing. Use all lower case, no special characters, no hyphens, yes underscores _.

```sh
    sudo vi /media/userID/UUID/etc/hostname
    sudo vi /media/userID/UUID/etc/hosts
```

### Step 4: Enable SSH on Boot

Put a file named ssh in the root of your boot partition.

Now your SD card is ready. Eject it from your computer, put it in the Pi and plug in the Pi.

### Step 5: Connecting to the Pi

If you followed the above instructions to add wifi access, your Pi should now be connected to your wifi network. Now you need to find its IP address so you can connect to it via SSH.

The easiest way (on Ubuntu) is to use the findcar donkey command. You can try ping raspberrypi.local. If you've modified the hostname, then you should try:

```sh
    ping <your hostname>.local
```

This will fail on a windows machine. Windows users will need the full IP address (unless using cygwin).

If you are having troubles locating your Pi on the network, you will want to plug in an HDMI monitor and USB keyboard into the Pi. Boot it. Login with:

```sh
    Username: pi
    Password: raspberry
```

Then try the command:

```sh
    ifconfig wlan0
```

If this has a valid IPv4 address, 4 groups of numbers separated by dots, then you can try that with your SSH command. If you don't see anything like that, then your wifi config might have a mistake. You can try to fix with

```sh
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

If you don't have a HDMI monitor and keyboard, you can plug-in the Pi with a CAT5 cable to a router with DHCP. If that router is on the same network as your PC, you can try:

```sh
    ping raspberrypi.local
```

Hopefully, one of those methods worked and you are now ready to SSH into your Pi. On Mac and Linux, you can open Terminal. On Windows you can install Putty, one of the alternatives, or on Windows 10 you may have ssh via the command prompt.

If you have a command prompt, you can try:

```sh
    ssh pi@raspberrypi.local
```

or

```sh
    ssh pi@<your pi ip address>
```

or via Putty.

```sh
    Username: pi
    Password: raspberry
    Hostname:<your pi IP address>
```

### Step 6: Update and Upgrade

```sh
    sudo apt-get update
    sudo apt-get upgrade
```

### Step 7: Raspi-config

```sh
sudo raspi-config

    change default password for pi
    change hostname
    enable Interfacing Options | I2C
    enable Interfacing Options | Camera
    Advanced Options | Exapand Filesystem
```

Choose and hit enter.

```sh
    Note: Reboot after changing these settings. Should happen if you say yes.
```

### Step 8: Install Dependencies

```sh
sudo apt-get install \
         build-essential python3 python3-dev python3-pip \
         python3-virtualenv python3-numpy python3-picamera python3-pandas \
         python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev \
         gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp
```

### Step 9: Install Optional OpenCV Dependencies

If you are going for a minimal install, you can get by without these. But it can be handy to have OpenCV.

```sh
    sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev \
    libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev \
    libswscale-dev libqtgui4 libqt4-test
```

### Step 10: Setup Virtual Env

```sh
    python3 -m virtualenv -p python3 env --system-site-packages
    echo "source env/bin/activate" >> ~/.bashrc
    source ~/.bashrc
```

Modifying your .bashrc in this way will automatically enable this environment
each time you login. To return to the system python you can type deactivate.

### Step 11: Install Donkeycar Python Code

Change to a dir you would like to use as the head of your projects.

```sh
    mkdir projects
    cd projects
```

### Fix the LC_errors

```sh
    etc/envirmonet
    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
    LC_ALL=en_GB.UTF-8
    LANG=en_GB.UTF-8
```


### Install Open CV

```sh
    sudo apt install python3-opencv
```


## Setup I2C

```sh
    sudo usermod -aG i2c <username>
    sudo reboot
```

After a reboot, then try:

```sh
    sudo i2cdetect -r -y 1
```

Raspberry Pi:

```sh
    sudo apt-get install i2c-tools
    sudo i2cdetect -y 1
```

This should show you a grid of addresses like:

```sh
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: 70 -- -- -- -- -- -- --
```

In this case, the 40 shows up as the address of our PCA9685 board. If this does
not show up, then check your wiring to the board. On a pi, ensure I2C is
enabled in sudo raspi-config


## Nodejs

use of nvm

```sh
    https://github.com/nvm-sh/nvm
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh | bash
    source ~/.bashrc
    nvm --version
    nvm install node
```

## Links

* [raspberry-pi-auto-wifi-hotspot-switch-direct-connection](https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/158-raspberry-pi-auto-wifi-hotspot-switch-direct-connection)
* [Tensorflow ARM](https://github.com/lhelontra/tensorflow-on-arm/releases)
* [UFW Firewall](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

## Motioneye

https://github.com/ccrisan/motioneyeos/releases
