#!/usr/bin/env bash

# Terminate already running bar instances
killall polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
polybar main -c $(dirname $0)/config.ini &
