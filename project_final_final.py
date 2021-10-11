# This program converts USD to any currency

import tkinter
import tkinter.messagebox

class CurrencyConvert:
    def __init__(self):
        
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Currency Converter')
        self.main_window.geometry('400x190')

        # Convert three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create and pack Label Widget in top frame
        self.prompt_label = tkinter.Label(self.top_frame, \
                                    text='Convert any amount of USD')
        self.top_entry = tkinter.Entry(self.top_frame, \
                                       width=10)
        self.top_label = tkinter.Label(self.top_frame, \
                                       text='USD')
        self.prompt_label.pack()
        self.top_entry.pack(side='left')
        self.top_label.pack(side='left')

        # Create a IntVar object for Radiobuttons
        self.radio_var = tkinter.IntVar()

        # Set intVar object to 1
        self.radio_var.set(1)

        # Create the Radiobutton widgets in mid
        self.rb1 = tkinter.Radiobutton(self.mid_frame, \
                                       text='EUR', \
                            variable=self.radio_var, \
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.mid_frame, \
                                       text='CAD', \
                            variable=self.radio_var, \
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.mid_frame, \
                                       text='JPY', \
                            variable=self.radio_var, \
                                       value=3)
        self.rb4 = tkinter.Radiobutton(self.mid_frame, \
                                       text='GBP', \
                            variable=self.radio_var, \
                                       value=4)

        # Pack the Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()

        # Create and pack widgets at the bottom frame
        self.convert_button = tkinter.Button(self.bottom_frame, \
                                             text='Convert', \
                                        command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                            text='Quit', \
                                        command=self.main_window.destroy)
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop
        tkinter.mainloop()

    # Calculate the conversions
    def convert(self):
        if self.radio_var.get() == 1:
            rate = 0.84
        elif self.radio_var.get() == 2:
            rate = 1.31
        elif self.radio_var.get() == 3:
            rate = 103.77
        else:
            rate = 0.75

        conversion = float(self.top_entry.get()) * rate
        tkinter.messagebox.showinfo('Conversion', \
                                    'Your conversion is ' + \
                                    format(conversion, ',.2f') + \
                                    '.')

# Create an instance of the CurrencyConvertGUI
currency_convert = CurrencyConvert()
