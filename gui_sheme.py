import tkinter as tk
import tkinter.ttk as ttk


class Kbsheme(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        if 'entr' in kwargs:
            self.entr = kwargs['entr']
            del kwargs['entr']
        else:
            self.entr = lambda tag: print(tag)
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.c = tk.Canvas(parent, width=1700, height=800, bg='grey80')

        self.selected_links = []
        self.selected_link = []
        self.links_objects = []
        self.box_objects = []
        self.redboxes_num = 0
        self.rbox_tag = [""]*2
        # PRINT KBK
        self.terminal_print_face_down(600, 30, 10, "C")
        self.terminal_print_face_down(200, 120, 50, "BA1")
        self.terminal_print_face_down(900, 120, 50, "BA3")
        self.terminal_print_face_down(200, 250, 50, "BA2")
        self.terminal_print_face_down(900, 250, 50, "BA4")
        self.terminal_print_face_down(1550, 300, 8, "K")
        self.terminal_print_face_down(40, 300, 8, "K", start_number=8)
        self.terminal_print_face_up(200, 620, 50, "M", start_number=0, shift=25)
        self.terminal_print_face_up(900, 620, 50, "M", start_number=25, shift=25)
        self.terminal_print_face_up(180, 500, 52, "M", start_number=100, shift=26)
        self.terminal_print_face_up(900, 500, 52, "M", start_number=126, shift=26)
        self.terminal_print_face_down(300, 750, 100, "CH")
        self.terminal_print_face_up(180, 420, 25, "MB1")
        self.terminal_print_face_up(900, 420, 25, "MB2")
        self.terminal_print_face_up(180, 350, 25, "MB3")
        self.terminal_print_face_up(900, 350, 25, "MB4")
        self.c.pack(side="left", fill="both", expand=True)
        # EVENTS
        self.c.tag_bind("press", '<Button-1>', self.event_process)
        # parent.bind('<Return>', self.event_process)
        self.c.bind("<Return>", (lambda event:print("adasd")))
    def print_link(self, tag1, tag2):
        box1 = self.c.find_withtag(tag1)
        box2 = self.c.find_withtag(tag2)
        self.c.itemconfig(box1[0], fill="yellow")
        self.c.itemconfig(box2[0], fill="yellow")
        self.box_objects.append(box1[0])
        self.box_objects.append(box2[0])
        tag1_coords = self.c.coords(tag1)
        tag2_coords = self.c.coords(tag2)
        tag = f"{tag1}_{tag2}"
        self.links_objects.append(self.c.create_line(
            tag1_coords[0] + 5, tag1_coords[1] + 5, tag2_coords[0] + 5,
            tag2_coords[1] + 5, width=2, tag=tag, fill='red'))

    def higlight_link(self):
        tag1 = self.selected_link[0]
        tag2 = self.selected_link[1]
        for klm in self.box_objects:
            self.c.itemconfig(klm, fill="yellow")
        tag = f"{tag1}_{tag2}"
        box1 = self.c.find_withtag(tag1)
        box2 = self.c.find_withtag(tag2)
        self.c.itemconfig(box1[0], fill="cyan")
        self.c.itemconfig(box2[0], fill="cyan")
        for link in self.links_objects:
            self.c.itemconfig(link, fill="red")
        lin = self.c.find_withtag(tag)
        self.c.itemconfig(lin, fill="blue")
        self.c.tag_raise(tag)

    def clean_links(self):
        for link in self.links_objects:
            self.c.delete(link)
        for box in self.box_objects:
            self.c.itemconfig(box, fill="lightgreen")
        self.box_objects.clear()
        self.links_objects.clear()

    def print_links(self):
        self.clean_links()
        for item in self.selected_links:
            self.print_link(item[0], item[1])
        self.selected_link = self.selected_links[0]
        self.higlight_link()

    def get_by_coord(self, x: object, y):
        obj = self.c.find_closest(x, y)
        if self.c.type(obj) == "rectangle":
            return obj
        else:
            obj = self.c.find_below(obj)
        return obj

    def event_process(self, event):
        i = self.get_by_coord(event.x, event.y)
        tag = self.c.gettags(i)
        # self.entr(tag[0])
        if tag[0] in self.rbox_tag:
            for index in range(2):
                if self.rbox_tag[index] == tag[0]:
                    self.rbox_tag[index]=""
                    self.c.itemconfig(i, fill="lightgreen")
                    self.entr(tag[0])
                    return False
        else:
            for index in range(2):
                if self.rbox_tag[index] == "":
                    self.rbox_tag[index]=tag[0]
                    self.c.itemconfig(i, fill="red")
                    self.entr(tag[0])
                    return False

        # if self.c.itemcget(i, "fill") == "lightgreen":
        #     if self.redboxes_num < 2:
        #         self.c.itemconfig(i, fill="red")
        #         self.redboxes_num = self.redboxes_num + 1
        # elif self.c.itemcget(i, "fill") == "red":
        #     if i in self.box_objects:
        #         self.c.itemconfig(i, fill="yellow")
        #     else:
        #         self.c.itemconfig(i, fill="lightgreen")
        #     self.redboxes_num = self.redboxes_num - 1

    def terminal_print_face_down(self, base_x, base_y, count, name, size=21,
                                 gap=2, start_number=0, shift=0):
        self.c.create_text(base_x + count // 4,
                           base_y - 10,
                           tag=f"{name}",
                           text=f"{name}",
                           font="Verdana 10")
        for number_in_row in range(0, count // 2):
            tag = (
                f"{name}_{start_number + number_in_row + 1}", "press")
            self.c.create_rectangle(base_x + (size + gap) * number_in_row,
                                    base_y,
                                    base_x + size +
                                    (size + gap) * number_in_row,
                                    base_y + size,
                                    tag=tag,
                                    fill="lightgreen")
            self.c.create_text(
                base_x + (size + gap) * number_in_row + size // 2,
                base_y + size // 2,
                tag=tag,
                text=f"{start_number + number_in_row + 1}",
                font="Verdana 7")
        for number_in_row in range(count // 2, count):
            tag = (
                f"{name}_{start_number + shift + number_in_row + 1}",
                "press")
            self.c.create_rectangle(
                base_x + (size + gap) * (number_in_row - count // 2),
                base_y + size + gap,
                base_x + size +
                (size + gap) * (number_in_row - count // 2),
                base_y + size * 2 + gap,
                tag=tag,
                fill="lightgreen")
            self.c.create_text(
                base_x + (size + gap) *
                (number_in_row - count // 2) + size / 2,
                base_y + size // 2 + size + gap,
                text=f"{start_number + shift + number_in_row + 1}",
                tag=tag,
                font="Verdana 7")

    def terminal_print_face_up(self, base_x, base_y, count, name, size=21,
                               gap=2, start_number=0, shift=0):
        self.c.create_text(base_x + count // 4,
                           base_y - 10,
                           tag=f"{name}",
                           text=f"{name}",
                           font="Verdana 10")
        for number_in_row in range(0, count // 2):
            tag = (
                f"{name}_{start_number + number_in_row + 1}", "press")
            self.c.create_rectangle(base_x + (size + gap) * number_in_row,
                                    base_y + size + gap,
                                    base_x + size +
                                    (size + gap) * number_in_row,
                                    base_y + size * 2 + gap,
                                    tag=tag,
                                    fill="lightgreen")
            self.c.create_text(
                base_x + (size + gap) * number_in_row + size // 2,
                base_y + size // 2 + size + gap,
                tag=tag,
                text=f"{start_number + number_in_row + 1}",
                font="Verdana 7")
        for number_in_row in range(count // 2, count):
            tag = (
                f"{name}_{start_number + shift + number_in_row + 1}", "press")
            self.c.create_rectangle(
                base_x + (size + gap) * (number_in_row - count // 2),
                base_y,
                base_x + size +
                (size + gap) * (number_in_row - count // 2),
                base_y + size,
                tag=tag,
                fill="lightgreen")
            self.c.create_text(
                base_x + (size + gap) *
                (number_in_row - count // 2) + size / 2,
                base_y + size // 2,
                text=f"{start_number + shift + number_in_row + 1}",
                tag=tag,
                font="Verdana 7")
