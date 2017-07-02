#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Transmitter; Try 2
# Description: Second try at a FM transmitter
# Generated: Fri Jun 23 18:22:17 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM Transmitter; Try 2")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.channel_two = channel_two = 434e6
        self.channel_one = channel_one = 432e6
        self.center_freq = center_freq = 433e6

        ##################################################
        # Blocks
        ##################################################
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label='Center Frequency',
        	converter=forms.float_converter(),
        )
        self.Add(self._center_freq_text_box)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self._channel_two_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.channel_two,
        	callback=self.set_channel_two,
        	label='Channel Two Frequency',
        	converter=forms.float_converter(),
        )
        self.Add(self._channel_two_text_box)
        self._channel_one_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.channel_one,
        	callback=self.set_channel_one,
        	label='Channel One Frequency',
        	converter=forms.float_converter(),
        )
        self.Add(self._channel_one_text_box)
        self.blocks_wavfile_source_1 = blocks.wavfile_source('/home/radioboy/sdr/Claves.wav', True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=320000,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_wavfile_source_1, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_channel_two(self):
        return self.channel_two

    def set_channel_two(self, channel_two):
        self.channel_two = channel_two
        self._channel_two_text_box.set_value(self.channel_two)

    def get_channel_one(self):
        return self.channel_one

    def set_channel_one(self, channel_one):
        self.channel_one = channel_one
        self._channel_one_text_box.set_value(self.channel_one)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_text_box.set_value(self.center_freq)
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
