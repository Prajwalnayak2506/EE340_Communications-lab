#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Part2a
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
import sip



class Part2a(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Part2a", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Part2a")
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

        self.settings = Qt.QSettings("GNU Radio", "Part2a")

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
        self.samp_rate = samp_rate = sps*symb_rate
        self.offset = offset = 0
        self.object0 = object0 = digital.constellation_calcdist([-1-1j, -1+1j, 1+1j, 1-1j], [0, 1, 3, 2],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.object0.set_npwr(1.0)
        self.interpolate = interpolate = 20
        self.carr_freq = carr_freq = 500000

        ##################################################
        # Blocks
        ##################################################

        self._offset_range = qtgui.Range(0, 10, 0.1, 0, 200)
        self._offset_win = qtgui.RangeWidget(self._offset_range, self.set_offset, "'offset'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._offset_win)
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                symb_rate,
                1,
                (11*8)))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                symb_rate,
                1,
                (11*sps)))
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=interpolate,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=interpolate,
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
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                (samp_rate*interpolate),
                samp_rate,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(8, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(object0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j,-1+1j,1+1j,1-1j], 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_1_0 = blocks.threshold_ff((-0.25), 0.25, 0)
        self.blocks_threshold_ff_0_1 = blocks.threshold_ff((-0.25), 0.25, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 48)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(2)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(2)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'out2.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 4)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_cc(-1-1j)
        self.analog_sig_source_x_0_1 = analog.sig_source_f((samp_rate*interpolate), analog.GR_SIN_WAVE, (carr_freq+offset), 1, 0, 3.14)
        self.analog_sig_source_x_0_0 = analog.sig_source_f((samp_rate*interpolate), analog.GR_COS_WAVE, (carr_freq+offset), 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c((samp_rate*interpolate), analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_threshold_ff_0_1, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_threshold_ff_0_1_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_threshold_ff_0_1, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.blocks_threshold_ff_0_1_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.blocks_delay_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Part2a")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.sps*self.symb_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symb_rate, 1, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symb_rate, 1, (11*8)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_samp_rate(self.sps*self.symb_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symb_rate, 1, (11*self.sps)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq((self.samp_rate*self.interpolate))
        self.analog_sig_source_x_0_0.set_sampling_freq((self.samp_rate*self.interpolate))
        self.analog_sig_source_x_0_1.set_sampling_freq((self.samp_rate*self.interpolate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*self.interpolate), self.samp_rate, 1000, window.WIN_HAMMING, 6.76))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symb_rate, 1, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symb_rate, 1, (11*8)))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0_0.set_frequency((self.carr_freq+self.offset))
        self.analog_sig_source_x_0_1.set_frequency((self.carr_freq+self.offset))

    def get_object0(self):
        return self.object0

    def set_object0(self, object0):
        self.object0 = object0
        self.digital_constellation_decoder_cb_0.set_constellation(self.object0)

    def get_interpolate(self):
        return self.interpolate

    def set_interpolate(self, interpolate):
        self.interpolate = interpolate
        self.analog_sig_source_x_0.set_sampling_freq((self.samp_rate*self.interpolate))
        self.analog_sig_source_x_0_0.set_sampling_freq((self.samp_rate*self.interpolate))
        self.analog_sig_source_x_0_1.set_sampling_freq((self.samp_rate*self.interpolate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*self.interpolate), self.samp_rate, 1000, window.WIN_HAMMING, 6.76))

    def get_carr_freq(self):
        return self.carr_freq

    def set_carr_freq(self, carr_freq):
        self.carr_freq = carr_freq
        self.analog_sig_source_x_0_0.set_frequency((self.carr_freq+self.offset))
        self.analog_sig_source_x_0_1.set_frequency((self.carr_freq+self.offset))




def main(top_block_cls=Part2a, options=None):

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