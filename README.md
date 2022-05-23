# Polybar Collection

My personal collection. Trying to make some nice themes, and show how great [Polybar](https://github.com/polybar/polybar) is. I'll keep updating the collection, and maybe create some custom scripts so you and I can have a better experience with this thing. I also recommend you to check this [adi1090x Polybar Collection](https://github.com/adi1090x/polybar-themes), has some great themes, so if you don't like my collection, you can just check the other one. Also the reason why I'm doing this is because I want you to have more options and ideas to build your own theme.

Read this README with attention.

## Getting Started

### Prerequisites

First of all, install Polybar:

[Compiling Polybar](https://github.com/polybar/polybar/wiki/Compiling)

By default the font used is `JetBrainsMono` (you can change it in the **fonts.ini** file), you can download and install from [NerdFonts](https://www.nerdfonts.com/font-downloads):

Also you'll need [MaterialIcons](https://github.com/google/material-design-icons) and [Feather](https://feathericons.com/).
You can move both **MaterialIcons** and **feather** inside **fonts** to **$HOME/.fonts/** and run:

```bash
$HOME
-> fc-cache -fv
```

or just search how to install fonts!

### Cloning

Now you need to clone the repo in the \$HOME directory (because the path inside the files points to **$HOME/polybar-collection**):

```bash
$HOME
-> git clone --depth 1 https://github.com/Murzchnvok/polybar-collection
```

or clone to other directory and create a symlink of the folder in the \$HOME directory:

```bash
$HOME/Projects
-> git clone --depth 1 https://github.com/Murzchnvok/polybar-collection

$HOME
-> ln -s $HOME/Projects/polybar-collection $HOME/polybar-collection
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

## Few changes

Now we only have one file **modules.ini** to change the modules that we like to use. I believe that's a better way to configure our Polybar themes:

```ini
modules-left = date wallz nft tor weather bspwm i3
modules-center = mpd
modules-right = wired cpu memory xbacklight pulseaudio
```

The only problem with this, is that some themes don't have certain modules, for now at least! I'm planning on making this collection easier to setup, so if you have any ideas you can always share.

## Weather app

As pointed out by Dennis Perrone, my personal OpenWeather API Key is in the project as a constant, and I did this intentionally so it just works, and it's fine if you want to use it the same as me, but I'll suggest you to create your own API Key for free in the official [OpenWeather](https://openweathermap.org/api) website. There's a limit of requests you can make using the same API Key, so we both could be without the weather info if a lot of requests are made.

After you create your API Key, you can pass as an argument in the **weather.sh** script, or you can set an environment variable for **OPENWEATHER_API_KEY** with your own API Key:

## Wallz

Still thinking about this one, maybe I should add more 'backend' options, for now is only using Bing API, but I could add more options since Bing API have a 'limited', but with a really good quality, wallpapers collection. For now I'll be only using on minimal theme, but when I'm 'done' I'll add to the others.

## You might be interested

- [Rofi Collection](https://github.com/Murzchnvok/rofi-collection)
- [Wallpaper Collection](https://drive.google.com/drive/folders/1o1qjRgkJtnF_8uGB1z6MRsQUjWinHUsw?usp=sharing)
- [Pomotroid (pomodoro app)](https://github.com/Splode/pomotroid)
- [Ugly To-Do](https://github.com/Murzchnvok/ugly-todo)

_Enjoy!_

### Murz

![desktop](screenshots/murz/desktop.png)

```ini
modules-left = date weather round-right
modules-center = round-left bspwm round-right
modules-right = round-left mpd
```

### Chnvok

![desktop](screenshots/chnvok/desktop.png)

```ini
modules-left = date weather mpd
modules-center = bspwm
modules-right = memory cpu xbacklight pulseaudio session
```

### Dracula

![desktop](screenshots/dracula/desktop.png)

```ini
modules-left = date margin weather margin mpd
modules-center = bspwm
modules-right = memory margin cpu margin xbacklight margin pulseaudio margin battery margin session
```

### Gruvbox

![desktop](screenshots/gruvbox/desktop.png)

```ini
modules-left = bspwm
modules-center = round-left-blue weather date round-right-blue margin round-left mpd round-right
modules-right = cpu memory pulseaudio xbacklight
```

### Lofi

![desktop](screenshots/lofi/desktop.png)

```ini
modules-left = bspwm
modules-center = mpd
modules-right = date weather
```

### Material

![desktop](screenshots/material/desktop.png)

```ini
modules-left = weather margin date margin mpd tri-upper-right tri-lower-left bspwm tri-upper-right
modules-center = 
modules-right = memory margin cpu margin xbacklight margin pulseaudio
```

### Minimal

![desktop](screenshots/minimal/desktop.png)

```ini
modules-left = date weather bspwm
modules-center = mpd
modules-right = cpu memory xbacklight pulseaudio
```

### Nord

![desktop](screenshots/nord/desktop.png)

```ini
modules-left = date margin weather margin mpd round-right
modules-center = trap-left bspwm trap-right
modules-right = memory margin cpu margin xbacklight margin pulseaudio margin wallz margin session
```

### One Dark

![desktop](screenshots/onedark/desktop.png)

```ini
modules-left = bspwm margin date margin weather margin mpd
modules-center =
modules-right = cpu margin memory margin pulseaudio margin xbacklight margin wallz margin session
```
