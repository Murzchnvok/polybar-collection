#!/bin/sh

pkill wallpaper.sh

clickLeft() {
  $(dirname $0)/wallpaper.sh preset
}

clickMiddle() {
  pkill wallpaper.sh
}

clickRight() {
  $(dirname $0)/wallpaper.sh random
}

clickDoubleLeft() {
  $(dirname $0)/wallpaper.sh preset auto
}

clickDoubleRight() {
  $(dirname $0)/wallpaper.sh random auto 5m
}

scrollUp() {
  $(dirname $0)/wallpaper.sh bingdaily
}

scrollDown() {
  $(dirname $0)/wallpaper.sh randomgif &
}

case $1 in
clickleft)
  clickLeft
  ;;
clickmiddle)
  clickMiddle
  ;;
clickright)
  clickRight
  ;;
clickdoubleleft)
  clickDoubleLeft
  ;;
clickdoubleright)
  clickDoubleRight
  ;;
scrollup)
  scrollUp
  ;;
scrolldown)
  scrollDown
  ;;
esac
