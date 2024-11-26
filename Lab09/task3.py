#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
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
from gnuradio.filter import pfb
import sip



class task3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "task3")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.symb_rate = symb_rate = 50000
        self.ntaps = ntaps = 11*sps
        self.gain = gain = 3
        self.f_off = f_off = 1
        self.excess_bw = excess_bw = 1

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_tab_widget = Qt.QTabWidget()
        self.qtgui_tab_widget_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_0)
        self.qtgui_tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_0.addLayout(self.qtgui_tab_widget_grid_layout_0)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_0, 'Symbols')
        self.qtgui_tab_widget_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_1)
        self.qtgui_tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_1.addLayout(self.qtgui_tab_widget_grid_layout_1)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_1, 'RRC_output')
        self.qtgui_tab_widget_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_2)
        self.qtgui_tab_widget_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_2.addLayout(self.qtgui_tab_widget_grid_layout_2)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_2, 'Modulated_signal_with noise')
        self.qtgui_tab_widget_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_3)
        self.qtgui_tab_widget_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_3.addLayout(self.qtgui_tab_widget_grid_layout_3)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_3, 'Demodulated_signal_with f_off')
        self.qtgui_tab_widget_widget_4 = Qt.QWidget()
        self.qtgui_tab_widget_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_4)
        self.qtgui_tab_widget_grid_layout_4 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_4.addLayout(self.qtgui_tab_widget_grid_layout_4)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_4, 'Match_filter_output')
        self.qtgui_tab_widget_widget_5 = Qt.QWidget()
        self.qtgui_tab_widget_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_5)
        self.qtgui_tab_widget_grid_layout_5 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_5.addLayout(self.qtgui_tab_widget_grid_layout_5)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_5, 'costas_output')
        self.top_layout.addWidget(self.qtgui_tab_widget)
        self._f_off_range = qtgui.Range(0, 100, 1, 1, 200)
        self._f_off_win = qtgui.RangeWidget(self._f_off_range, self.set_f_off, "f_off", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_off_win)
        self._excess_bw_range = qtgui.Range(0, 10, 1, 1, 200)
        self._excess_bw_win = qtgui.RangeWidget(self._excess_bw_range, self.set_excess_bw, "excess_bw", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._excess_bw_win)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccf(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_sink_x_0_1_0_1 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            50000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0_1.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_5.addWidget(self._qtgui_sink_x_0_1_0_1_win)
        self.qtgui_sink_x_0_1_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            400000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0_0.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_3.addWidget(self._qtgui_sink_x_0_1_0_0_win)
        self.qtgui_sink_x_0_1_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            50000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_4.addWidget(self._qtgui_sink_x_0_1_0_win)
        self.qtgui_sink_x_0_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            8000000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_2.addWidget(self._qtgui_sink_x_0_1_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            400000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_1.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            50000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.qtgui_tab_widget_layout_0.addWidget(self._qtgui_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=firdes.root_raised_cosine(gain, sps * symb_rate, symb_rate, excess_bw, ntaps)
        ,
            flt_size=32,
            atten=100)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                8000000,
                200000,
                20000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                8000000,
                200000,
                20000,
                window.WIN_HAMMING,
                6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.0628, firdes.root_raised_cosine(gain,32*sps*symb_rate,symb_rate,excess_bw,ntaps), 32, 16, 1.5, 1)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(0.0628, 4, False)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j, -1+1j, +1-1j, 1+1j], 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_skiphead_0_0_1 = blocks.skiphead(gr.sizeof_char*1, 2)
        self.blocks_pack_k_bits_bb_0_0_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(2)
        self.blocks_or_xx_0 = blocks.or_bb()
        self.blocks_multiply_xx_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/priyansh/Desktop/EE340/Lab9/Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/priyansh/Desktop/EE340/Lab9/output_3.txt', False)
        self.blocks_file_sink_0_0_1.set_unbuffered(False)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(8000000, analog.GR_SIN_WAVE, (500000 + f_off), 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(8000000, analog.GR_COS_WAVE, (500000 + f_off), 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(8000000, analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(8000000, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_multiply_xx_0_1_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.qtgui_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_or_xx_0, 1))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.blocks_or_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_or_xx_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_1, 0), (self.blocks_file_sink_0_0_1, 0))
        self.connect((self.blocks_skiphead_0_0_1, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_sink_x_0_1_0_1, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_skiphead_0_0_1, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_sink_x_0_1_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_float_to_complex_1, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.sps)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,32*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain, self.sps * self.symb_rate, self.symb_rate, self.excess_bw, self.ntaps)
        )
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,32*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain, self.sps * self.symb_rate, self.symb_rate, self.excess_bw, self.ntaps)
        )

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,32*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain, self.sps * self.symb_rate, self.symb_rate, self.excess_bw, self.ntaps)
        )

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,32*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain, self.sps * self.symb_rate, self.symb_rate, self.excess_bw, self.ntaps)
        )

    def get_f_off(self):
        return self.f_off

    def set_f_off(self, f_off):
        self.f_off = f_off
        self.analog_sig_source_x_0_1.set_frequency((500000 + self.f_off))
        self.analog_sig_source_x_0_1_0.set_frequency((500000 + self.f_off))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,32*self.sps*self.symb_rate,self.symb_rate,self.excess_bw,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain, self.sps * self.symb_rate, self.symb_rate, self.excess_bw, self.ntaps)
        )




def main(top_block_cls=task3, options=None):

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
