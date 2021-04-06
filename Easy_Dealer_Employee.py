from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from ttkthemes import themed_tk as tk
from PyQt5 import QtWidgets
import os
import mysql.connector
from tkinter import messagebox
import Login_Page

directory_path = os.path.dirname(__file__)

class Employee:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        start_width = int((screen_width - 1280) / 2)
        start_height = int((screen_height - 720) / 2)
        self.root.title('Easy Dealer')
        self.root.iconbitmap(directory_path + '/images/logo.ico')
        self.root.geometry(f'1280x720+{start_width}+{start_height - 30}')
        self.root.resizable(False, False)
        self.root.config(bg='#1F2026')

        def dashboard_button_clicked():
            self.dashboard_button.config(bg='#3C3F4A')
            self.show_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            try:
                db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                my_cursor = db.cursor()
                query = f'SELECT Full_Name FROM user_table WHERE UserName = "{self.username}"'
                my_cursor.execute(query)
                fullname = my_cursor.fetchone()[0]
            except Exception as e:
                print(e)

            dashboard_bg_label = Label(self.content_frame, image=self.dashboard_bg_image)
            dashboard_bg_label.place(x=-2, y=-2)

            welcome_label = Label(self.content_frame, text='WELCOME,', font=('Arial Rounded MT', 13, 'bold'), bg='#292B37', fg='white')
            welcome_label.place(x=21, y=14)

            name_label = Label(self.content_frame, text=fullname, anchor='w', width=25, font=('Arial Rounded MT', 13, 'bold'), bg='#292B37', fg='#BBBBBB')
            name_label.place(x=118, y=14)

            recent_sells_label = Label(self.content_frame, text='Recent sells,', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            recent_sells_label.place(x=21, y=65)

            try:
                db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                my_cursor = db.cursor()
                query = f'SELECT * FROM sell ORDER BY Sell_ID DESC LIMIT 3'
                my_cursor.execute(query)
                sell_details = my_cursor.fetchall()
                # sell_details = []

                if len(sell_details) >= 1:
                    customer_id = sell_details[0][1]
                    product_name = sell_details[0][5]
                    selling_price = sell_details[0][3]
                    date_of_sell = sell_details[0][4]

                    query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                    my_cursor.execute(query)
                    customer_name = my_cursor.fetchone()[0]

                    customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w', width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    customer_name_label.place(x=45, y=309)

                    product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w', width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    product_name_label.place(x=45, y=334)

                    selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w', width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_price_label.place(x=45, y=359)

                    selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w', width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_date_label.place(x=45, y=384)

                else:
                    self.no_content = Label(self.content_frame, text=f'No contents available to show..', font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    self.no_content.place(x=90, y=340)

                if len(sell_details) >= 2:
                    customer_id = sell_details[1][1]
                    product_name = sell_details[1][5]
                    selling_price = sell_details[1][3]
                    date_of_sell = sell_details[1][4]

                    query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                    my_cursor.execute(query)
                    customer_name = my_cursor.fetchone()[0]

                    customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    customer_name_label.place(x=423, y=179)

                    product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    product_name_label.place(x=423, y=204)

                    selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_price_label.place(x=423, y=229)

                    selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_date_label.place(x=423, y=254)

                else:
                    self.no_content = Label(self.content_frame, text=f'No contents available to show..', font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    self.no_content.place(x=550, y=210)

                if len(sell_details) >= 3:
                    customer_id = sell_details[2][1]
                    product_name = sell_details[2][5]
                    selling_price = sell_details[2][3]
                    date_of_sell = sell_details[2][4]

                    query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                    my_cursor.execute(query)
                    customer_name = my_cursor.fetchone()[0]

                    customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    customer_name_label.place(x=423, y=440)

                    product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    product_name_label.place(x=423, y=465)

                    selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_price_label.place(x=423, y=490)

                    selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w', width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    selling_date_label.place(x=423, y=515)

                else:
                    self.no_content = Label(self.content_frame, text=f'No contents available to show..', font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                    self.no_content.place(x=550, y=470)

            except Exception as e:
                print(e)

        def show_products_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#3C3F4A')
            self.sales_button.config(bg='#292B37')


            for widget in self.content_frame.winfo_children():
                widget.destroy()

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            def bound_to_mousewheel(event):
                showall_canvas.bind_all("<MouseWheel>", on_mousewheel)

            def unbound_to_mousewheel(event):
                showall_canvas.unbind_all("<MouseWheel>")

            def on_mousewheel(event):
                showall_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

            temp_frame = Frame(self.content_frame, width=960, height=514, bg='#292B37', border=None)
            temp_frame.place(x=2, y=115)

            showall_canvas = Canvas(temp_frame, width=960, height=514, bg='#292B37')

            vertical_bar = ttk.Scrollbar(temp_frame, orient='vertical', command=showall_canvas.yview)
            vertical_bar.pack(side=RIGHT, fill='y')

            showall_canvas.config(yscrollcommand=vertical_bar.set)

            final_frame = Frame(temp_frame, width=960, height=514, bg='#292B37')
            showall_canvas.create_window((0, 0), window=final_frame, anchor='nw')
            showall_canvas.bind('<Configure>', lambda e: showall_canvas.configure(scrollregion=showall_canvas.bbox('all')))

            final_frame.bind('<Enter>', bound_to_mousewheel)
            final_frame.bind('<Leave>', unbound_to_mousewheel)

            border_hide_frame1 = Frame(self.content_frame, bg='#292B37', height=7, width=958)
            border_hide_frame1.place(x=6, y=111)

            border_hide_frame2 = Frame(self.content_frame, bg='#292B37', height=638, width=7)
            border_hide_frame2.place(x=-1, y=111)

            border_hide_frame3 = Frame(self.content_frame, bg='#292B37', height=519, width=7)
            border_hide_frame3.place(x=959, y=112)

            showall_canvas.config(yscrollcommand=vertical_bar.set)
            showall_canvas.pack(side=LEFT, expand=True, fill=BOTH)

            show_product_bg_frame = Frame(self.content_frame,  bg='#292B37', height=107, width=958)
            show_product_bg_frame.place(x=2, y=9)

            show_employees_title_label = Label(show_product_bg_frame, image=self.show_employees_title_image, bg='#292B37')
            show_employees_title_label.place(x=-2, y=-2)

            show_product_label = Label(show_product_bg_frame, text='SHOW PRODUCT INFORMATION', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            show_product_label.place(x=50, y=40)

            try:

                db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                my_cursor = db.cursor()
                query = f'SELECT * FROM product;'
                my_cursor.execute(query)
                products = my_cursor.fetchall()

                for i in range(len(products)):
                    employee_frame = Frame(final_frame, bg='#292B37', height=340, width=958)

                    employee_frame_bg_label = Label(employee_frame, image=self.show_employee_bg_image, bg='#292B37')
                    employee_frame_bg_label.place(x=-2, y=-2)

                    product_name_label = Label(employee_frame, text=products[i][1], font=('Arial Rounded MT', 17, 'bold'), bg='#292B37', fg='white')
                    product_name_label.place(x=90, y=68)

                    product_price_label = Label(employee_frame, text='$ ' + str(products[i][3]), font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='white')
                    product_price_label.place(x=90, y=101)

                    product_id_label = Label(employee_frame, text=f'Product ID                 :     {products[i][0]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    product_id_label.place(x=90, y=153)

                    product_category_label = Label(employee_frame, text=f'Category                    :     {products[i][2]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    product_category_label.place(x=90, y=201)

                    dop_label = Label(employee_frame, text=f'Date of purchase      :     {products[i][4]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    dop_label.place(x=90, y=249)

                    employee_frame.pack()
            except Exception as e:
                print(e)

        def sales_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#3C3F4A')

            def sale():

                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass
                product_name = product_name_entry.get()
                product_id = product_id_entry.get()
                selling_price = selling_price_entry.get()
                product_category = product_category_entry.get()
                dos = dos_entry.get()

                customer_name = customer_name_entry.get()
                phone = phone_entry.get()
                email = email_entry.get()
                address = address_entry.get()

                if product_name == '' or product_id == '' or selling_price == '' or product_category == '' or dos == '' or customer_name == '' or phone == '' or email == '' or address == '':
                    alert_label.config(text='Fill up all the fields..', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM product WHERE Product_ID = "{product_id}"'
                        my_cursor.execute(query)
                        product = my_cursor.fetchall()

                        if len(product) == 0:
                            alert_label.config(text='Oops! Product not available', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:
                            query = f'SELECT * FROM customer WHERE Phone_Number = "{phone}"'
                            my_cursor.execute(query)
                            customer = my_cursor.fetchall()

                            if len(customer) == 0:
                                query = f'INSERT INTO customer (Full_Name, Email, Phone_Number, Address) VALUE ("{customer_name}", "{email}", "{phone}", "{address}");'
                                my_cursor.execute(query)
                                db.commit()

                                query = f'SELECT Customer_ID FROM customer WHERE Phone_Number = "{phone}";'
                                my_cursor.execute(query)
                                customer_id = my_cursor.fetchall()[0][0]

                                query = f'SELECT Price FROM product WHERE Product_ID = "{product_id}";'
                                my_cursor.execute(query)
                                purchase_price = my_cursor.fetchone()[0]

                                query = f'INSERT INTO Sell (Customer_ID, Product_ID, Product_Name, Product_Category, Purchase_Price, Selling_Price, DOS) Value ({int(customer_id)}, "{product_id}", "{product_name}", "{product_category}", {float(purchase_price)}, {float(selling_price)}, "{dos}");'
                                my_cursor.execute(query)
                                db.commit()

                                query = f'DELETE FROM product WHERE Product_ID = "{product_id}"'
                                my_cursor.execute(query)
                                db.commit()

                                alert_label.config(text='Product has been sold..', bg='#2FA422', fg='white')
                                self.content_frame.after(1500, disappear_alert_label)

                            else:
                                query = f'UPDATE customer SET Full_Name = "{customer_name}", Email= "{email}", Address="{address}" WHERE Phone_Number = "{phone}";'
                                my_cursor.execute(query)
                                db.commit()

                                query = f'SELECT Customer_ID FROM customer WHERE Phone_Number = "{phone}";'
                                my_cursor.execute(query)
                                customer_id = my_cursor.fetchall()[0][0]

                                query = f'SELECT Price FROM product WHERE Product_ID = "{product_id}";'
                                my_cursor.execute(query)
                                purchase_price = my_cursor.fetchone()[0]

                                query = f'INSERT INTO Sell (Customer_ID, Product_ID, Product_Name, Product_Category, Purchase_Price, Selling_Price, DOS) Value ({int(customer_id)}, "{product_id}", "{product_name}", "{product_category}", {float(purchase_price)}, {float(selling_price)}, "{dos}");'
                                my_cursor.execute(query)
                                db.commit()

                                query = f'DELETE FROM product WHERE Product_ID = "{product_id}"'
                                my_cursor.execute(query)
                                db.commit()
                                alert_label.config(text='Product has been sold..', bg='#2FA422', fg='white')
                                self.content_frame.after(1500, disappear_alert_label)

                            product_id_entry.delete(0, 'end')
                            product_name_entry.delete(0, 'end')
                            selling_price_entry.delete(0, 'end')
                            product_category_entry.delete(0, 'end')
                            dos_entry.delete(0, 'end')
                            customer_name_entry.delete(0, 'end')
                            phone_entry.delete(0, 'end')
                            email_entry.delete(0, 'end')
                            address_entry.delete(0, 'end')

                    except Exception as e:
                        alert_label.config(text='Oops! Something went wrong..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)


            def search():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass
                searched_product_id = product_id_entry.get()
                if searched_product_id == '':
                    alert_label.config(text='Enter a product id..', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM product WHERE Product_ID = "{searched_product_id}"'
                        my_cursor.execute(query)
                        product = my_cursor.fetchall()

                        if len(product) == 0:
                            product_name_entry.delete(0, 'end')
                            product_category_entry.delete(0, 'end')

                            alert_label.config(text='Oops! Product not available', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:

                            product_name_entry.delete(0, 'end')
                            product_category_entry.delete(0, 'end')

                            product_name_entry.insert(0, product[0][1])
                            product_category_entry.insert(0, product[0][2])

                    except Exception as e:
                        alert_label.config(text='Sorry! Unable to load data..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            sales_bg_label = Label(self.content_frame, image=self.sales_bg_image)
            sales_bg_label.place(x=-2, y=-2)

            sales_label = Label(self.content_frame, text='SALES', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            sales_label.place(x=50, y=40)

            product_details_label = Label(self.content_frame, text='PRODUCT DETAILS', font=('Arial Rounded MT', 12, 'bold'), bg='#333646', fg='#BBBBBB')
            product_details_label.place(x=65, y=101)

            product_id_label = Label(self.content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            product_id_label.place(x=96, y=145)

            product_name_label = Label(self.content_frame, text='Product Name', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            product_name_label.place(x=96, y=182)

            selling_price_label = Label(self.content_frame, text='Selling Price', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            selling_price_label.place(x=96, y=220)

            product_category_label = Label(self.content_frame, text='Product Category', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            product_category_label.place(x=96, y=257)

            dos_label = Label(self.content_frame, text='Date Of Sell', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            dos_label.place(x=96, y=294)

            customer_details_label = Label(self.content_frame, text='CUSTOMER DETAILS', font=('Arial Rounded MT', 12, 'bold'), bg='#333646', fg='#BBBBBB')
            customer_details_label.place(x=65, y=345)

            customer_name_label = Label(self.content_frame, text='Customer Name', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            customer_name_label.place(x=96, y=388)

            phone_label = Label(self.content_frame, text='Phone Number', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            phone_label.place(x=96, y=425)

            email_label = Label(self.content_frame, text='E-mail', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            email_label.place(x=96, y=462)

            address_label = Label(self.content_frame, text='Address', font=('Arial Rounded MT', 11, 'bold'), bg='#333646', fg='white')
            address_label.place(x=96, y=499)

            product_id_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            product_id_entry.place(x=247, y=150)

            product_name_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            product_name_entry.place(x=247, y=186)

            selling_price_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            selling_price_entry.place(x=247, y=222)

            product_category_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            product_category_entry.place(x=247, y=258)

            dos_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            dos_entry.place(x=247, y=294)

            customer_name_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            customer_name_entry.place(x=247, y=391)

            phone_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            phone_entry.place(x=247, y=427)

            email_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            email_entry.place(x=247, y=463)

            address_entry = Entry(self.content_frame, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white', borderwidth=0, width=56)
            address_entry.place(x=247, y=499)

            search_button = Button(self.content_frame, cursor='hand2', image=self.search_button_icon_image, borderwidth=0, activebackground='#686972', bg='#686972', command=search)
            search_button.place(x=677, y=150)

            ok_button = Button(self.content_frame, cursor='hand2', image=self.ok_button_image, borderwidth=0, activebackground='#292B37', bg='#292B37', command=sale)
            ok_button.place(x=675, y=565)

            alert_label = Label(self.content_frame, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=90, y=565)

        def logout():
            user_response = messagebox.askyesno('Confirm Logout', 'Do you really want to logout ?')

            if user_response:
                try:
                    self.Login_Page = QtWidgets.QMainWindow()
                    self.ui = Login_Page.Ui_Login_Window()
                    self.ui.setupUi(self.Login_Page)
                    self.root.destroy()
                    self.Login_Page.show()
                except Exception as e:
                    print(e)
            else:
                pass

        def profile():
            def edit():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass
                def save():
                    name = fullname_entry.get()
                    password = password_entry.get()
                    phone = phone_entry.get()
                    email = email_entry.get()
                    address = address_entry.get()
                    dob = dob_entry.get()

                    if name == '' or password == '' or phone == '' or email == '' or address == '' or dob == '':
                        alert_label.config(text='Fill up all the fields..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                    else:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                            my_cursor = db.cursor()
                            query = f'UPDATE user_table SET Full_Name="{name}", User_Password="{password}", Phone_Number="{phone}", Email="{email}", Address="{address}", DOB="{dob}" WHERE UserName="{self.username}";'
                            my_cursor.execute(query)
                            db.commit()

                            for widget in prof.winfo_children():
                                widget.destroy()

                            profile_content()

                        except Exception as e:
                            alert_label.config(text='Sorry! Unable to edit..', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)

                for widget in prof.winfo_children():
                    widget.destroy()
                edit_profile_bg_label = Label(prof, image=self.edit_profile_bg_image)
                edit_profile_bg_label.place(x=-2, y=-2)

                edit_profile_label = Label(prof, text='EDIT PROFILE', font=('Arial Rounded MT', 12, 'bold'), bg='#292B37', fg='#BBBBBB')
                edit_profile_label.place(x=40, y=40)

                fullname_label = Label(prof, text=f'Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                fullname_label.place(x=72, y=110)

                password_label = Label(prof, text=f'Password', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                password_label.place(x=72, y=159)

                phone_label = Label(prof, text=f'Phone Number', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                phone_label.place(x=72, y=207)

                email_label = Label(prof, text=f'E-mail', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                email_label.place(x=72, y=255)

                address_label = Label(prof, text=f'Address', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                address_label.place(x=72, y=303)

                dob_label = Label(prof, text=f'Date of birth', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                dob_label.place(x=72, y=352)

                fullname_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                fullname_entry.place(x=198, y=110)

                password_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                password_entry.place(x=198, y=159)

                phone_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                phone_entry.place(x=198, y=207)

                email_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                email_entry.place(x=198, y=255)

                address_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                address_entry.place(x=198, y=303)

                dob_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0, width=40)
                dob_entry.place(x=198, y=352)

                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                    my_cursor = db.cursor()
                    query = f'SELECT * FROM user_table WHERE UserName = "{self.username}"'
                    my_cursor.execute(query)
                    user_details = my_cursor.fetchall()

                    fullname_entry.insert(0, user_details[0][0])
                    password_entry.insert(0, user_details[0][7])
                    phone_entry.insert(0, user_details[0][2])
                    email_entry.insert(0, user_details[0][1])
                    address_entry.insert(0, user_details[0][3])
                    dob_entry.insert(0, user_details[0][4])

                except Exception as e:
                    print(e)

                save_button = Button(prof, cursor='hand2', image=self.save_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=save)
                save_button.place(x=482, y=441)

                cancel_button = Button(prof, cursor='hand2', image=self.cancel_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=profile_content)
                cancel_button.place(x=387, y=441)

                alert_label = Label(prof, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
                alert_label.place(x=40, y=435)

            def profile_content():
                for widget in prof.winfo_children():
                    widget.destroy()
                try:
                    db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                    my_cursor = db.cursor()
                    query = f'SELECT * FROM user_table WHERE UserName = "{self.username}"'
                    my_cursor.execute(query)
                    user_details = my_cursor.fetchall()

                    profile_label = Label(prof, text='PROFILE', font=('Arial Rounded MT', 12, 'bold'), bg='#292B37', fg='#BBBBBB')
                    profile_label.place(x=50, y=48)

                    name_label = Label(prof, text=user_details[0][0], font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='white')
                    name_label.place(x=76, y=109)

                    designation_label = Label(prof, text=user_details[0][5], font=('Arial Rounded MT', 12, 'bold'), bg='#292B37', fg='white')
                    designation_label.place(x=76, y=150)

                    username_label = Label(prof, text=f'Username                 {user_details[0][6]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    username_label.place(x=76, y=231)

                    phone_label = Label(prof, text=f'Phone Number        {user_details[0][2]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    phone_label.place(x=76, y=269)

                    email_label = Label(prof, text=f'E-mail                        {user_details[0][1]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    email_label.place(x=76, y=307)

                    address_label = Label(prof, text=f'Address                    {user_details[0][3]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    address_label.place(x=76, y=345)

                    dob_label = Label(prof, text=f'Date of birth             {user_details[0][4]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    dob_label.place(x=76, y=384)

                    edit_button = Button(prof, cursor='hand2', image=self.edit_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=edit)
                    edit_button.place(x=450, y=45)
                except Exception as e:
                    print(e)

            prof = Toplevel()
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            start_width = int((screen_width - 600) / 2)
            start_height = int((screen_height - 500) / 2)
            prof.title('User Profile')
            prof.iconbitmap(directory_path + '/images/logo.ico')
            prof.geometry(f'600x500+{start_width}+{start_height - 30}')
            prof.resizable(False, False)
            prof.config(bg='#292B37')

            profile_content()


        self.main_background_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/main_bg.png'))
        self.dashboard_logo_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/dashboard_logo.png'))
        self.dashboard_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/dashboard_bg.png'))
        self.notification_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/notification_img.png'))
        self.user_icon_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/user_icon.png'))
        self.logout_icon_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/logout_img.png'))
        self.show_employees_title_image = ImageTk.PhotoImage( Image.open(directory_path + '/images/show_employees_title_bg.png'))
        self.show_employee_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/show_employee_bg.png'))
        self.sales_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/sales_bg.png'))
        self.search_button_icon_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/search_icon.png'))
        self.ok_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/ok_button.png'))
        self.edit_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/edit_button_img.png'))
        self.edit_profile_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/owner_edit_profile_bg.png'))
        self.save_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/save_button.png'))
        self.cancel_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/cancel_button.png'))

        self.main_background_label = Label(self.root, image=self.main_background_image)
        self.main_background_label.place(x=-2, y=-2)

        try:
            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
            my_cursor = db.cursor()
            query = f'SELECT Full_Name FROM user_table WHERE UserName = "{self.username}"'
            my_cursor.execute(query)
            fullname = my_cursor.fetchone()[0]
        except Exception as e:
            print(e)

        self.profile_button = Button(self.root, cursor='hand2', image=self.user_icon_image, borderwidth=0,
                                     activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37',
                                     command=profile)
        self.profile_button.place(x=930, y=25)

        self.profile_name_label = Label(self.root, text=fullname, anchor='w', width=25,
                                        font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#BBBBBB')
        self.profile_name_label.place(x=962, y=28)

        self.logout_button = Button(self.root, cursor='hand2', image=self.logout_icon_image, borderwidth=0,
                                    activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37',
                                    command=logout)
        self.logout_button.place(x=1200, y=22)

        self.content_frame = Frame(self.root, width=980, height=630, bg='#292B37')  # bg='#292B37'
        self.content_frame.place(x=278, y=64)

        self.dashboard_bg_label = Label(self.content_frame, image=self.dashboard_bg_image)
        self.dashboard_bg_label.place(x=-2, y=-2)

        self.side_frame = Frame(self.root, width=255, height=425, bg='#292B37')  # bg='#292B37'
        self.side_frame.place(x=18, y=255)

        self.dashboard_button = Button(self.side_frame, text='DASHBOARD                 ', cursor='hand2',
                                       font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white',
                                       bg='#3C3F4A', borderwidth=0, activebackground='#333640',
                                       activeforeground='white', command=dashboard_button_clicked)
        self.dashboard_button.pack()

        self.show_products_button = Button(self.side_frame, text='SHOW PRODUCTS       ', cursor='hand2',
                                           font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white',
                                           bg='#292B37', borderwidth=0, activebackground='#333640',
                                           activeforeground='white', command=show_products_button_clicked)
        self.show_products_button.pack()



        self.sales_button = Button(self.side_frame, text='SALES                            ', cursor='hand2',
                                   font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37',
                                   borderwidth=0, activebackground='#333640', activeforeground='white',
                                   command=sales_button_clicked)
        self.sales_button.pack()



        self.welcome_label = Label(self.content_frame, text='WELCOME,', font=('Arial Rounded MT', 13, 'bold'),
                                   bg='#292B37', fg='white')
        self.welcome_label.place(x=21, y=14)

        self.name_label = Label(self.content_frame, text=fullname, anchor='w', width=25,
                                font=('Arial Rounded MT', 13, 'bold'), bg='#292B37', fg='#BBBBBB')
        self.name_label.place(x=118, y=14)

        self.recent_sells_label = Label(self.content_frame, text='Recent sells,', font=('Arial Rounded MT', 11, 'bold'),
                                        bg='#292B37', fg='white')
        self.recent_sells_label.place(x=21, y=65)

        try:

            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
            my_cursor = db.cursor()
            query = f'SELECT * FROM sell ORDER BY Sell_ID DESC LIMIT 3'
            my_cursor.execute(query)
            sell_details = my_cursor.fetchall()
            # sell_details = []

            if len(sell_details) >= 1:
                customer_id = sell_details[0][1]
                product_name = sell_details[0][5]
                selling_price = sell_details[0][3]
                date_of_sell = sell_details[0][4]

                query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                my_cursor.execute(query)
                customer_name = my_cursor.fetchone()[0]

                customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w',
                                            width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                customer_name_label.place(x=45, y=309)

                product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w',
                                           width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                product_name_label.place(x=45, y=334)

                selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w',
                                            width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_price_label.place(x=45, y=359)

                selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w',
                                           width=38, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_date_label.place(x=45, y=384)

            else:
                self.no_content = Label(self.content_frame, text=f'No contents available to show..',
                                        font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                self.no_content.place(x=90, y=340)

            if len(sell_details) >= 2:
                customer_id = sell_details[1][1]
                product_name = sell_details[1][5]
                selling_price = sell_details[1][3]
                date_of_sell = sell_details[1][4]

                query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                my_cursor.execute(query)
                customer_name = my_cursor.fetchone()[0]

                customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w',
                                            width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                customer_name_label.place(x=423, y=179)

                product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w',
                                           width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                product_name_label.place(x=423, y=204)

                selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w',
                                            width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_price_label.place(x=423, y=229)

                selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w',
                                           width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_date_label.place(x=423, y=254)

            else:
                self.no_content = Label(self.content_frame, text=f'No contents available to show..',
                                        font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                self.no_content.place(x=550, y=210)

            if len(sell_details) >= 3:
                customer_id = sell_details[2][1]
                product_name = sell_details[2][5]
                selling_price = sell_details[2][3]
                date_of_sell = sell_details[2][4]

                query = f'SELECT full_name FROM customer WHERE Customer_ID = "{customer_id}"'
                my_cursor.execute(query)
                customer_name = my_cursor.fetchone()[0]

                customer_name_label = Label(self.content_frame, text=f'Customer Name: {customer_name}', anchor='w',
                                            width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                customer_name_label.place(x=423, y=440)

                product_name_label = Label(self.content_frame, text=f'Product Name: {product_name}', anchor='w',
                                           width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                product_name_label.place(x=423, y=465)

                selling_price_label = Label(self.content_frame, text=f'Selling Price: {selling_price} $', anchor='w',
                                            width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_price_label.place(x=423, y=490)

                selling_date_label = Label(self.content_frame, text=f'Selling Date: {date_of_sell}', anchor='w',
                                           width=65, font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                selling_date_label.place(x=423, y=515)

            else:
                self.no_content = Label(self.content_frame, text=f'No contents available to show..',
                                        font=('Arial Rounded MT', 10, 'bold'), bg='#333640', fg='white')
                self.no_content.place(x=550, y=470)

        except Exception as e:
            print(e)

        self.root.mainloop()


# employee = tk.ThemedTk()
# employee.get_themes()
# employee.set_theme('black')
# EDO = Employee(employee, 'nowmi022')