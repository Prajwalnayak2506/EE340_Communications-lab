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
import numpy
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



class TASK1_abcd(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "TASK1_abcd")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 10000
        self.sps = sps = 8
        self.noise_amp = noise_amp = 0.1
        self.demod_delay = demod_delay = 11
        self.b4 = b4 = 0.0625
        self.b3 = b3 = -0.125
        self.b2 = b2 = 0.25
        self.b1 = b1 = -0.5
        self.alpha = alpha = 2.5

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_tab_widget_1 = Qt.QTabWidget()
        self.qtgui_tab_widget_1_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_0)
        self.qtgui_tab_widget_1_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_0.addLayout(self.qtgui_tab_widget_1_grid_layout_0)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_0, 'Chunks to symbols output - time')
        self.qtgui_tab_widget_1_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_1)
        self.qtgui_tab_widget_1_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_1.addLayout(self.qtgui_tab_widget_1_grid_layout_1)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_1, 'Chunks to symbols output - constellation')
        self.qtgui_tab_widget_1_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_2)
        self.qtgui_tab_widget_1_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_2.addLayout(self.qtgui_tab_widget_1_grid_layout_2)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_2, 'RRC_output_constellation')
        self.qtgui_tab_widget_1_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_3)
        self.qtgui_tab_widget_1_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_3.addLayout(self.qtgui_tab_widget_1_grid_layout_3)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_3, 'equalizer_output - constellation')
        self.qtgui_tab_widget_1_widget_4 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_4)
        self.qtgui_tab_widget_1_grid_layout_4 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_4.addLayout(self.qtgui_tab_widget_1_grid_layout_4)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_4, 'match_filter_output_constellation')
        self.qtgui_tab_widget_1_widget_5 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_5)
        self.qtgui_tab_widget_1_grid_layout_5 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_5.addLayout(self.qtgui_tab_widget_1_grid_layout_5)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_5, 'error')
        self.top_layout.addWidget(self.qtgui_tab_widget_1)
        self._noise_amp_range = qtgui.Range(0, 1, 0.1, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "noise_amp", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self._demod_delay_range = qtgui.Range(0, 100, 1, 11, 200)
        self._demod_delay_win = qtgui.RangeWidget(self._demod_delay_range, self.set_demod_delay, "'demod_delay'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._demod_delay_win)
        self._b4_range = qtgui.Range(-1, 1, 0.1, 0.0625, 200)
        self._b4_win = qtgui.RangeWidget(self._b4_range, self.set_b4, "b4", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b4_win)
        self._b3_range = qtgui.Range(-1, 1, 0.1, -0.125, 200)
        self._b3_win = qtgui.RangeWidget(self._b3_range, self.set_b3, "b3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b3_win)
        self._b2_range = qtgui.Range(-1, 1, 0.1, 0.25, 200)
        self._b2_win = qtgui.RangeWidget(self._b2_range, self.set_b2, "b2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b2_win)
        self._b1_range = qtgui.Range(-1, 1, 0.1, -0.5, 200)
        self._b1_win = qtgui.RangeWidget(self._b1_range, self.set_b1, "b1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b1_win)
        self._alpha_range = qtgui.Range(0, 3, 0.1, 2.5, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "alpha", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.rational_resampler_xxx_1_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=5,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            10000, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_layout_5.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(True)


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


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_layout_3.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_layout_4.addWidget(self._qtgui_const_sink_x_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_layout_1.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-1), 1)
        self.qtgui_const_sink_x_0.set_x_axis((-1), 1)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
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
        self.qtgui_tab_widget_1_layout_2.addWidget(self._qtgui_const_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                400000,
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                400000,
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccf(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([0.001], [1, 0.98], True)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([1,(0.707+0.707j),1j,(-0.707+0.707j),-1,(-0.707-0.707j),-1j,(0.707-0.707j)], 1)
        self.blocks_skiphead_1_0 = blocks.skiphead(gr.sizeof_float*1,  5)
        self.blocks_skiphead_1 = blocks.skiphead(gr.sizeof_float*1, 5)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1_3 = blocks.multiply_const_ff(b1)
        self.blocks_multiply_const_vxx_1_2_1 = blocks.multiply_const_ff(b4)
        self.blocks_multiply_const_vxx_1_2_0_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_1_2_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_1_2 = blocks.multiply_const_ff(b4)
        self.blocks_multiply_const_vxx_1_1_0 = blocks.multiply_const_ff(b3)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_ff(b3)
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_ff(b2)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(b2)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(b1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.5)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_float*1, demod_delay)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, demod_delay)
        self.blocks_delay_1_3 = blocks.delay(gr.sizeof_float*1, 8)
        self.blocks_delay_1_2_1 = blocks.delay(gr.sizeof_float*1, 32)
        self.blocks_delay_1_2_0_0 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_delay_1_2_0 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_delay_1_2 = blocks.delay(gr.sizeof_float*1, 32)
        self.blocks_delay_1_1_0 = blocks.delay(gr.sizeof_float*1, 24)
        self.blocks_delay_1_1 = blocks.delay(gr.sizeof_float*1, 24)
        self.blocks_delay_1_0_0 = blocks.delay(gr.sizeof_float*1, 16)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_float*1, 16)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 8)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 40)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1))
        self.analog_sig_source_x_0_2_0 = analog.sig_source_f(400000, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(400000, analog.GR_SIN_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(400000, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(400000, analog.GR_SIN_WAVE, 100000, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 8, 1000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_multiply_xx_0_2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_multiply_xx_0_2_0, 1))
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_delay_1_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.blocks_delay_1_1, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_delay_1_1_0, 0), (self.blocks_multiply_const_vxx_1_1_0, 0))
        self.connect((self.blocks_delay_1_2, 0), (self.blocks_multiply_const_vxx_1_2, 0))
        self.connect((self.blocks_delay_1_2_0, 0), (self.blocks_multiply_const_vxx_1_2_0, 0))
        self.connect((self.blocks_delay_1_2_0_0, 0), (self.blocks_multiply_const_vxx_1_2_0_0, 0))
        self.connect((self.blocks_delay_1_2_1, 0), (self.blocks_multiply_const_vxx_1_2_1, 0))
        self.connect((self.blocks_delay_1_3, 0), (self.blocks_multiply_const_vxx_1_3, 0))
        self.connect((self.blocks_delay_2, 0), (self.blocks_skiphead_1, 0))
        self.connect((self.blocks_delay_2_0, 0), (self.blocks_skiphead_1_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.qtgui_const_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.blocks_add_xx_0_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_2_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_1_2_0_0, 0), (self.blocks_add_xx_0_0, 4))
        self.connect((self.blocks_multiply_const_vxx_1_2_1, 0), (self.blocks_add_xx_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_3, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_2_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.blocks_skiphead_1, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_skiphead_1_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.iir_filter_xxx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_delay_1_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_delay_1_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_delay_1_2_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_delay_1_2_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_delay_1_3, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.blocks_delay_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.blocks_delay_1_1, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.blocks_delay_1_2, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.blocks_delay_1_2_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_delay_2, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.blocks_delay_2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TASK1_abcd")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.symbol_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_demod_delay(self):
        return self.demod_delay

    def set_demod_delay(self, demod_delay):
        self.demod_delay = demod_delay
        self.blocks_delay_2.set_dly(int(self.demod_delay))
        self.blocks_delay_2_0.set_dly(int(self.demod_delay))

    def get_b4(self):
        return self.b4

    def set_b4(self, b4):
        self.b4 = b4
        self.blocks_multiply_const_vxx_1_2.set_k(self.b4)
        self.blocks_multiply_const_vxx_1_2_1.set_k(self.b4)

    def get_b3(self):
        return self.b3

    def set_b3(self, b3):
        self.b3 = b3
        self.blocks_multiply_const_vxx_1_1.set_k(self.b3)
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.b3)

    def get_b2(self):
        return self.b2

    def set_b2(self, b2):
        self.b2 = b2
        self.blocks_multiply_const_vxx_1_0.set_k(self.b2)
        self.blocks_multiply_const_vxx_1_0_0.set_k(self.b2)

    def get_b1(self):
        return self.b1

    def set_b1(self, b1):
        self.b1 = b1
        self.blocks_multiply_const_vxx_1.set_k(self.b1)
        self.blocks_multiply_const_vxx_1_3.set_k(self.b1)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))




def main(top_block_cls=TASK1_abcd, options=None):

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
