from tkinter import *
from mbit import mBit
from monobit import monoBit
from autocorelation import autocorrelation
from serial import serial
from PIL import ImageTk, Image

def click_monobit_test():
  # Pentru inceput distrug widget-urile existente pe panoul din dreapta.
  for widget in right_panel.winfo_children():
    widget.destroy()
  alpha_label = Label(right_panel, text="Alpha:")
  alpha_label.grid(pady = 20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady = 20)

  token_label = Label(right_panel, text="Token:")
  token_label.grid(pady=20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20)

  def execute_test():
    alpha = (float)(alpha_entry.get())
    token = token_entry.get().encode()
    result = monoBit(alpha, token)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 0)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20)

def click_mbit_test():
  # Pentru inceput curatam panoul din dreapta.
  # Method winfo_children() return a list of all widgets which are children of this widget.
  for widget in right_panel.winfo_children():
    widget.destroy()
  alpha_label = Label(right_panel, text="Alpha:")
  alpha_label.grid(pady = 5)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady = 5)

  m_label = Label(right_panel, text="m:")
  m_label.grid(pady = 5)
  m_entry = Entry(right_panel)
  m_entry.grid(pady = 5)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady = 5)
  token_entry = Entry(right_panel)
  token_entry.grid(pady = 5)

  def execute_test():
    alpha = float(alpha_entry.get())
    m = int(m_entry.get())
    token = (token_entry.get()).encode()
    result = mBit(alpha, m, token)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 0)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20)

def click_autocorelation():
  for widget in right_panel.winfo_children():
    widget.destroy()
  
  alpha_label = Label(right_panel, text="alpha:")
  alpha_label.grid(pady=20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady=20)

  n_label = Label(right_panel, text="n:")
  n_label.grid(pady=20)
  n_entry = Entry(right_panel)
  n_entry.grid(pady=20)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady=20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20)

  x_label = Label(right_panel, text="x:")
  x_label.grid(pady=20)
  x_entry = Entry(right_panel)
  x_entry.grid(pady=20)

  y_label = Label(right_panel, text="y:")
  y_label.grid(pady=20)
  y_entry = Entry(right_panel)
  y_entry.grid(pady=20)
  def execute_test():
    alpha = float(alpha_entry.get())
    n = int(n_entry.get())
    token = token_entry.get().encode()
    x = int(x_entry.get())
    y = int(y_entry.get())
    result = autocorrelation(n, token, alpha, x, y)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 0)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20)

def click_serial():
  for widget in right_panel.winfo_children():
    widget.destroy()
  
  alpha_label = Label(right_panel, text="alpha:")
  alpha_label.grid(pady=20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady=20)

  n_label = Label(right_panel, text="n:")
  n_label.grid(pady=20)
  n_entry = Entry(right_panel)
  n_entry.grid(pady=20)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady=20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20)

  m_label = Label(right_panel, text="m:")
  m_label.grid(pady=20)
  m_entry = Entry(right_panel)
  m_entry.grid(pady=20)

  def execute_test():
    alpha = float(alpha_entry.get())
    n = int(n_entry.get())
    token = token_entry.get().encode()
    m = int(m_entry.get())
    result = serial(n, token, alpha, m)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 0)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20)

root = Tk()

root.title("NIST security-validator")

label1 = Label(root, text="Selectati unul dintre testele pe care doriti sa le aplicati.", fg = "black", bg="beige", font = ("Console", 16), anchor="center")
label1.grid(row = 0, column = 1, padx = 310, pady = 2)

# creez un frame in partea stanga de culoare bej unde voi amplasa butoanele
left_panel = Frame(root, bg="beige", width = 500, height=1100)
#stikcy pe nord sud west, adica tocmai in partea stanga.
left_panel.grid(padx=0, pady=0, sticky="nsw")

center_panel = Frame(root, bg="white", width=300, height=300)
center_panel.grid(row=1, column=1, padx=10, pady=10, sticky="n")
center_panel.place(anchor="center", relx=0.5, rely=0.55)


# Încarc și afișez imaginea în frame-ul central
# deschid imaginea cu ajutorul modulului PIL, image
image = Image.open("img.jpg")
image = image.resize((750, 650))
# creez imaginea intr-un format pe care tkinter il poate afisa, cu ImageTk
# # insa tkinter neputand manipula imaginea direct, o convertesc cu clasa PhotoImage.
photo_tkinter = ImageTk.PhotoImage(image)
photo_label = Label(center_panel, image = photo_tkinter)
photo_label.grid(pady  = 0)


label_left1 = Button(left_panel, text="Frequency test", background="cornflower blue", activebackground="DeepSkyBlue2", border=3, command=click_mbit_test)
label_left1.grid(pady = 90, padx = 50)

label_left2 = Button(left_panel, text="M-bit test", background="cornflower blue", activebackground="DeepSkyBlue2", border=3, command=click_monobit_test)
label_left2.grid(pady = 110)

label_left2 = Button(left_panel, text="Autocorelation test", background="cornflower blue", activebackground="DeepSkyBlue2", border=3, command = click_autocorelation)
label_left2.grid(pady = 110)

label_left2 = Button(left_panel, text="Serial test", background="cornflower blue", activebackground="DeepSkyBlue2", border=3, command=click_serial)
label_left2.grid(pady = 110)

right_panel = Frame(root, bg = "beige")
right_panel.grid(sticky="nse", row=1, column=1, padx=20, pady=20)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.mainloop()