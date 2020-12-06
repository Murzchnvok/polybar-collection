# Polybar Collection

My personal collection. (I'll update soon to the new version of polybar)

_If you find any error or you have an idea of a theme or something, send a message to me on [reddit](https://www.reddit.com/user/murzchnvok) or on Discord_ **Murzchnvok#1166**

## Getting Started

### Prerequisites

You need to install Polybar and FontAwesome:

[Compiling Polybar](https://github.com/polybar/polybar/wiki/Compiling)

Debian/Ubuntu

```bash
$HOME
-> sudo apt install fonts-font-awesome
```

Fedora

```bash
$HOME
-> sudo dnf install fontawesome-fonts
```

Also you need to download and install these fonts from [nerd fonts](https://www.nerdfonts.com/font-downloads):

- JetBrainsMono
- Iosevka
- UbuntuMono

To install this font, copy/move to the folder _~/.fonts_ and run in the terminal:

```bash
$HOME
-> fc-cache -fv
```

### Cloning

First you need to clone the repo in the \$HOME directory:

```bash
$HOME
-> git clone https://github.com/Murzchnvok/polybar-collection
```

or clone to other directory and create a symlink of the folder in the \$HOME directory:

```bash
$HOME/Projects
-> git clone https://github.com/Murzchnvok/polybar-collection

$HOME
-> ln -s $HOME/Projects/polybar-collection $HOME/polybar-collection
```

Other option is to copy a config folder to _\$HOME/.config/polybar/_ directory:

```bash
$HOME
-> cp -r material $HOME/.config/polybar
```

or create a symlink of the folder in the _\$HOME/.config/polybar/_ directory:

```bash
$HOME
-> ln -s $HOME/Projects/polybar-collection/nord $HOME/.config/polybar/
```

### Running

BSPwm

```bash
$HOME/polybar-collection/launch.sh
```

I3wm

```bash
exec_always --no-startup-id $HOME/polybar-collection/launch.sh
```

Remember to keep updated:

```bash
$HOME
-> cd $HOME/polybar-collection && git pull
```

## You might be interested

- [Rofi Collection](https://github.com/Murzchnvok/rofi-collection)
- [Wallpaper Collection](https://drive.google.com/drive/folders/1o1qjRgkJtnF_8uGB1z6MRsQUjWinHUsw?usp=sharing)
- [Pomotroid (pomodoro app)](https://github.com/Splode/pomotroid)
- [Taskbook (task and notes command line)](https://github.com/klaussinani/taskbook)

_Quality is more important then quantity!_

## Dracula

![desktop](screenshots/dracula/desktop.png)

![rofi](screenshots/dracula/rofi.png)

![some apps](screenshots/dracula/pomotroid.png)

## Material

![desktop](screenshots/material/desktop.png)

![rofi](screenshots/material/rofi.png)

![some apps](screenshots/material/some-apps.png)

## Minimal

![desktop](screenshots/minimal/desktop.png)

![rofi](screenshots/minimal/rofi.png)

![some apps](screenshots/minimal/pomotroid.png)

## Neon

![desktop](screenshots/neon/desktop.png)

![rofi](screenshots/neon/rofi.png)

![pomotroid](screenshots/neon/some-apps.png)

## Nord

![desktop](screenshots/nord/desktop.png)

![rofi](screenshots/nord/rofi.png)

![pomotroid](screenshots/nord/pomotroid.png)
