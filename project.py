#Main project

from tkinter import font

import mysql.connector
import string
import random
import sys
from tkinter import messagebox
from PIL import Image, ImageTk

# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="junior_college"
)



# ____________________________________________________________________________________________
# Function to save data to MySQL
def save_to_mysql():

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='college'
        )

        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        gender = gender_var.get()
        stream = stream_var.get()
        dob = dob_entry.get()
        age = age_entry.get()
        percentage = percentage_entry.get()
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for i in range(10))
        unique_no = code
        cursor = connection.cursor()

        custom_font = font.Font(family="Helvetica", size=20)
        custom2_font = font.Font(family="Helvetica", size=23)
        custom3_font = font.Font(family="Helvetica", size=16)

        if len(phone) == 10 and phone.isdigit():
            if age.isdigit():
                if email.endswith("@gmail.com"):

                    # Insert data into the admission table
                    insert_query = "INSERT INTO applicants(name, email, phone, address, gender, stream, dob, age, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    data1 = (name, email, phone, address, gender, stream, dob, age, percentage)
                    cursor.execute(insert_query, data1)
                    data2 = (name, email,phone,address, gender,stream,dob,age,percentage,unique_no)
                    connection.commit()



                    # Check eligibility
                    if float(percentage) > 75.0 :
                        admission_status.config(
                            text=f"Admitted.\n Your unique ID is {unique_no}",
                            font=custom3_font)
                        # Insert data into the admitted_stu table
                        insert_query = "INSERT INTO admitted_stu (name, email, phone, address, gender, stream, dob, age, percentage,unique_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                        cursor.execute(insert_query, data2)
                        connection.commit()

                    else:
                        # admission_status.config(text="Sorry. Not admitted.",font=custom_font)
                        import tkinter as tk

                        def display_message():
                            message_label.config(text="Sorry. You are not admitted.")

                            # Schedule the program to exit after 5 seconds
                            root.after(5000, exit_program)

                        def exit_program():
                            root.destroy()

                        # Create the main Tkinter window
                        root = tk.Tk()
                        root.title("Admission Display")

                        root.geometry("400x400")

                        # Create a label for displaying the message
                        message_label = tk.Label(root, text="")
                        message_label.pack(pady=20)

                        # Button to trigger the message display
                        display_button = tk.Button(root, text="Display", command=display_message)
                        display_button.pack(pady=10)

                        # Run the Tkinter main loop
                        root.mainloop()

                        sys.exit()


                    connection.close()
                    result_label.config(text="Data saved.", font=custom3_font)

                    frame.destroy()
                else:
                    admission_status.config(text="Kindly check the Email ID and re-enter it.")
            else:
                admission_status.config(text="Kindly check the Age and re-enter it")
        else:
            admission_status.config(text="Kindly check the phone number and re-enter it.",font=custom2_font)
    except mysql.connector.Error as err:
        # Display the error in a messagebox
        messagebox.showerror("Error", f"Error: {err}")


import tkinter as tk
from tkinter import ttk
import mysql.connector

# Create a basic GUI
root = tk.Tk()
root.title("College Admission Interface!")

frame = tk.Frame(root)
frame.pack()

image_path = "Untitled design.png"
original_image = Image.open(image_path)

resized_image = original_image.resize((700,700))
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image and set it as the background
bg_label = tk.Label(root, image=tk_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.geometry("700x700")

name_label = tk.Label(root, text="Full Name")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email (with @ prefix)")
email_entry = tk.Entry(root)

phone_label = tk.Label(root, text="Phone Number (10 Digit)")
phone_entry = tk.Entry(root)

address_label = tk.Label(root, text="Address")
address_entry = tk.Entry(root)

gender_label = tk.Label(root, text="Gender")
gender_var = tk.StringVar()
gender_var.set("Female")
gender_option = tk.OptionMenu(root, gender_var, "Female", "Male", "Other")

stream_label = tk.Label(root, text="Stream")
stream_var = tk.StringVar()
stream_var.set("Science")
stream_option = tk.OptionMenu(root, stream_var, "Science", "Commerce", "Arts")

dob_label = tk.Label(root, text="Date of Birth Format(YYYY-MM-DD)")
dob_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age INTEGER FORM")
age_entry = tk.Entry(root)

percentage_label = tk.Label(root, text="Percentage")
percentage_entry = tk.Entry(root)

save_button = tk.Button(root, text="Save", command=save_to_mysql)

result_label = tk.Label(root, text="")
admission_status = tk.Label(root, text="")

current_page = admission_status

name_label.pack()
name_entry.pack(padx = 10, pady=5)


email_label.pack()
email_entry.pack(padx = 10, pady=5)

phone_label.pack()
phone_entry.pack(padx = 10, pady=5)

address_label.pack()
address_entry.pack(padx = 10, pady=5)

gender_label.pack()
gender_option.pack(padx = 10, pady=5)

stream_label.pack()
stream_option.pack(padx = 10, pady=5)

dob_label.pack()
dob_entry.pack(padx = 10, pady=5)

age_label.pack()
age_entry.pack(padx = 10, pady=5)

percentage_label.pack()
percentage_entry.pack(padx = 10, pady=5)

save_button.pack(padx = 10, pady=5)
result_label.pack(padx = 10, pady=5)
admission_status.pack(padx = 10, pady=5)

root.mainloop()


# __________________________________________________________________________________________________


import mysql.connector
from tkinter import Tk, Label, Button

# Function to connect to the database and fetch the number of students
def get_number_of_students():

    try:
        # Update these parameters with your MySQL server details
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="college"
        )

        cursor = connection.cursor()

        # Execute the query to get the count of students
        cursor.execute('SELECT COUNT(*) FROM admitted_stu where stream = "Science"')
        result = cursor.fetchone()[0]
        cursor.execute('Select count(*) from admitted_stu where stream = "Arts"')
        result1 = cursor.fetchone()[0]
        cursor.execute('Select count(*) from admitted_stu where stream = "Commerce"')
        result2 = cursor.fetchone()[0]

        # Display the result in the Tkinter window
        result_label.config(text=f"Number of Science Students are: {result}")
        result1_label.config(text=f"Number of Art students are: {result1}")
        result2_label.config(text=f"Number of Commerce students are: {result2}")

    except mysql.connector.Error as err:
        result_label.config(text=f"Error: {err}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()


# Create the main Tkinter window
root = Tk()
root.title("Number of students in each stream.")

image_path = "Untitled design.png"
original_image = Image.open(image_path)

resized_image = original_image.resize((700,700))
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image and set it as the background
bg_label = tk.Label(root, image=tk_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.geometry("700x700")

# Create a label to display the result
result_label = Label(root, text="")
result_label.pack(pady=20)

result1_label = Label(root, text="")
result1_label.pack(pady=20)

result2_label = Label(root, text="")
result2_label.pack(pady=20)

# Create a button to trigger the query
fetch_button = Button(root, text="Fetch Number of Students", command=get_number_of_students)
fetch_button.pack(pady=40,padx =80)

# Run the Tkinter main loop
root.mainloop()

# _____________________________________________________________________________________________
import mysql.connector


def search_data():
    # Get the search term from the Entry widget
    search_term = entry_search.get()


    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='college'
        )

        cursor = connection.cursor()

        # Execute the SQL query to search for data
        query = "SELECT * FROM admitted_stu WHERE unique_no LIKE %s"
        cursor.execute(query, ('%' + search_term + '%',))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Display data in Tkinter window
        display_data(rows, columns)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def display_data(rows, columns):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("MySQL Data Display")

    # Create a Treeview widget to display data
    tree = ttk.Treeview(window, columns=columns, show="headings")

    # Add column headings
    for col in columns:
        tree.heading(col, text=col)

    # Add data rows
    for row in rows:
        tree.insert("", "end", values=row)

    # Pack the Treeview widget
    tree.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Create the main application window
root = tk.Tk()
root.title("MySQL Search with Tkinter")

image_path = "Untitled design.png"
original_image = Image.open(image_path)

resized_image = original_image.resize((700,700))
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image and set it as the background
bg_label = tk.Label(root, image=tk_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.geometry("700x700")

# Entry widget for search term
names_label = tk.Label(root, text="Record's Unique ID:")
names_label.pack()
names_entry = tk.Entry(root)

entry_search = ttk.Entry(root)
entry_search.pack(pady = 20)

# Button to trigger the search
btn_search = ttk.Button(root, text="Search", command=search_data)
btn_search.pack(pady=10)

search_status = tk.Label(root,text="")
search_status.pack()
# Start the Tkinter main event loop
root.mainloop()

# ______________________________________________________________________________________________
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def update_data():
    # Get the new values from Entry widgets
    first_input = first_input_var.get()
    second_input = second_input_var.get()
    new_some = entry_new_some.get()
    condition_value = entry_condition_value.get()

    # Display a confirmation dialog
    confirm = messagebox.askyesno("Confirmation", "Do you want to update the data?")

    if not confirm:
        return  # User canceled the operation

    # Clear the entry widgets
    entry_new_some.delete(0, tk.END)

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',

            password='password',
            database='college'
        )

        cursor = connection.cursor()

        # Update the data in the specific column
        null_update = f"update admitted_stu set {first_input} = null where {second_input}= %s"
        cursor.execute(null_update, (condition_value,))

        update_query = f"UPDATE applicants SET {first_input} = %s WHERE {second_input}= %s"
        cursor.execute(update_query, (new_some, condition_value))

        final_update = f"update admitted_stu set {first_input} = %s where {second_input} = %s"
        cursor.execute(final_update,(new_some,condition_value))

        # Commit the changes
        connection.commit()

        # Display a success message
        messagebox.showinfo("Success", "Close this page."
                                       "Search your email in the next page to know about the changes!")


    except mysql.connector.Error as err:
        # Display the error in a messagebox
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Create the main application window
root = tk.Tk()
root.title("MySQL Update with Tkinter")

image_path = "Untitled design.png"
original_image = Image.open(image_path)

resized_image = original_image.resize((700,700))
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image and set it as the background
bg_label = tk.Label(root, image=tk_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.geometry("700x700")

# Entry widgets for new data input
first_input_label = tk.Label(root, text="What you want to update?:")
first_input_var = tk.StringVar()
first_input_var.set("Name")
first_input_label.pack()
first_input_option = tk.OptionMenu(root, first_input_var,"Name","email","Phone","Address","Gender","Stream","Dob","Age")
first_input_option.pack()

new_some_label = tk.Label(root, text="New Value:")
entry_new_some = ttk.Entry(root, width=30)
new_some_label.pack()
entry_new_some.pack(pady=20, padx=20)

second_input_label = tk.Label(root, text="What value will you provide?:")
second_input_var = tk.StringVar()
second_input_var.set("Email")
second_input_label.pack()
second_input_option = tk.OptionMenu(root, second_input_var,"Email", "Phone")
second_input_option.pack()

condition_value_label = tk.Label(root, text="Record's info where updating:")
entry_condition_value = ttk.Entry(root, width=30)
condition_value_label.pack()
entry_condition_value.pack(pady=20, padx=20)

# Button to trigger the update
btn_update = ttk.Button(root, text="Update Data", command=update_data)
btn_update.pack(pady=10)
# Start the Tkinter main event loop
root.mainloop()
# ________________________________________________________________________
def search_data():
    # Get the search term from the Entry widget
    search_term = entry_search.get()


    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='college'
        )

        cursor = connection.cursor()

        # Execute the SQL query to search for data
        query = "SELECT * FROM admitted_stu WHERE unique_no LIKE %s"
        cursor.execute(query, ('%' + search_term + '%',))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Display data in Tkinter window
        display_data(rows, columns)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def display_data(rows, columns):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("MySQL Data Display")

    # Create a Treeview widget to display data
    tree = ttk.Treeview(window, columns=columns, show="headings")

    # Add column headings
    for col in columns:
        tree.heading(col, text=col)

    # Add data rows
    for row in rows:
        tree.insert("", "end", values=row)

    # Pack the Treeview widget
    tree.pack()

    # Start the Tkinter event loop
    window.mainloop()



# Create the main application window
root = tk.Tk()
root.title("MySQL Search with Tkinter")

image_path = "Untitled design.png"
original_image = Image.open(image_path)

resized_image = original_image.resize((700,700))
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label with the image and set it as the background
bg_label = tk.Label(root, image=tk_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.geometry("700x700")

# Entry widget for search term
names_label = tk.Label(root, text="Record's Unique ID:")
names_label.pack()
names_entry = tk.Entry(root)

entry_search = ttk.Entry(root)
entry_search.pack(pady = 20)

# Button to trigger the search
btn_search = ttk.Button(root, text="Search", command=search_data)
btn_search.pack(pady=10)


search_status = tk.Label(root,text="")
search_status.pack()

# Start the Tkinter main event loop
root.mainloop()
