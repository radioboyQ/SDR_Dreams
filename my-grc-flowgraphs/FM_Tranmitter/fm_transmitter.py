#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Transmitter
# Author: Scott Fraser
# Generated: Fri Jun 23 17:58:10 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class fm_transmitter(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "FM Transmitter")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100
        self.channel_two = channel_two = 102.1e6
        self.channel_one_freq = channel_one_freq = 103e6
        self.center_freq = center_freq = 102.1e6

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=44100,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_1 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf=0' )
        self.osmosdr_sink_1.set_sample_rate(2e6)
        self.osmosdr_sink_1.set_center_freq(center_freq, 0)
        self.osmosdr_sink_1.set_freq_corr(0, 0)
        self.osmosdr_sink_1.set_gain(0, 0)
        self.osmosdr_sink_1.set_if_gain(0, 0)
        self.osmosdr_sink_1.set_bb_gain(0, 0)
        self.osmosdr_sink_1.set_antenna('', 0)
        self.osmosdr_sink_1.set_bandwidth(0, 0)
          
        self.blocks_wavfile_source_1 = blocks.wavfile_source('/home/radioboy/Claves.wav', True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((1, ))
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=32000,
        	quad_rate=320000,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.osmosdr_sink_1, 0))    
        self.connect((self.blocks_wavfile_source_1, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_1, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_channel_two(self):
        return self.channel_two

    def set_channel_two(self, channel_two):
        self.channel_two = channel_two

    def get_channel_one_freq(self):
        return self.channel_one_freq

    def set_channel_one_freq(self, channel_one_freq):
        self.channel_one_freq = channel_one_freq

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_1.set_center_freq(self.center_freq, 0)


def main(top_block_cls=fm_transmitter, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
