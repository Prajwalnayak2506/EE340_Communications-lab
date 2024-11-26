#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Part4
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
from gnuradio import zeromq
import sip



class Part4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Part4", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Part4")
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

        self.settings = Qt.QSettings("GNU Radio", "Part4")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([0-0j, 0+1j, 1+1j, 1-0j], [0, 1, 2, 3],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation_0.set_npwr(1.0)
        self.symbol_rate = symbol_rate = 50000
        self.sps = sps = 8
        self.skip_head = skip_head = 3
        self.samp_rate = samp_rate = 8000000
        self.off = off = 2
        self.alpha = alpha = 0.9

        ##################################################
        # Blocks
        ##################################################

        self._off_range = qtgui.Range(0, 10, 0.1, 2, 200)
        self._off_win = qtgui.RangeWidget(self._off_range, self.set_off, "off", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._off_win)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float, 1, 'tcp://127.0.0.1:50001', 100, False, (-1), True)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://127.0.0.1:50001', 100, False, (-1), False)
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                50000,
                1,
                (11*sps)))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                50000,
                1,
                (11*sps)))
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccf(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd([0.01], [1,0.99], True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([1.0001,-1], [1,1], True)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(sps, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j, -1+1j, 1+1j, 1-1j], 1)
        self.blocks_vco_c_0 = blocks.vco_c(50000, (-5), 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_1 = blocks.threshold_ff((-0.0000001), 0, 0)
        self.blocks_threshold_ff_0_0_0 = blocks.threshold_ff((-0.0000001), 0, 0)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 11)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(2)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1.414)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1.414)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, 'Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'out4.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 100)
        self.blocks_complex_to_float_0_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff((-0.5))
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-0.5))
        self.analog_sig_source_x_0_0_1_0 = analog.sig_source_f((8000000 + off), analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_f(8000000, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f((8000000 + off), analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(8000000, analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)
        self._alpha_range = qtgui.Range(0, 1, 0.1, 0.9, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_1_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_0_1_0, 0))
        self.connect((self.analog_sig_source_x_0_0_1_0, 0), (self.blocks_multiply_xx_0_1_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_1_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_1_0_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_threshold_ff_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_threshold_ff_0_1, 0))
        self.connect((self.blocks_complex_to_float_0_0_0, 1), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_complex_to_float_0_0_0, 0), (self.blocks_multiply_xx_0_1_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_1_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0_1_0_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.iir_filter_xxx_0_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_0_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.blocks_threshold_ff_0_1, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_complex_to_float_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_multiply_const_vxx_3, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Part4")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0
        self.digital_constellation_decoder_cb_0.set_constellation(self.variable_constellation_0)

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), 50000, 1, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), 50000, 1, (11*self.sps)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), 50000, 1, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), 50000, 1, (11*self.sps)))

    def get_skip_head(self):
        return self.skip_head

    def set_skip_head(self, skip_head):
        self.skip_head = skip_head

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)

    def get_off(self):
        return self.off

    def set_off(self, off):
        self.off = off
        self.analog_sig_source_x_0_0_0.set_sampling_freq((8000000 + self.off))
        self.analog_sig_source_x_0_0_1_0.set_sampling_freq((8000000 + self.off))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha




def main(top_block_cls=Part4, options=None):

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
