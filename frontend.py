import tkinter # conda install -c anaconda tk


def connexion():
    window = tkinter.Tk()
    window.title("Connexion")
    screen_x = 840
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels
    label_connexion = tkinter.Label(window, text="Connexion", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_connexion.place(relx=0.5, rely=0.3)

    label_identifier = tkinter.Label(window, text="Identifier", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_identifier.place(relx=0.3, rely=0.4)
    entry_identifier = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_identifier.place(relx=0.5, rely=0.4)

    label_password = tkinter.Label(window, text="Password", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_password.place(relx=0.3, rely=0.5)
    entry_password = tkinter.Entry(window, font=("helvetica", 15, "bold"), show="*", bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_password.place(relx=0.5, rely=0.5)

    #Button
    button =tkinter.Button(window, text="Connect", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button.place(relx=0.6, rely=0.6)

    window.mainloop()

def create_account():
    window = tkinter.Tk()
    window.title("Create new account")
    screen_x = 840
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels
    label_connexion = tkinter.Label(window, text="Registration", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_connexion.place(relx=0.4, rely=0.1)

    label_user = tkinter.Label(window, text="Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_user.place(relx=0.25, rely=0.2)
    entry_user = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_user.place(relx=0.5, rely=0.2)

    label_identifier = tkinter.Label(window, text="Identifier", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_identifier.place(relx=0.25, rely=0.3)
    entry_identifier = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_identifier.place(relx=0.5, rely=0.3)

    label_password = tkinter.Label(window, text="Password", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_password.place(relx=0.25, rely=0.4)
    entry_password = tkinter.Entry(window, font=("helvetica", 15, "bold"),  show="*", bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_password.place(relx=0.5, rely=0.4)

    label_conf_password = tkinter.Label(window, text="Confirm password", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_conf_password.place(relx=0.25, rely=0.5)
    entry_conf_password = tkinter.Entry(window, font=("helvetica", 15, "bold"),  show="*", bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_conf_password.place(relx=0.5, rely=0.5)

    label_category = tkinter.Label(window, text="Category", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_category.place(relx=0.25, rely=0.6)
    entry_category = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_category.place(relx=0.5, rely=0.6)

    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) # command=signup
    button_back.place(relx=0.2, rely=0.8)
    #Button
    button =tkinter.Button(window, text="Connect", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button.place(relx=0.65, rely=0.8)

    window.mainloop()

def manage_checkout():
    window = tkinter.Tk()
    window.title("Manage Chekout")
    screen_x = 1100
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels and entry
    label_choose = tkinter.Label(window, text="Choose articles", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_choose.place(relx=0.3, rely=0.1)

    label_article_name = tkinter.Label(window, text="Product Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_article_name.place(relx=0.05, rely=0.2)
    entry_article_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_article_name.place(relx=0.2, rely=0.2)

    label_quantity = tkinter.Label(window, text="Quantity", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_quantity.place(relx=0.05, rely=0.27)
    entry_quantity = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_quantity.place(relx=0.2, rely=0.27)

    label_client_name = tkinter.Label(window, text="Client Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_client_name.place(relx=0.05, rely=0.5)
    entry_client_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_client_name.place(relx=0.2, rely=0.5)

    label_product_desc = tkinter.Label(window, text="Products Description", font=("helvetica", 15, "bold"), fg="black", borderwidth=5)
    label_product_desc.place(relx=0.7, rely=0.17)
    entry_product_desc = tkinter.Label(window, font=("helvetica", 15, "bold"), width=50, heigh=15, bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_product_desc.place(relx=0.5, rely=0.23)


    #Button ADD
    button_add =tkinter.Button(window, text="ADD", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button_add.place(relx=0.35, rely=0.32)

    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) # command=signup
    button_back.place(relx=0.1, rely=0.8)

    #Button
    button =tkinter.Button(window, text="Validate", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button.place(relx=0.8, rely=0.8)

    window.mainloop()

def manage_product_and_client():
    window = tkinter.Tk()
    window.title("Product and Client manager")
    screen_x = 840
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels
    label_connexion = tkinter.Label(window, text="Search Product or Client", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_connexion.place(relx=0.4, rely=0.1)

    label_product = tkinter.Label(window, text="Search Product", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_product.place(relx=0.25, rely=0.2)
    entry_product = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_product.place(relx=0.5, rely=0.2)
    button_product =tkinter.Button(window, text="Search", font=("helvetica", 10, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white") # command=signup
    button_product.place(relx=0.75, rely=0.2)

    label_client = tkinter.Label(window, text="Search Client", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_client.place(relx=0.25, rely=0.3)
    entry_client = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_client.place(relx=0.5, rely=0.3)
    button_client =tkinter.Button(window, text="Search", font=("helvetica", 10, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white") # command=signup
    button_client.place(relx=0.75, rely=0.3)


    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) # command=signup
    button_back.place(relx=0.2, rely=0.5)

    window.mainloop()


def search_or_add_product():
    window = tkinter.Tk()
    window.title("Search or Add new product")
    screen_x = 640
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels and entry
    label_choose = tkinter.Label(window, text="Modify or Add new", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_choose.place(relx=0.25, rely=0.1)

    label_article_name = tkinter.Label(window, text="Product Name", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_article_name.place(relx=0.1, rely=0.2)
    entry_article_name = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_article_name.place(relx=0.45, rely=0.2)

    label_stock_quantity = tkinter.Label(window, text="Quantity", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_stock_quantity.place(relx=0.1, rely=0.27)
    entry_stock_quantity = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_stock_quantity.place(relx=0.45, rely=0.27)

    label_unit_purchase_price = tkinter.Label(window, text="Unit purchase price", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_unit_purchase_price.place(relx=0.1, rely=0.34)
    entry_unit_purchase_price = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_unit_purchase_price.place(relx=0.45, rely=0.34)

    label_unit_sels_price = tkinter.Label(window, text="Unit sels price", font=("helvetica", 15, "bold"), bg="white", fg="black", borderwidth=5)
    label_unit_sels_price.place(relx=0.1, rely=0.41)
    entry_unit_sels_price = tkinter.Entry(window, font=("helvetica", 15, "bold"), bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_unit_sels_price.place(relx=0.45, rely=0.41)


    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) # command=signup
    button_back.place(relx=0.05, rely=0.8)

    #Button
    button =tkinter.Button(window, text="Add or Update", font=("Times New Roman", 15, "bold"), bg="#4160fd", fg='white',
                    activebackground="#2894FF", activeforeground="white", borderwidth=2) # command=signup
    button.place(relx=0.6, rely=0.8)

    window.mainloop()

def diplay_client_purchase():
    window = tkinter.Tk()
    window.title("Product and Client manager")
    screen_x = 840
    screen_y = 620
    pos_x = int(window.winfo_screenwidth())//2 - screen_x//2
    pos_y = int(window.winfo_screenheight())//2 - screen_y//2
    win_size = "{}x{}+{}+{}".format(screen_x, screen_y, pos_x, pos_y)
    window.geometry(win_size)
    #labels
    label_client_purchase = tkinter.Label(window, text="Client Purchases", font=("helvetica", 15, "bold"),  fg="#003D79", borderwidth=5)
    label_client_purchase.place(relx=0.4, rely=0.1)
    entry_client_purchase = tkinter.Label(window, font=("helvetica", 15, "bold"), width=70, heigh=20, bg="#ECF5FF", fg="#003D79", borderwidth=2)
    entry_client_purchase.place(relx=0.07, rely=0.2)
    
    #Button Back
    button_back =tkinter.Button(window, text="Back", font=("Times New Roman", 15, "bold"), bg="#BB5E00", fg='white',
                    activebackground="#EA7500", activeforeground="white", borderwidth=2) # command=signup
    button_back.place(relx=0.1, rely=0.8)

    window.mainloop()






#connexion()
#create_account()
manage_checkout()
#manage_product_and_client()
#search_or_add_product()
#diplay_client_purchase()






