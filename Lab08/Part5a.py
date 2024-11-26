#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Part5a
# Author: Harsh S Roniyar
# Copyright: HSR
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from math import pi
import sip



class Part5a(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Part5a", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Part5a")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Part5a")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symb_rate = symb_rate = 50000
        self.sps = sps = 8
        self.t_alpha_range = t_alpha_range = 0.8
        self.samp_rate = samp_rate = sps*symb_rate
        self.ip_factor = ip_factor = 20
        self.eight_psk = eight_psk = [(1+2e-16j) ,(0.7071067811865476+0.7071067811865475j) ,(6.123233995736766e-17+1j) ,(-0.7071067811865475+0.7071067811865476j) ,(-1+1.2246467991473532e-16j) ,(-0.7071067811865477-0.7071067811865475j) ,(-1.8369701987210297e-16-1j) ,(0.7071067811865474-0.7071067811865477j) ]
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist(eight_psk, [0, 1 ,2 ,3 ,4 ,5 ,6 , 7],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation_0.set_npwr(1.0)
        self.t_alpha = t_alpha = t_alpha_range
        self.samp_rate_iq = samp_rate_iq = samp_rate*ip_factor
        self.r_alpha = r_alpha = 0.8
        self.ntaps = ntaps = 11*sps
        self.noise_amp = noise_amp = 0.1
        self.gain = gain = 3
        self.freq_offset = freq_offset = 10
        self.delay_slider = delay_slider = 0
        self.Qpsk = Qpsk = [-1-1j, -1+1j, 1+1j, 1-1j]

        ##################################################
        # Blocks
        ##################################################

        self._noise_amp_range = qtgui.Range(0, 5, 0.1, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "'noise_amp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self._freq_offset_range = qtgui.Range(0, 100, 1, 10, 200)
        self._freq_offset_win = qtgui.RangeWidget(self._freq_offset_range, self.set_freq_offset, "'freq_offset'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self._t_alpha_range_range = qtgui.Range(0, 1, 0.05, 0.8, 200)
        self._t_alpha_range_win = qtgui.RangeWidget(self._t_alpha_range_range, self.set_t_alpha_range, "'t_alpha_range'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._t_alpha_range_win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=ip_factor,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccf(
                interpolation=1,
                decimation=1,
                taps=firdes.root_raised_cosine(gain,samp_rate,symb_rate,r_alpha,ntaps),
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccf(
                interpolation=1,
                decimation=1,
                taps=firdes.root_raised_cosine(gain,samp_rate,symb_rate,t_alpha,ntaps),
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=ip_factor,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate_iq,
                40000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate_iq,
                40000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccf(sps, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(eight_psk, 1)
        self._delay_slider_range = qtgui.Range(0, 7, 1, 0, 200)
        self._delay_slider_win = qtgui.RangeWidget(self._delay_slider_range, self.set_delay_slider, "'delay_slider'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_slider_win)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(3)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff((-1))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'Original_Text.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate_iq, analog.GR_COS_WAVE, (500000+freq_offset), 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate_iq, analog.GR_SIN_WAVE, (500000+freq_offset), 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate_iq, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.rational_resampler_xxx_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Part5a")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.sps*self.symb_rate)
        self.rational_resampler_xxx_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.t_alpha,self.ntaps))
        self.rational_resampler_xxx_0_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.r_alpha,self.ntaps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.sps)
        self.set_samp_rate(self.sps*self.symb_rate)

    def get_t_alpha_range(self):
        return self.t_alpha_range

    def set_t_alpha_range(self, t_alpha_range):
        self.t_alpha_range = t_alpha_range
        self.set_t_alpha(self.t_alpha_range)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_iq(self.samp_rate*self.ip_factor)
        self.rational_resampler_xxx_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.t_alpha,self.ntaps))
        self.rational_resampler_xxx_0_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.r_alpha,self.ntaps))

    def get_ip_factor(self):
        return self.ip_factor

    def set_ip_factor(self, ip_factor):
        self.ip_factor = ip_factor
        self.set_samp_rate_iq(self.samp_rate*self.ip_factor)

    def get_eight_psk(self):
        return self.eight_psk

    def set_eight_psk(self, eight_psk):
        self.eight_psk = eight_psk
        self.digital_chunks_to_symbols_xx_0.set_symbol_table(self.eight_psk)

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_t_alpha(self):
        return self.t_alpha

    def set_t_alpha(self, t_alpha):
        self.t_alpha = t_alpha
        self.rational_resampler_xxx_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.t_alpha,self.ntaps))

    def get_samp_rate_iq(self):
        return self.samp_rate_iq

    def set_samp_rate_iq(self, samp_rate_iq):
        self.samp_rate_iq = samp_rate_iq
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate_iq)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate_iq)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate_iq)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_iq, 40000, 10000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate_iq, 40000, 10000, window.WIN_HAMMING, 6.76))

    def get_r_alpha(self):
        return self.r_alpha

    def set_r_alpha(self, r_alpha):
        self.r_alpha = r_alpha
        self.rational_resampler_xxx_0_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.r_alpha,self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.rational_resampler_xxx_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.t_alpha,self.ntaps))
        self.rational_resampler_xxx_0_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.r_alpha,self.ntaps))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.rational_resampler_xxx_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.t_alpha,self.ntaps))
        self.rational_resampler_xxx_0_0_0.set_taps(firdes.root_raised_cosine(self.gain,self.samp_rate,self.symb_rate,self.r_alpha,self.ntaps))

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.analog_sig_source_x_0_0_0.set_frequency((500000+self.freq_offset))
        self.analog_sig_source_x_0_1.set_frequency((500000+self.freq_offset))

    def get_delay_slider(self):
        return self.delay_slider

    def set_delay_slider(self, delay_slider):
        self.delay_slider = delay_slider

    def get_Qpsk(self):
        return self.Qpsk

    def set_Qpsk(self, Qpsk):
        self.Qpsk = Qpsk




def main(top_block_cls=Part5a, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
