# -*- coding: utf-8 -*-
# python

import Tkinter
import ttk

"""
The module supplies functions to display graphical elements in a GUI
"""

def display_frame(text_to_set, x, y, xspan, yspan):

	frame = Tkinter.LabelFrame(text=text_to_set, relief="groove", borderwidth=2)
	frame.grid(column = x, row = y, columnspan = xspan, rowspan = yspan, sticky='EW')
	return frame


def display_label(frame, text_to_set, x, y, xspan, yspan):

	labelVar = Tkinter.StringVar()
	label = Tkinter.Label(frame, textvariable = labelVar, anchor = "w", justify = "left", font = "Calibri 10")
	label.grid(column = x, row = y, columnspan = xspan, rowspan = yspan, sticky='EW')
	labelVar.set(u"%s" % text_to_set)
	return labelVar, label

def display_entry(frame, text_to_set, x, y, xspan, yspan):

	entryVar = Tkinter.StringVar()
	entry = Tkinter.Entry(frame, justify = "left",textvariable = entryVar, font = "Calibri 10", width = 10)
	entryVar.set(text_to_set)
	entry.grid(column = x, row = y, colspan = xspan, rowspan = yspan, sticky='EW')
	return entryVar, entry

def display_radiobuttons(frame, radiobuttons_list, configuration, x, y, xspan, yspan):
	radiobuttonsVar = Tkinter.StringVar()
	for i in radiobuttons_list:
		radiobuttons = Tkinter.Radiobutton(frame, text = i[0], variable = radiobuttonsVar, anchor = "w", 
			value = i[1], font = "Calibri 10")
		exec("%s" % configuration)
		radiobuttons.grid(column = x, row = y + (radiobuttons_list.index(i)), sticky='EW')
	return radiobuttonsVar