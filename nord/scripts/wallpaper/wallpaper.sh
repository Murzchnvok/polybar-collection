#!/bin/sh

GIF_SLEEP_TIME=0.1

TIME_NOW=$(date +%H)
DAY=6
NIGHT=18

WALLPAPERS_PATH=$HOME/Pictures/Wallpapers
GIF_PATH=$WALLPAPERS_PATH/gifs-frames

DAY_WALL=$WALLPAPERS_PATH/nord-water.png
NIGHT_WALL=$WALLPAPERS_PATH/nord-water.png

preset() {
  if [ $TIME_NOW -ge $NIGHT -o $TIME_NOW -lt $DAY ]; then
    feh --bg-fill $NIGHT_WALL
  else
    feh --bg-fill $DAY_WALL
  fi
}

random() {
  feh --bg-fill --randomize $WALLPAPERS_PATH/*
}

presetgif() {
  while :; do
    for image in $GIF_PATH/rainy-day/*; do
      feh --bg-fill $image
      sleep $GIF_SLEEP_TIME
    done
  done
}

randomgif() {
  cdir=$(ls $GIF_PATH | wc -l)
  rnum=$(shuf -i 1-$cdir -n 1)
  rdir=$(ls $GIF_PATH | sed -n $rnum"p")
  while :; do
    for image in $GIF_PATH/$rdir/*; do
      feh --bg-fill $image
      sleep $GIF_SLEEP_TIME
    done
  done
}

auto() {
  while :; do
    $arg1
    sleep $arg3
  done
}

verify() {
  if [ "$arg2" = "auto" ]; then
    auto
  elif [ "$arg2" = "" ]; then
    echo
  else
    usage
    exit 1
  fi
}

case $1 in
preset)
  verify
  preset
  ;;
random)
  verify
  random
  ;;
presetgif)
  presetgif
  ;;
randomgif)
  randomgif
  ;;
esac
