import PySimpleGUI as sg

class Multiline(sg.Multiline):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ratio = 0
        self.lines = 1

    def initial(self, window, width=5, bg='#202020', fg='white', font=None):
        self.window = window
        self.line = sg.tk.Text(self.widget.master, width=5, height=self.Size[1], bg=bg, fg=fg, font=font)
        self.line.pack(side='left', fill='y', expand=False, before=self.widget)
        self.line.bindtags((str(self.line), str(window.TKroot), "all"))
        self.line.tag_add("right", '1.0', "end")
        self.line.tag_configure("right", justify='right')
        self.line.delete('1.0', 'end')
        self.line.insert('1.0', '1', 'right')
        self.bind('<Configure>', '')
        self.bind('<MouseWheel>', '')
        self.vsb.configure(command=self.y_scroll)
        window.refresh()
        window.move_to_center()

    def reset(self):
        self.window.refresh()
        new_ratio, _ = self.vsb.get()
        new_lines = int(self.widget.index(sg.tk.END).split('.')[0]) - 1
        if new_lines != self.lines:
            self.lines = new_lines
            text = '\n'.join([f'{i+1}' for i in range(self.lines)])
            self.line.delete('1.0', 'end')
            self.line.insert('1.0', text)
            self.line.tag_add("right", '1.0', "end")
        if new_ratio != self.ratio:
            self.ratio = new_ratio
            self.line.yview_moveto(self.ratio)

    def y_scroll(self, action, n, what=None):
        if action == sg.tk.MOVETO:
            self.widget.yview_moveto(n)
            self.line.yview_moveto(n)
        elif action == sg.tk.SCROLL:
            self.widget.yview_scroll(n, what)
            self.line.yview_scroll(n, what)

font = ('Courier New', 20)
sg.theme('Darkblue')
sg.set_options(font=font)

column1 = [
    [Multiline('',   size=(40, 10), justification='left', focus=True, pad=(0, 0),
        background_color='#404040', text_color='white', expand_x=True,
        expand_y=True, enable_events=True, horizontal_scroll=True, sbar_width=20,
        sbar_arrow_width=20, key='-ML-')],
]
layout = [[sg.Column(column1, expand_x=True, expand_y=True, pad=(0, 0))]]
location = sg.Window.get_screen_size()
window = sg.Window('Title', layout, resizable=True, margins=(0, 0), location=location, finalize=True)
ml = window['-ML-']
ml.initial(window, width=5, bg='#202020', fg='#808080', font=font)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == '-ML-':
        ml.reset()

window.close()
