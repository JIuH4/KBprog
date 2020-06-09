from gui_classes import AutocompleteEntry, Table, SignalList
from gui_sheme import Kbsheme
from krossblocks import KBK
from  utils import Utils
from tkinter import filedialog
import links as lnk
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

ut=Utils("ss")
ut.m151_200 = "p2"
ut.m1_50 = "p1"
ut.generate_links()

links = lnk.Links(KBK,ut)
print(links.check_node("CH_98"))
links.load_json("test_data")


def popupmsg(msg="Подключение модулей"):

    popup = tk.Tk(className='Tkkross')
    popup.wm_title("Подключение модулей")
    label = ttk.Label(popup, text=msg)
    comboExample = ttk.Combobox(popup,
                                values=ut.connectors)
    comboExample.pack()
    comboExample2 = ttk.Combobox(popup,
                                values=ut.connectors)
    comboExample2.pack()
    comboExample3 = ttk.Combobox(popup,
                                values=ut.connectors)
    comboExample3.pack()
    comboExample4 = ttk.Combobox(popup,
                                values=ut.connectors)
    comboExample4.pack()
    label.pack(side="top", fill="x", pady=10)
    def plop():
        popup.destroy()
    B1 = ttk.Button(popup, text="Okay", command = plop)
    B1.pack()
    popup.mainloop()


# print(links.edit_link("K_1", "M_51",node2_new="M_59"))


def add():
    if entry_sign.get() != "":
        links.add_link(entry.get(), entry2.get(), signal=entry_sign.get())
        links.select_signal(entry_sign.get())
        refresh_signals()
        refresh_links()
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        if sheme is not None:
            sheme.redboxes_num = 0
            sheme.rbox_tag = [""] * 2


def delete_signale():
    signal_to_rem = signal_list.get_selected()
    links.delete_signal(signal_to_rem)
    refresh_signals()
    refresh_links()


def delete_link():
    link_to_rem = tbl.get_selected()
    links.select_link(link_to_rem[0], link_to_rem[1])
    links.rem_selected_link()
    refresh_signals()
    refresh_links()


sheme = None
shemeWindow = None


def create_window():
    global sheme, shemeWindow
    if shemeWindow is None:
        shemeWindow = tk.Toplevel(root, class_='Tkkross2')
        sheme = Kbsheme(shemeWindow, entr=sheme_select)
        sheme.pack()
        refresh_links()
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        return shemeWindow
    else:
        shemeWindow.destroy()
        sheme = None
        shemeWindow = None


def select_signal(event):
    links.select_signal(signal_list.get_selected())
    if links.selected_signal != "":
        entry_sign.delete(0, tk.END)
        entry_sign.insert(0, links.selected_signal)
    refresh_links()


def select_link(event):
    selectd = tbl.get_selected()
    links.select_link(selectd[0], selectd[1])
    if sheme is not None:
        sheme.selected_link = links.selected_link
        sheme.higlight_link()


def refresh_links():
    tbl.nodes = links.selected_links
    tbl.refresh_tree()
    if sheme is not None:
        sheme.selected_links = links.selected_links
        sheme.print_links()


def refresh_signals():
    tmp = signal_list.get_selected()
    signal_list.signals = links.get_signals()
    signal_list.refresh()
    signal_list.set_selected_by_name(tmp)


def opn():
    root.filename = filedialog.askopenfilename(
        title="Select file",
        filetypes=(("JSON", "*.json"), ("all files", "*.*")))
    if root.filename:
        links.load_json(root.filename)
        refresh_signals()
        refresh_links()


def save_as():
    root.filename = filedialog.asksaveasfilename(
        title="Select file",
        filetypes=(("JSON", "*.json"), ("all files", "*.*")))
    if root.filename:
        links.save_json(root.filename)


def sheme_select(tag):
    if entry.get() == "" and entry2.get() != tag:
        entry.delete(0, tk.END)
        entry.insert(0, tag)
        entry.selection(None)
        return True
    elif entry.get() == tag:
        entry.delete(0, tk.END)
        delete_link()
        return False
    if entry2.get() == "" and entry.get() != tag:
        entry2.delete(0, tk.END)
        entry2.insert(0, tag)
        entry2.selection(None)
        return True
    elif entry2.get() == tag:
        entry2.delete(0, tk.END)
        delete_link()
        return False
    print("ttt" + tag)


def graf():
    G = nx.Graph()

    lins_gr = links.links

    gr = np.array(lins_gr)
    gr2 = gr[:, 0:2]

    G.add_edges_from(gr2)

    def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                    vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                    pos=pos, parent=root)
        return pos

    if not nx.is_tree(G):
        print('cannot use hierarchy_pos on a graph that is not a tree')
        nx.draw(G, with_labels=True)
    else:
        pos = hierarchy_pos(G, "K_1")
        print(list(nx.bfs_edges(G, "K_1")))
        nx.draw(G,  pos=pos, with_labels=True)
    plt.show()

autocompleteList = list()
for klemnik in KBK:
    autocompleteList.extend(klemnik)

root = tk.Tk(className='Tkkross')
root.title("Добавление сигналов")
# labels
ttk.Label(root, text="Сигнал").grid(column=0, row=0, padx=6, sticky='s')
ttk.Label(root, text="Клемник1").grid(column=1, row=0, padx=6, sticky='s')
ttk.Label(root, text="Клемник2").grid(column=2, row=0, padx=6, sticky='s')
# entrys
entry_sign = ttk.Entry()
entry_sign.grid(column=0, row=1, padx=6, pady=6)
entry = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32)
entry.grid(row=1, column=1)
entry2 = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32)
entry2.grid(row=1, column=2)
# Buttons
ttk.Button(text="Добавить", command=add).grid(column=3, row=1, padx=6, pady=6)
ttk.Button(text="Удалить сигнал", command=delete_signale).grid(column=0, row=3, padx=6, pady=6)
ttk.Button(text="Удалить", command=delete_link).grid(row=2, column=3, padx=5, pady=5)
ttk.Button(text="Cхема", command=create_window).grid(row=4, column=3, padx=5, pady=5)
ttk.Button(text="Cхема", command=graf).grid(row=4, column=2, padx=5, pady=5)

# таблица связей
tbl = Table(root, class_='Table_Nodes', row=2, column=1, columnspan=2, entr=select_link)
signal_list = SignalList(root, row=2, column=0, columnspan=1, entr=select_signal)

menubar = tk.Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=opn)
filemenu.add_command(label="Save", command=save_as)
filemenu.add_separator()

menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="pop!", command=popupmsg)
helpmenu.add_command(label="QUIT!", command=root.quit)
menubar.add_cascade(label="Quit", menu=helpmenu)
# menubar.add_cascade(label="Quit222", menu=popupmsg)
# display the menu
root.config(menu=menubar)

links.select_signal("")
refresh_signals()
refresh_links()

root.mainloop()
