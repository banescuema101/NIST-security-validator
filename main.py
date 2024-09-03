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

  describe_label = Label(right_panel, text="Enter the parameters")
  describe_label.grid(pady = 10, padx = 20)

  alpha_label = Label(right_panel, text="Alpha:")
  alpha_label.grid(pady = 20, padx = 20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady = 20, padx = 20)

  token_label = Label(right_panel, text="Token:")
  token_label.grid(pady=20, padx = 20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20, padx = 20)

  def execute_test():
    alpha = (float)(alpha_entry.get())
    token = token_entry.get().encode()
    result = monoBit(alpha, token)
    result_label.config(text = result)
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 20, padx = 20)
  #creez label nou pentru a afisa rezultatul
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20, padx = 20)

def click_mbit_test():
  # Pentru inceput curatam panoul din dreapta.
  # Method winfo_children() return a list of all widgets which are children of this widget.
  for widget in right_panel.winfo_children():
    widget.destroy()

  describe_label = Label(right_panel, text="Enter the parameters")
  describe_label.grid(pady = 10, padx = 20)
  
  alpha_label = Label(right_panel, text="Alpha:")
  alpha_label.grid(pady = 20, padx = 20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady = 20, padx = 20)

  m_label = Label(right_panel, text="m:")
  m_label.grid(pady = 20, padx = 20)
  m_entry = Entry(right_panel)
  m_entry.grid(pady = 20, padx = 20)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady = 20, padx = 20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady = 20, padx = 20)

  def execute_test():
    alpha = float(alpha_entry.get())
    m = int(m_entry.get())
    token = (token_entry.get()).encode()
    result = mBit(alpha, m, token)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(pady = 20, padx = 20)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20, padx = 20)

def click_autocorelation():
  for widget in right_panel.winfo_children():
    widget.destroy()

  describe_label = Label(right_panel, text="Enter the parameters")
  describe_label.grid(pady = 10, padx = 20)

  alpha_label = Label(right_panel, text="alpha:")
  alpha_label.grid(pady=20, padx = 20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady=20, padx = 20)

  n_label = Label(right_panel, text="n:")
  n_label.grid(pady=20, padx = 20)
  n_entry = Entry(right_panel)
  n_entry.grid(pady=20, padx = 20)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady=20, padx = 20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20, padx = 20)

  x_label = Label(right_panel, text="x:")
  x_label.grid(pady=20, padx = 20)
  x_entry = Entry(right_panel)
  x_entry.grid(pady=20, padx = 20)

  y_label = Label(right_panel, text="y:")
  y_label.grid(pady=20, padx = 20)
  y_entry = Entry(right_panel)
  y_entry.grid(pady=20, padx = 20)
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
  result_label.grid(padx = 20, pady = 20)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20, padx = 20)

def click_serial():
  for widget in right_panel.winfo_children():
    widget.destroy()

  describe_label = Label(right_panel, text="Enter the parameters")
  describe_label.grid(pady = 10, padx = 20)

  alpha_label = Label(right_panel, text="alpha:")
  alpha_label.grid(pady=20, padx = 20)
  alpha_entry = Entry(right_panel)
  alpha_entry.grid(pady=20, padx = 20)

  n_label = Label(right_panel, text="n:")
  n_label.grid(pady=20, padx = 20)
  n_entry = Entry(right_panel)
  n_entry.grid(pady=20, padx = 20)

  token_label = Label(right_panel, text="token:")
  token_label.grid(pady=20, padx = 20)
  token_entry = Entry(right_panel)
  token_entry.grid(pady=20, padx = 20)

  m_label = Label(right_panel, text="m:")
  m_label.grid(pady=20, padx = 20)
  m_entry = Entry(right_panel)
  m_entry.grid(pady=20, padx = 20)

  def execute_test():
    alpha = float(alpha_entry.get())
    n = int(n_entry.get())
    token = token_entry.get().encode()
    m = int(m_entry.get())
    result = serial(n, token, alpha, m)
    result_label.config(text = result)
  
  #creez label nou pentru a afisa rezultatul
  result_label = Label(right_panel, text = "", bg="beige")
  result_label.grid(padx = 20, pady = 20)
  #in momentul in care este apasat butonul "Done", se executa functia si se reconfigureaza labelul
  #pentru a se schimba afisasul labelului initial vid
  done_button = Button(right_panel, text = "Done", command = execute_test)
  done_button.grid(pady = 20, padx = 20)

root = Tk()

root.title("NIST security-validator")

#setting tkinter window size
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
print("Screen width:", width)
print("Screen height:", height)

width = width - 60
height = height - 70

root.geometry('%dx%d+0+0' % (width,height))

label = Label(root, text="From the left panel, choose which test do you want to execute!", font=("Calibri", 16), bg="beige")
label.grid(sticky = "n")
label.place(relx = 0.32, rely = 0.05)

# creez un frame in partea stanga de culoare bej unde voi amplasa butoanele
left_panel = Frame(root, bg="beige", width = 500, height=1100)
#stikcy pe nord sud west, adica tocmai in partea stanga.
left_panel.grid(padx=0, pady=20, sticky="nsw")

center_panel = Frame(root, bg="white", width=300, height=300)
center_panel.grid(row=1, column=1, sticky="n")
center_panel.place(anchor="center", relx=0.5, rely=0.55)


# Încarc și afișez imaginea în frame-ul central
# deschid imaginea cu ajutorul modulului PIL, image
image = Image.open("img.jpg")
image = image.resize((650, 550))
# creez imaginea intr-un format pe care tkinter il poate afisa, cu ImageTk
# # insa tkinter neputand manipula imaginea direct, o convertesc cu clasa PhotoImage.
photo_tkinter = ImageTk.PhotoImage(image)
photo_label = Label(center_panel, image = photo_tkinter)
photo_label.grid(pady  = 0)

image = Image.open("buton_1.png")
image = image.resize((190, 70))
photo_1 = ImageTk.PhotoImage(image)
button_1 = Button(left_panel, image = photo_1, border = 0, bg="beige", borderwidth=0, activebackground="white", command = click_monobit_test)
button_1.grid(pady = 76)

image = Image.open("buton_2.png")
image = image.resize((190, 80))
photo_2 = ImageTk.PhotoImage(image)
button_2 = Button(left_panel, image = photo_2, border = 0, bg="beige", activebackground="white", command = click_mbit_test)
button_2.grid(pady = 76, padx = 10)

image = Image.open("buton_3.png")
image = image.resize((190, 80))
photo_3 = ImageTk.PhotoImage(image)
button_3 = Button(left_panel, image = photo_3, border = 0, bg="beige", activebackground="white", command = click_autocorelation)
button_3.grid(pady = 76)

image = Image.open("buton_4.png")
image = image.resize((190, 80))
photo_4 = ImageTk.PhotoImage(image)
button_4 = Button(left_panel, image = photo_4, border = 0, bg="beige", activebackground="white", command = click_serial)
button_4.grid(pady = 76)

right_panel = Frame(root, bg = "beige", width=200)
right_panel.grid(sticky="nse", row = 0, column = 1, padx=20, pady=20)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.mainloop()