# Polybar Collection

My personal collection.

## Getting Started

Things you need to install first.

### Prerequisites

You need to install Polybar and FontAwesome:

Debian

```bash
sudo apt install polybar fonts-font-awesome
```

Ubuntu

```bash
sudo apt install build-essential git cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev fonts-font-awesome

git clone --recursive https://github.com/polybar/polybar && cd polybar && mkdir build && cd build && cmake .. && make -j$(nproc) && sudo make install
```

Fedora

```bash
sudo dnf install polybar fontawesome-fonts
```

If you're having trouble I highly recommend you to take a look at [polybar repo](https://github.com/polybar/polybar).

Also you need to download and install this font from [nerd fonts](https://www.nerdfonts.com/font-downloads):

* JetBrainsMono

To install just download the font, move/copy to the folder ~/.fonts and run in the terminal:

```bash
fc-cache -fv
```

### Installing

First you need to download or clone the repo:

```bash
git clone https://github.com/Murzchnvok/polybar-collection
```

You could copy or move a config folder to *~/.config/* doing this:

```bash
cp -r polybar-collection/material ~/.config/polybar
```

but what I recommend is to use the launch.sh script to launch the config file you want from the polybar-collection folder.

If you're using bspwm you need to add something like this to your bspwmrc:

```bash
$HOME/Projects/fun/polybar-collection/launch.sh
```

If you choose the second option, it will be easier to keep updated and you could always change the theme by just changing the config folder. But for that to work you'll need to put the polybar-collection folder in this directory:

```bash
$HOME/Projects/fun
```

To create the directory and download the polybar-collection:

```bash
mkdir -p $HOME/Projects/fun && cd $HOME/Projects/fun && git clone https://github.com/Murzchnvok/polybar-collection.git
```

## Something you might be interested

* [Rofi Collection](https://github.com/Murzchnvok/rofi-collection)
* [Wallpaper Collection](https://drive.google.com/drive/folders/1o1qjRgkJtnF_8uGB1z6MRsQUjWinHUsw?usp=sharing)
* [Pomotroid (pomodoro app)](https://github.com/Splode/pomotroid)
* [Taskbook (task and notes command line)](https://github.com/klaussinani/taskbook)

*Quality is more important then quantity!*

## Dracula

![desktop](screenshots/dracula/desktop.png)

![rofi](screenshots/dracula/rofi.png)

![some apps](screenshots/dracula/pomotroid.png)

## Material

![desktop](screenshots/material/desktop.png)

![rofi](screenshots/material/rofi.png)

![some apps](screenshots/material/some-apps.png)

## Neon

![desktop](screenshots/neon/desktop.png)

![rofi](screenshots/neon/rofi.png)

![pomotroid](screenshots/neon/some-apps.png)

## Nord

![desktop](screenshots/nord/desktop.png)

![rofi](screenshots/nord/rofi.png)

![pomotroid](screenshots/nord/pomotroid.png)
