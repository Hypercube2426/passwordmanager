from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50 )
#---------------------------canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#---------------------------labels

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:" )
website_label.grid(column=0, row=1 )
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)


#--------------------------entries
website_entry = Entry(width=35)
website_entry.grid(row=1 , column=1 , columnspan=2 )
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2 , column=1, columnspan=2  )
email_entry.insert(0,"dhruvbhasin0007@gmail.com")


password_entry = Entry(width=35 )
password_entry.grid(row=3 , column=1 ,columnspan=2 )

#--------------------------buttons
generate_button_button = Button(text="Generate password" ,width=12)
generate_button_button.grid(row=3 , column=2)

add_button = Button(text="Add" ,width=32 , borderwidth=1)
add_button.grid(row=4 , column=1, columnspan=2 )







window.mainloop()