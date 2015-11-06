# -*- coding: utf-8 -*-
# python

import Tkinter, dfcimanager_executor, tk_widgets as tkwid, config

"""
	The module supplies a class to display a graphical user interface. 
"""

class DFCIManagerGUI(Tkinter.Tk):

	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def form_connection_parameters(self, x, y, xspan, yspan):

		frame_connparam = tkwid.display_frame("Paramètres de connexion".decode("utf8"), x, y, xspan, yspan)

		self.label_host = tkwid.display_label(frame_connparam, "Hôte :".decode("utf8"), x, y + 1, None, None)
		self.label_port = tkwid.display_label(frame_connparam, "Port :", x, y + 2, None, None)
		self.label_dbname = tkwid.display_label(frame_connparam, "Base de \ndonnées :".decode("utf8"), x, y + 3, None, None)
		self.label_user = tkwid.display_label(frame_connparam, "Utilisateur :", x, y + 4, None, None)
		self.label_password = tkwid.display_label(frame_connparam, "Mot de passe :", x, y + 5, None, None)

		self.entry_host = tkwid.display_entry(frame_connparam, config.host, x + xspan - 1, y + 1, None, None)
		self.entry_port = tkwid.display_entry(frame_connparam, config.port, x + xspan - 1, y + 2, None, None)
		self.entry_dbname = tkwid.display_entry(frame_connparam, config.dbname, x + xspan - 1, y + 3, None, None)
		self.entry_user = tkwid.display_entry(frame_connparam, config.user, x + xspan - 1, y + 4, None, None)
		self.entry_password = tkwid.display_entry(frame_connparam, config.password, x + xspan - 1, y + 5, None, None)
		self.entry_password[1].config(show = "*")

	def form_database_tables(self, x, y, xspan, yspan):

		frame_db_tbl = tkwid.display_frame("Table à mettre à jour".decode("utf8"), x, y, xspan, yspan)

		radiobuttons_list = [("tro", "tro"), ("deb", "deb"), ("Toutes", "all")]
		configuration = "radiobuttons.config(font = \"Calibri 10\")"
		self.radiobutton_tables = tkwid.display_radiobuttons(frame_db_tbl, radiobuttons_list, configuration, x, y+1, xspan, yspan)

		
	def initialize(self):
		self.grid()

		self.form_connection_parameters(0, 0, 2, None)
		tkwid.display_label(None, " " * 5, 2, 0, None, None)
		self.form_database_tables(3, 0, 2, None)
		self.label_process_status = tkwid.display_label(None, "", 0, 8, 4, None)
		self.label_process_status[1].config(font="Calibri 10 bold", fg = "#000000")

		self.grid_columnconfigure(0, weight = 0)
		self.resizable(True, False)

		self.butt_update_table = Tkinter.Button(self, text = u"Mettre à jour", anchor = "w", command = self.update_table)
		self.butt_update_table.grid(column = 4, row = 8)

	def update_table(self):
		connection_values = [self.entry_host[0].get(), self.entry_port[0].get(), self.entry_dbname[0].get(),
		self.entry_user[0].get(), self.entry_password[0].get()]
		if self.radiobutton_tables.get() == "all":
			status = dfcimanager_executor.run_update_queries_all(connection_values)
			self.label_process_status[0].set(status)
		else:
			status = dfcimanager_executor.run_update_queries_by_tablename(connection_values, self.radiobutton_tables.get())
			self.label_process_status[0].set(status)

if __name__ == "__main__":
	dfci_manager_gui = DFCIManagerGUI(None)
	dfci_manager_gui['bg']= None
	dfci_manager_gui.title('DFCIManager')
	dfci_manager_gui.mainloop()