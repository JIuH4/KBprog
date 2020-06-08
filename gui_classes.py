import tkinter as tk
import tkinter.ttk as ttk
import re
import links


class Table(ttk.Treeview):
    def __init__(self, root, *args, **kwargs):

        # # Listbox length
        if 'row' in kwargs:
            self.row = kwargs['row']
            del kwargs['row']
        else:
            self.row = 1

        if 'entr' in kwargs:
            self.entr = kwargs['entr']
            del kwargs['entr']
        else:
            self.entr = lambda event: print("ss")

        if 'column' in kwargs:
            self.column = kwargs['column']
            del kwargs['column']
        else:
            self.column = 0

        if 'columnspan' in kwargs:
            self.columnspan = kwargs['columnspan']
            del kwargs['columnspan']
        else:
            self.columnspan = 1

        ttk.Treeview.__init__(self, root, *args, **kwargs)
        # self.focus()

        self.nodes = []

        self.cols = ('Nod_1', 'Nod_2', "Signal")
        self.listBox = ttk.Treeview(
            root, selectmode='browse', columns=self.cols, show='headings')
        self.listBox.grid(row=self.row, column=self.column,
                          columnspan=self.columnspan)
        for col in self.cols:
            self.listBox.heading(col, text=col)
        self.verscrlbar = ttk.Scrollbar(
            root, orient="vertical", command=self.listBox.yview)
        self.verscrlbar.grid(
            row=2, column=1, columnspan=self.columnspan, sticky='nes')
        self.listBox.bind("<<TreeviewSelect>>", self.entr)

    def refresh_tree(self):
        for i in self.listBox.get_children():
            self.listBox.delete(i)

        for i in self.nodes:
            self.listBox.insert("", "end", values=(i[0], i[1], i[2]))

    def sss(self):
        print("sd")

    def delete_selected(self, link):

        selection = self.listBox.focus()

        rem = self.listBox.item(selection)["values"]

        if rem != "":
            print(links.rem_link(rem[0], rem[1], link))

        self.refresh_tree()

    def get_selected(self):

        selection = self.listBox.focus()

        rem = self.listBox.item(selection)["values"]

        if rem != "":
            return rem
        return "no selected item"

    # self.var.trace('w', self.changed)
    # self.bind("<Right>", self.selection)
    # self.bind("<Up>", self.moveUp)
    # self.bind("<Down>", self.moveDown)

    # self.listboxUp = False


class AutocompleteEntry(ttk.Entry):
    def __init__(self, autocomplete_list, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(field_value, ac_list_entry):
                pattern = re.compile(
                    '.*' + re.escape(re.sub("_", "", field_value)) + '.*',
                    re.IGNORECASE)
                return re.match(pattern, re.sub("_", "", ac_list_entry))

            self.matchesFunction = matches

        ttk.Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocomplete_list

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = tk.StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        self.bind("<Return>", self.selection)
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()  # pylint: disable="access-member-before-definition" # noqa
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = tk.Listbox(
                        width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(
                        x=self.winfo_x(),
                        y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, tk.END)
                for w in words:
                    self.listbox.insert(tk.END, w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False

    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(tk.ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(tk.END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != tk.END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [w for w in self.autocompleteList
                if self.matchesFunction(self.var.get(), w)]


class SignalList(tk.Listbox):
    def __init__(self, root, *args, **kwargs):

        # # Listbox positional args
        if 'row' in kwargs:
            self.row = kwargs['row']
            del kwargs['row']
        else:
            self.row = 1

        if 'column' in kwargs:
            self.column = kwargs['column']
            del kwargs['column']
        else:
            self.column = 0

        if 'columnspan' in kwargs:
            self.columnspan = kwargs['columnspan']
            del kwargs['columnspan']
        else:
            self.columnspan = 1

        # # transfered functions

        if 'entr' in kwargs:
            self.entr = kwargs['entr']
            del kwargs['entr']
        else:
            self.entr = lambda event: print("ss")

        tk.Listbox.__init__(self, root, *args, **kwargs)

        self.signals = []

        self.listBox = tk.Listbox(exportselection=0)
        self.listBox.grid(row=self.row, column=self.column,
                          columnspan=self.columnspan, sticky='nesw', padx=5, )
        self.verscrlbar = ttk.Scrollbar(
            root, orient="vertical", command=self.listBox.yview)
        self.verscrlbar.grid(
            row=self.row, column=self.column, columnspan=self.columnspan, sticky='nes', padx=5, )
        self.listBox.bind("<<ListboxSelect>>", self.entr)

    def refresh(self):
        self.listBox.delete(0, tk.END)

        for signal in self.signals:
            self.listBox.insert(tk.END, signal)
        self.listBox.insert(0, "all signals")

    def get_selected(self):
        curselection = self.listBox.curselection()
        if curselection != ():
            index = int(curselection[0])
            value = self.listBox.get(index)
            if value == "all signals":
                return ""
            return value
        return ""

    def get_index_of(self, item):

        for index in range(0, self.listBox.size()):
            if self.listBox.get(index) == item:
                return index
        return 0

    def set_selected(self, index):

        self.listBox.selection_set(index)

    def set_selected_by_name(self, name):
        self.set_selected(self.get_index_of(name))

