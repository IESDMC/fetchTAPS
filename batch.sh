#!/bin/bash

x=1
while [ $x -le 23 ]
do
  python fetchWaveform.py -u chute@earth.sinica.edu.tw -p 27839910#2705 -format mseed -tb 2008-02-17T20:31:00 -te 2008-02-20T20:41:00 -proj 2008NSS,2008NSN -net TW -sta all -loc all -cha HHZ -label $x
  x=$(( $x + 1 ))
done

y=1
while [ $y -le 10 ]
do
  python fetchWaveform.py -u chute@earth.sinica.edu.tw -p 27839910#2705 -format mseed -tb 2008-02-17T20:31:00 -te 2008-02-17T20:41:00 -proj 2008NSS,2008NSN -net TW -sta all -loc all -cha HHZ -label small$y
  python fetchWaveform.py -u chute@earth.sinica.edu.tw -p 27839910#2705 -format mseed -tb 2008-02-17T20:31:00 -te 2008-02-20T20:41:00 -proj 2008NSS,2008NSN -net TW -sta all -loc all -cha HHZ -label large$y
  y=$(( $y + 1 ))
done

