import json
from itertools import groupby


class Links:
    def __init__(self, kros_bloc):
        self.links = []
        self.kross_bloc = kros_bloc
        self.selected_signal = ""
        self.selected_links = self.get_nodes_by_signal(self.selected_signal)
        self.selected_link = []

    def check_node(self, node):
        for klemnaya_kolodka in self.kross_bloc:
            if node in klemnaya_kolodka:
                return True
        return False

    def is_exist(self, n1, n2):
        for link in self.links:
            if (link[0] == n1 and link[1] == n2) or (link[1] == n1 and link[0] == n2):
                return True
        return False

    def add_link(self, n1, n2, signal="", info=""):
        if self.check_node(n1) and self.check_node(n2):
            if not self.is_exist(n1, n2):
                self.links.append([n1, n2, signal, info])
                return "link add success"
            else:
                return "link already exist"
        return f"n1 in kb {self.check_node(n1)}   n2 in kb {self.check_node(n2)}"

    def rem_link(self, n1, n2):  # TODO: peredelat
        link_to_rem = next((
            link for link in self.links if (link[0] == n1 and link[1] == n2) or (
                link[1] == n1 and link[0] == n2)), [None])
        if link_to_rem is not None:
            self.links.remove(link_to_rem)
            return "remove success"
        return "no such link"

    def rem_selected_link(self):  # TODO: peredelat
        if self.selected_link in self.links:
            self.links.remove(self.selected_link)
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)
            return "remove success"
        return "no such link"

    def save_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.links, file)

    def load_json(self, file_name):
        with open(file_name, 'r') as file:
            self.links = json.load(file)
            self.selected_signal = ""
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)

    def print_links(self):  # TODO: ubrat posle otladki
        for node in self.links:
            print(node)

    def edit_link(self, node1, node2, node1_new="", node2_new="", signal="", info=""):
        link_to_edit = next((
            link for link in self.links if (link[0] == node1 and link[1] == node2) or (
                link[1] == node1 and link[0] == node2)), None)
        if link_to_edit is not None:
            index = self.links.index(link_to_edit)
            if node1_new != "":
                if not ((self.is_exist(node1_new, node2) and node2_new == "") or (
                        self.is_exist(node1_new, node2_new) and node2_new != "")):
                    self.links[index][0] = node1_new
                else:
                    return "alredy exist"

            if node2_new != "":
                if not ((self.is_exist(node1, node2_new) and node1_new == "") or (
                        self.is_exist(node1_new, node2_new) and node1_new != "")):
                    self.links[index][1] = node2_new
                else:
                    return "alredy exist"
            if signal != "":
                self.links[index][2] = signal
            if info != "":
                self.links[index][2] = info

            return "edit success"
        return "no such item"

    def get_row(self, row_index):
        return [row[row_index] for row in self.links]

    def get_signals(self):  # TODO peredelat
        lsl = self.get_row(2)
        lsl.sort()
        lsl2 = [el for el, _ in groupby(lsl)]
        return lsl2

    def get_nodes_by_signal(self, signal_name):
        if signal_name == "":
            return self.links
        matches = [x for x in self.links if x[2] == signal_name]
        return matches

    def delete_signal(self, signal):
        links_to_rem = []
        for link in self.links:
            if link[2] == signal:
                links_to_rem.append(link)
        for link in links_to_rem:
            self.rem_link(link[0], link[1])
            self.select_signal(self.selected_signal)
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)

    def select_signal(self, signal=""):
        if signal in self.get_signals():
            self.selected_signal = signal
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)
            return True
        elif signal == "":
            self.selected_signal = signal
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)
            return True
        else:
            self.selected_signal = ""
            self.selected_links = self.get_nodes_by_signal(self.selected_signal)
            return False

    def select_link(self, n1, n2):
        for link in self.selected_links:
            if (link[0] == n1 and link[1] == n2) or (link[1] == n1 and link[0] == n2):
                self.selected_link = link
                return True
        return False
