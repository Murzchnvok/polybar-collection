# Polybar Collection

My personal collection.

## Getting Started

### Prerequisites

You need to install Polybar, NerdFonts and MaterialIcons:

[Compiling Polybar](https://github.com/polybar/polybar/wiki/Compiling)

You need to download and install these fonts from [NerdFonts](https://www.nerdfonts.com/font-downloads):

- JetBrainsMono
- Iosevka

Also you'll need to install [MaterialIcons](https://github.com/google/material-design-icons).

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
- [Ugly To-Do](https://github.com/Murzchnvok/ugly-todo)

_Quality is more important then quantity!_

## Murz

![desktop](screenshots/murz/desktop.png)

![rofi](screenshots/murz/rofi.png)

![some apps](screenshots/murz/some-apps.png)

## Chnvok (same as Murz, but with a different style)

![desktop](screenshots/chnvok/desktop.png)

## Dracula

![desktop](screenshots/dracula/desktop.png)

![rofi](screenshots/dracula/rofi.png)

![some apps](screenshots/dracula/some-apps.png)

## Gruvbox

![desktop](screenshots/gruvbox/desktop.png)

![rofi](screenshots/gruvbox/rofi.png)

![some apps](screenshots/gruvbox/some-apps.png)

## Material

![desktop](screenshots/material/desktop.png)

![rofi](screenshots/material/rofi.png)

![some apps](screenshots/material/some-apps.png)

## Minimal

![desktop](screenshots/minimal/desktop.png)

![rofi](screenshots/minimal/rofi.png)

![some apps](screenshots/minimal/some-apps.png)

## Nord

![desktop](screenshots/nord/desktop.png)

![rofi](screenshots/nord/rofi.png)

![pomotroid](screenshots/nord/some-apps.png)
