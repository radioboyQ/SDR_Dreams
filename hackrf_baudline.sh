#!/bin/bash
# ./hackrf_baudline.sh <frequency> <samplerate> <ifgain> <bbgain>

# Pipe HackRF output to Baudline
hackrf_transfer -r - -f ${1} -s ${2} -l ${3} -g ${4} | ~/sdr/baudline_1.08_linux_x86_64/baudline -reset -basefrequency ${1} -samplerate ${2} -channels 2 -format s8 -quadrature -flipcomplex -stdin
