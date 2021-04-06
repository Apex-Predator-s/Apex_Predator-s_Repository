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


class Owner:
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

        def bound_to_mousewheel(event):
            showall_canvas.bind_all("<MouseWheel>", on_mousewheel)

        def unbound_to_mousewheel(event):
            showall_canvas.unbind_all("<MouseWheel>")

        def on_mousewheel(event):
            showall_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def dashboard_button_clicked():
            self.dashboard_button.config(bg='#3C3F4A')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

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
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

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

            show_employees_bg_label = Label(show_product_bg_frame, image=self.show_employees_bg_image, bg='#292B37')
            show_employees_bg_label.place(x=-2, y=-2)

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

        def add_products_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#3C3F4A')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

            def add():

                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass
                product_name = product_name_edit.get()
                product_id = product_id_edit.get()
                purchase_price = purchase_price_edit.get()
                product_category = product_category_edit.get()
                dop = dop_edit.get()

                if product_name == '' or product_id == '' or purchase_price == '' or product_category == '' or dop == '':
                    alert_label.config(text='Fill up all the fields', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'INSERT INTO Product VALUES ("{product_id}", "{product_name}", "{product_category}", {purchase_price}, "{dop}");'
                        my_cursor.execute(query)
                        db.commit()
                        db.close()
                        alert_label.config(text='Product has been added successfully..', bg='#2FA422', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                        product_name_edit.delete(0, 'end')
                        product_id_edit.delete(0, 'end')
                        purchase_price_edit.delete(0, 'end')
                        product_category_edit.delete(0, 'end')
                        dop_edit.delete(0, 'end')

                    except Exception as e:
                        alert_label.config(text='Sorry! Invalid input..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            self.add_products_bg_label = Label(self.content_frame, image=self.add_products_bg_image)
            self.add_products_bg_label.place(x=-2, y=-2)

            add_product_label = Label(self.content_frame, text='ADD PRODUCT', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            add_product_label.place(x=50, y=50)

            product_name_label = Label(self.content_frame, text='Product Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            product_name_label.place(x=106, y=184)

            product_id_label = Label(self.content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            product_id_label.place(x=106, y=240)

            purchase_price_label = Label(self.content_frame, text='Purchase Price', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            purchase_price_label.place(x=106, y=307)

            product_category_label = Label(self.content_frame, text='Product Category', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            product_category_label.place(x=106, y=369)

            dop_label = Label(self.content_frame, text='Date Of Purchase', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            dop_label.place(x=106, y=432)

            product_name_edit = Entry(self.content_frame, text='Product Name', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            product_name_edit.place(x=281, y=184)

            product_id_edit = Entry(self.content_frame, text='Product ID', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            product_id_edit.place(x=281, y=245)

            purchase_price_edit = Entry(self.content_frame, text='Purchase Price', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            purchase_price_edit.place(x=281, y=307)

            product_category_edit = Entry(self.content_frame, text='Product Category', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            product_category_edit.place(x=281, y=369)

            dop_edit = Entry(self.content_frame, text='Date Of Purchase', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            dop_edit.place(x=281, y=432)

            add_product_button = Button(self.content_frame, cursor='hand2', image=self.add_products_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=add)
            add_product_button.place(x=722, y=523)

            alert_label = Label(self.content_frame, width=30, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=106, y=523)

            product_name_edit.delete(0, 'end')
            product_id_edit.delete(0, 'end')
            purchase_price_edit.delete(0, 'end')
            product_category_edit.delete(0, 'end')
            dop_edit.delete(0, 'end')

        def update_products_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#3C3F4A')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

            def search():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass

                def update():
                    product_name = product_name_edit.get()
                    product_id = product_id_edit.get()
                    purchase_price = purchase_price_edit.get()
                    product_category = product_category_edit.get()
                    dop = dop_edit.get()

                    if searched_product_id != product_id:
                        alert_label.config(text='Oops! Invalid input..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                    elif product_name == '' or product_id == '' or purchase_price == '' or product_category == '' or dop == '':
                        alert_label.config(text='Fill up all the fields', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                    else:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                            my_cursor = db.cursor()
                            query = f'UPDATE product SET Product_Name = "{product_name}", Product_Category = "{product_category}",  Price = {float(purchase_price)}, DOP = "{dop}"  WHERE Product_ID = "{searched_product_id}";'
                            my_cursor.execute(query)
                            db.commit()
                            db.close()
                            for widget in self.update_content_frame.winfo_children():
                                widget.destroy()
                            search_edit.delete(0, 'end')
                            alert_label.config(text='Successfully updated the product', bg='#2FA422', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        except Exception as e:
                            alert_label.config(text='Sorry! Unable to update', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)

                searched_product_id = search_edit.get()

                if searched_product_id == '':
                    alert_label.config(text='Enter a product ID', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    for widget in self.update_content_frame.winfo_children():
                        widget.destroy()
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM product WHERE Product_ID = "{searched_product_id}"'
                        my_cursor.execute(query)
                        product = my_cursor.fetchall()

                        if len(product) == 0:
                            alert_label.config(text='Product doesn\'t exists', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:
                            product_id = product[0][0]
                            product_name = product[0][1]
                            product_category = product[0][2]
                            purchase_price = product[0][3]
                            dop = product[0][4]

                            update_product_content_label = Label(self.update_content_frame, image=self.update_content_image, bd=0)
                            update_product_content_label.place(x=230, y=24)

                            product_name_label = Label(self.update_content_frame, text='Product Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_name_label.place(x=106, y=46)

                            product_id_label = Label(self.update_content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_id_label.place(x=106, y=111)

                            purchase_price_label = Label(self.update_content_frame, text='Purchase Price', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            purchase_price_label.place(x=106, y=177)

                            product_category_label = Label(self.update_content_frame, text='Product Category', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_category_label.place(x=106, y=243)

                            dop_label = Label(self.update_content_frame, text='Date Of Purchase', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            dop_label.place(x=106, y=309)

                            product_name_edit = Entry(self.update_content_frame, text='Product Name', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            product_name_edit.place(x=281, y=46)

                            product_id_edit = Entry(self.update_content_frame, text='Product ID', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            product_id_edit.place(x=281, y=111)

                            purchase_price_edit = Entry(self.update_content_frame, text='Purchase Price', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            purchase_price_edit.place(x=281, y=177)

                            product_category_edit = Entry(self.update_content_frame, text='Product Category', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            product_category_edit.place(x=281, y=243)

                            dop_edit = Entry(self.update_content_frame, text='Date Of Purchase', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            dop_edit.place(x=281, y=309)

                            product_name_edit.delete(0, 'end')
                            product_id_edit.delete(0, 'end')
                            purchase_price_edit.delete(0, 'end')
                            product_category_edit.delete(0, 'end')
                            dop_edit.delete(0, 'end')

                            product_name_edit.insert(0, product_name)
                            product_id_edit.insert(0, product_id)
                            purchase_price_edit.insert(0, purchase_price)
                            product_category_edit.insert(0, product_category)
                            dop_edit.insert(0, dop)

                            update_button = Button(self.update_content_frame, cursor='hand2', image=self.update_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=update)
                            update_button.place(x=723, y=370)

                    except Exception as e:
                        alert_label.config(text='Sorry! Something went wrong..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            self.update_products_bg_label = Label(self.content_frame, image=self.update_product_bg_image)
            self.update_products_bg_label.place(x=-2, y=-2)

            update_product_label = Label(self.content_frame, text='UPDATE PRODUCT', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            update_product_label.place(x=50, y=50)

            product_id_search_label = Label(self.content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            product_id_search_label.place(x=160, y=116)

            search_edit = Entry(self.content_frame, width=60, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            search_edit.place(x=270, y=116)
            search_edit.delete(0, 'end')

            search_button = Button(self.content_frame, cursor='hand2', image=self.search_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=search)
            search_button.place(x=776, y=105)

            self.update_content_frame = Frame(self.content_frame, width=980, height=470, bg='#292B37')  # bg='#292B37'
            self.update_content_frame.place(x=0, y=161)

            alert_label = Label(self.content_frame, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=90, y=530)

        def delete_products_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#3C3F4A')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

            def search():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass

                def delete():

                    user_response = messagebox.askokcancel('Confirm Deletion', 'Do you want to delete the product ?')

                    if user_response:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                            my_cursor = db.cursor()
                            query = f'DELETE FROM product WHERE Product_ID = "{searched_product_id}";'
                            my_cursor.execute(query)
                            db.commit()
                            db.close()
                            for widget in self.delete_content_frame.winfo_children():
                                widget.destroy()
                            search_edit.delete(0, 'end')
                            alert_label.config(text='Successfully deleted the product', bg='#2FA422', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        except Exception as e:
                            alert_label.config(text='Sorry! Unable to delete', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                    else:
                        pass

                searched_product_id = search_edit.get()

                if searched_product_id == '':
                    alert_label.config(text='Enter a product ID', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    for widget in self.delete_content_frame.winfo_children():
                        widget.destroy()
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM product WHERE Product_ID = "{searched_product_id}"'
                        my_cursor.execute(query)
                        product = my_cursor.fetchall()

                        if len(product) == 0:
                            alert_label.config(text='Product doesn\'t exists', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:
                            product_id = product[0][0]
                            product_name = product[0][1]
                            product_category = product[0][2]
                            purchase_price = product[0][3]
                            dop = product[0][4]

                            product_name_label = Label(self.delete_content_frame, text='Product Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_name_label.place(x=106, y=46)

                            product_id_label = Label(self.delete_content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_id_label.place(x=106, y=111)

                            purchase_price_label = Label(self.delete_content_frame, text='Purchase Price', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            purchase_price_label.place(x=106, y=177)

                            product_category_label = Label(self.delete_content_frame, text='Product Category', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            product_category_label.place(x=106, y=243)

                            dop_label = Label(self.delete_content_frame, text='Date Of Purchase', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            dop_label.place(x=106, y=309)

                            product_name_label1 = Label(self.delete_content_frame, text=f'{product_name}', anchor='w', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', borderwidth=0, fg='white')
                            product_name_label1.place(x=281, y=46)

                            product_id_label1 = Label(self.delete_content_frame, text=f'{product_id}', anchor='w', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', borderwidth=0, fg='white')
                            product_id_label1.place(x=281, y=111)

                            purchase_price_label1 = Label(self.delete_content_frame, text=f'{purchase_price}', anchor='w', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', borderwidth=0, fg='white')
                            purchase_price_label1.place(x=281, y=177)

                            product_category_label1 = Label(self.delete_content_frame, text=f'{product_category}', anchor='w', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', borderwidth=0, fg='white')
                            product_category_label1.place(x=281, y=243)

                            dop_label1 = Label(self.delete_content_frame, text=f'{dop}', anchor='w', width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', borderwidth=0, fg='white')
                            dop_label1.place(x=281, y=309)

                            delete_button = Button(self.delete_content_frame, cursor='hand2', image=self.delete_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=delete)
                            delete_button.place(x=723, y=370)

                    except Exception as e:
                        alert_label.config(text='Sorry! Something went wrong..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()


            self.delete_products_bg_label = Label(self.content_frame, image=self.update_product_bg_image)
            self.delete_products_bg_label.place(x=-2, y=-2)

            delete_product_label = Label(self.content_frame, text='DELETE PRODUCT', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            delete_product_label.place(x=50, y=50)

            product_id_search_label = Label(self.content_frame, text='Product ID', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            product_id_search_label.place(x=160, y=116)

            search_edit = Entry(self.content_frame, width=60, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            search_edit.place(x=270, y=116)
            search_edit.delete(0, 'end')

            search_button = Button(self.content_frame, cursor='hand2', image=self.search_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=search)
            search_button.place(x=776, y=105)

            self.delete_content_frame = Frame(self.content_frame, width=980, height=470, bg='#292B37')  # bg='#292B37'
            self.delete_content_frame.place(x=0, y=161)

            alert_label = Label(self.content_frame, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=90, y=530)

        def sales_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#3C3F4A')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

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

        def selling_history_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#3C3F4A')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

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

            selling_history_bg_frame = Frame(self.content_frame,  bg='#292B37', height=107, width=958)
            selling_history_bg_frame.place(x=2, y=9)

            selling_history_bg_label = Label(selling_history_bg_frame, image=self.show_employees_bg_image, bg='#292B37')
            selling_history_bg_label.place(x=-2, y=-2)

            selling_history_label = Label(selling_history_bg_frame, text='SELLING HISTORY', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            selling_history_label.place(x=50, y=40)


            try:
                db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                my_cursor = db.cursor()
                query = f'SELECT Sell.Product_ID, sell.Product_Name, Sell.Product_Category, Sell.Purchase_Price, Sell.Selling_Price, Sell.DOS, Customer.Full_Name, Customer.Phone_Number, Customer.Email, Customer.Address FROM Sell, Customer WHERE sell.Customer_ID = customer.Customer_ID'
                my_cursor.execute(query)
                sells = my_cursor.fetchall()

                for i in range(len(sells)):
                    employee_frame = Frame(final_frame, bg='#292B37', height=393, width=958)

                    employee_frame_bg_label = Label(employee_frame, image=self.selling_history_bg_image, bg='#292B37')
                    employee_frame_bg_label.place(x=-2, y=-2)

                    selling_details_label = Label(employee_frame, text='Selling Details', font=('Arial Rounded MT', 14, 'bold'), bg='#50515B', fg='#BBBBBB')
                    selling_details_label.place(x=51, y=27)

                    product_name_label = Label(employee_frame, text=sells[i][1], font=('Arial Rounded MT', 16, 'bold'), bg='#50515B', fg='white')
                    product_name_label.place(x=82, y=70)

                    selling_price_label = Label(employee_frame, text='$ ' + str(sells[i][4]), font=('Arial Rounded MT', 10, 'bold'), bg='#50515B', fg='white')
                    selling_price_label.place(x=82, y=96)

                    product_id_label = Label(employee_frame, text=f'Product ID               :     {sells[i][0]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    product_id_label.place(x=82, y=123)

                    product_category_label = Label(employee_frame, text=f'Category                  :     {sells[i][2]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    product_category_label.place(x=82, y=152)

                    date_of_sell_label = Label(employee_frame, text=f'Date of Sale            :     {sells[i][5]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    date_of_sell_label.place(x=82, y=181)

                    profit_label = Label(employee_frame, text=f'Profit                        :     {sells[i][4] - sells[i][3]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    profit_label.place(x=82, y=210)

                    customer_name_label = Label(employee_frame, text=f'Customer Name     :     {sells[i][6]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    customer_name_label.place(x=82, y=250)

                    phone_label = Label(employee_frame, text=f'Phone Number       :     {sells[i][7]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    phone_label.place(x=82, y=278)

                    email_label = Label(employee_frame, text=f'E-mail                       :     {sells[i][8]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    email_label.place(x=82, y=306)

                    address_label = Label(employee_frame, text=f'Address                   :     {sells[i][9]}', font=('Arial Rounded MT', 11, 'bold'), bg='#50515B', fg='white')
                    address_label.place(x=82, y=335)

                    employee_frame.pack()
            except Exception as e:
                print(e)

        def show_employees_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#3C3F4A')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

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

            show_employees_bg_frame = Frame(self.content_frame,  bg='#292B37', height=107, width=958)
            show_employees_bg_frame.place(x=2, y=9)

            show_employees_bg_label = Label(show_employees_bg_frame, image=self.show_employees_bg_image, bg='#292B37')
            show_employees_bg_label.place(x=-2, y=-2)

            show_employees_label = Label(show_employees_bg_frame, text='SHOW EMPLOYEE INFORMATION', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            show_employees_label.place(x=50, y=40)

            try:

                db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                my_cursor = db.cursor()
                query = f'SELECT * FROM user_table WHERE NOT Designation = "Owner"'
                my_cursor.execute(query)
                employees = my_cursor.fetchall()

                for i in range(len(employees)):
                    employee_frame = Frame(final_frame, bg='#292B37', height=340, width=958)

                    employee_frame_bg_label = Label(employee_frame, image=self.show_employee_bg_image, bg='#292B37')
                    employee_frame_bg_label.place(x=-2, y=-2)

                    fullname_label = Label(employee_frame, text=employees[i][0], font=('Arial Rounded MT', 20, 'bold'), bg='#292B37', fg='white')
                    fullname_label.place(x=58, y=22)

                    designation_label = Label(employee_frame, text=employees[i][5], font=('Arial Rounded MT', 15, 'bold'), bg='#292B37', fg='white')
                    designation_label.place(x=58, y=72)

                    username_label = Label(employee_frame, text=f'Username               :     {employees[i][6]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    username_label.place(x=58, y=126)

                    salary_label = Label(employee_frame, text=f'Salary                      :     {employees[i][8]} $', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    salary_label.place(x=58, y=162)

                    phone_label = Label(employee_frame, text=f'Phone Number      :     {employees[i][2]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    phone_label.place(x=58, y=198)

                    email_label = Label(employee_frame, text=f'E-mail                      :     {employees[i][1]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    email_label.place(x=58, y=234)

                    address_label = Label(employee_frame, text=f'Address                  :     {employees[i][3]}', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                    address_label.place(x=58, y=270)

                    employee_frame.pack()
            except Exception as e:
                print(e)

        def add_employees_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#3C3F4A')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#292B37')

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            def add():

                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass

                employee_name = employee_name_entry.get()
                username = username_entry.get()
                password = password_entry.get()
                phone_number = phone_number_entry.get()
                salary = salary_entry.get()
                designation = designation_entry.get()

                if employee_name == '' or username == '' or password == '' or phone_number == '' or salary == '' or designation == '':
                    alert_label.config(text='Fill up all the fields', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                elif designation.lower() == 'owner':
                    alert_label.config(text='Sorry! Invalid input..', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'INSERT INTO user_table (Full_Name, Phone_Number, Designation, UserName,  User_Password, Salary) VALUE("{employee_name}", "{phone_number}", "{designation}", "{username}", "{password}", {salary});'
                        my_cursor.execute(query)
                        db.commit()
                        db.close()
                        alert_label.config(text='Employee added successfully..', bg='#2FA422', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                        employee_name_entry.delete(0, 'end')
                        username_entry.delete(0, 'end')
                        password_entry.delete(0, 'end')
                        phone_number_entry.delete(0, 'end')
                        salary_entry.delete(0, 'end')
                        designation_entry.delete(0, 'end')

                    except Exception as e:
                        alert_label.config(text='Sorry! Invalid input..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            add_employees_bg_label = Label(self.content_frame, image=self.add_employees_bg_image)
            add_employees_bg_label.place(x=-2, y=-2)

            add_employees_label = Label(self.content_frame, text='ADD EMPLOYEES', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            add_employees_label.place(x=50, y=50)

            employee_name_label = Label(self.content_frame, text='Employee Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            employee_name_label.place(x=106, y=136)

            username_label = Label(self.content_frame, text='Username', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            username_label.place(x=106, y=200)

            password_label = Label(self.content_frame, text='Password', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            password_label.place(x=106, y=260)

            phone_number_label = Label(self.content_frame, text='Phone Number', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            phone_number_label.place(x=106, y=322)

            salary_label = Label(self.content_frame, text='Salary', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            salary_label.place(x=106, y=383)

            designation_label = Label(self.content_frame, text='Designation', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            designation_label.place(x=106, y=446)

            employee_name_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            employee_name_entry.place(x=281, y=138)

            username_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            username_entry.place(x=281, y=200)

            password_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            password_entry.place(x=281, y=262)

            phone_number_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            phone_number_entry.place(x=281, y=324)

            salary_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            salary_entry.place(x=281, y=387)

            designation_entry = Entry(self.content_frame, width=70, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0,  fg='white')
            designation_entry.place(x=281, y=448)

            add_employee_button = Button(self.content_frame, cursor='hand2', image=self.add_employee_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=add)
            add_employee_button.place(x=722, y=523)

            alert_label = Label(self.content_frame, width=30, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=106, y=523)

        def update_employees_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#3C3F4A')
            self.delete_employees_button.config(bg='#292B37')

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            def search():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass

                def update():
                    fullname = fullname_edit.get()
                    email = email_edit.get()
                    phone = phone_edit.get()
                    address = address_edit.get()
                    dob = dob_edit.get()
                    designation = designation_edit.get()
                    password = password_edit.get()
                    salary = salary_edit.get()

                    if fullname == '' or email == '' or phone == '' or address == '' or dob == '' or designation == '' or password == '' or salary == '':
                        alert_label.config(text='Fill up all the fields', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)
                    else:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                            my_cursor = db.cursor()
                            query = f'UPDATE user_table SET Full_Name = "{fullname}", Email = "{email}", Phone_Number = "{phone}", Address = "{address}", DOB = "{dob}", Designation = "{designation}", User_Password = "{password}", Salary = {salary}  WHERE UserName = "{searched_username}";'
                            my_cursor.execute(query)
                            db.commit()
                            db.close()
                            for widget in self.update_content_frame.winfo_children():
                                widget.destroy()
                            search_edit.delete(0, 'end')
                            alert_label.config(text='Employee updated Successfully..', bg='#2FA422', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        except Exception as e:
                            alert_label.config(text='Sorry! Unable to update', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)

                searched_username = search_edit.get()

                if searched_username == '':
                    alert_label.config(text='Enter a Username', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    for widget in self.update_content_frame.winfo_children():
                        widget.destroy()
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM user_table WHERE UserName = "{searched_username}"'
                        my_cursor.execute(query)
                        employee = my_cursor.fetchall()

                        if len(employee) == 0 or searched_username == 'karim':
                            alert_label.config(text='Employee doesn\'t exists', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:
                            fullname = employee[0][0]
                            email = employee[0][1]
                            if email == None:
                                email = ''
                            phone = employee[0][2]
                            address = employee[0][3]
                            if address == None:
                                address = ''
                            dob = employee[0][4]
                            if dob == None:
                                dob = ''
                            designation = employee[0][5]
                            password = employee[0][7]
                            salary = employee[0][8]

                            update_employee_content_bg_label = Label(self.update_content_frame, image=self.update_employee_content_bg_image, bd=0)
                            update_employee_content_bg_label.place(x=0, y=0)

                            fullname_label = Label(self.update_content_frame, text='Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            fullname_label.place(x=14, y=37)

                            password_label = Label(self.update_content_frame, text='Password', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            password_label.place(x=14, y=107)

                            designation_label = Label(self.update_content_frame, text='Designation', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            designation_label.place(x=14, y=177)

                            salary_label = Label(self.update_content_frame, text='Salary', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            salary_label.place(x=14, y=243)

                            email_label = Label(self.update_content_frame, text='E-mail', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            email_label.place(x=475, y=37)

                            address_label = Label(self.update_content_frame, text='Address', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            address_label.place(x=475, y=111)

                            phone_label = Label(self.update_content_frame, text='Phone Number', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            phone_label.place(x=475, y=177)

                            dob_label = Label(self.update_content_frame, text='Date of birth', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            dob_label.place(x=475, y=243)

                            fullname_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            fullname_edit.place(x=135, y=39)

                            password_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            password_edit.place(x=135, y=109)

                            designation_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            designation_edit.place(x=135, y=179)

                            salary_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            salary_edit.place(x=135, y=248)

                            email_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            email_edit.place(x=625, y=39)

                            address_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            address_edit.place(x=625, y=109)

                            phone_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            phone_edit.place(x=625, y=179)

                            dob_edit = Entry(self.update_content_frame, width=34, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
                            dob_edit.place(x=625, y=248)

                            fullname_edit.delete(0, 'end')
                            password_edit.delete(0, 'end')
                            designation_edit.delete(0, 'end')
                            salary_edit.delete(0, 'end')
                            email_edit.delete(0, 'end')
                            address_edit.delete(0, 'end')
                            phone_edit.delete(0, 'end')
                            dob_edit.delete(0, 'end')

                            fullname_edit.insert(0, fullname)
                            password_edit.insert(0, password)
                            designation_edit.insert(0, designation)
                            salary_edit.insert(0, salary)
                            email_edit.insert(0, email)
                            address_edit.insert(0, address)
                            phone_edit.insert(0, phone)
                            dob_edit.insert(0, dob)

                            update_button = Button(self.update_content_frame, cursor='hand2', image=self.update_employee_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=update)
                            update_button.place(x=755, y=310)

                    except Exception as e:
                        alert_label.config(text='Sorry! Something went wrong..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            self.update_employee_bg_label = Label(self.content_frame, image=self.update_employee_bg_image)
            self.update_employee_bg_label.place(x=-2, y=-2)

            update_employee_label = Label(self.content_frame, text='UPDATE EMPLOYEE', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            update_employee_label.place(x=50, y=40)

            username_search_label = Label(self.content_frame, text='Username', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            username_search_label.place(x=220, y=90)

            search_edit = Entry(self.content_frame, width=41, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            search_edit.place(x=332, y=90)
            search_edit.delete(0, 'end')

            search_button = Button(self.content_frame, cursor='hand2', image=self.search_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=search)
            search_button.place(x=680, y=78)

            self.update_content_frame = Frame(self.content_frame, width=938, height=387, bg='#292B37')  # bg='#292B37'
            self.update_content_frame.place(x=22, y=186)

            alert_label = Label(self.content_frame, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=90, y=560)

        def delete_employees_button_clicked():
            self.dashboard_button.config(bg='#292B37')
            self.show_products_button.config(bg='#292B37')
            self.add_products_button.config(bg='#292B37')
            self.update_products_button.config(bg='#292B37')
            self.delete_products_button.config(bg='#292B37')
            self.sales_button.config(bg='#292B37')
            self.selling_history_button.config(bg='#292B37')
            self.show_employees_button.config(bg='#292B37')
            self.add_employees_button.config(bg='#292B37')
            self.update_employees_button.config(bg='#292B37')
            self.delete_employees_button.config(bg='#3C3F4A')

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            def search():
                def disappear_alert_label():
                    try:
                        alert_label.config(bg='#292B37', fg='#292B37')
                    except Exception as e:
                        pass

                def delete():
                    user_response = messagebox.askokcancel('Confirm Deletion', 'Do you want to delete the Employee ?')

                    if user_response:
                        try:
                            db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                            my_cursor = db.cursor()
                            query = f'DELETE FROM user_table WHERE UserName = "{searched_username}";'
                            my_cursor.execute(query)
                            db.commit()
                            db.close()
                            for widget in self.delete_content_frame.winfo_children():
                                widget.destroy()
                            search_edit.delete(0, 'end')
                            alert_label.config(text='Successfully deleted the employee', bg='#2FA422', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        except Exception as e:
                            alert_label.config(text='Sorry! Unable to delete', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                    else:
                        pass

                searched_username = search_edit.get()

                if searched_username == '':
                    alert_label.config(text='Enter a Username', bg='#AA2F2F', fg='white')
                    self.content_frame.after(1500, disappear_alert_label)
                else:
                    for widget in self.delete_content_frame.winfo_children():
                        widget.destroy()
                    try:
                        db = mysql.connector.connect(host='localhost', user='root', passwd='', database='Easy_Dealer')
                        my_cursor = db.cursor()
                        query = f'SELECT * FROM user_table WHERE UserName = "{searched_username}"'
                        my_cursor.execute(query)
                        employee = my_cursor.fetchall()

                        if len(employee) == 0 or searched_username == 'karim':
                            alert_label.config(text='Employee doesn\'t exists', bg='#AA2F2F', fg='white')
                            self.content_frame.after(1500, disappear_alert_label)
                        else:
                            fullname = employee[0][0]
                            email = employee[0][1]
                            if email == None:
                                email = ''
                            phone = employee[0][2]
                            address = employee[0][3]
                            if address == None:
                                address = ''
                            dob = employee[0][4]
                            if dob == None:
                                dob = ''
                            designation = employee[0][5]
                            password = employee[0][7]
                            salary = employee[0][8]

                            fullname_label = Label(self.delete_content_frame, text='Name', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            fullname_label.place(x=202, y=22)

                            password_label = Label(self.delete_content_frame, text='Password', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            password_label.place(x=202, y=66)

                            designation_label = Label(self.delete_content_frame, text='Designation', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            designation_label.place(x=202, y=110)

                            salary_label = Label(self.delete_content_frame, text='Salary', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            salary_label.place(x=202, y=154)

                            email_label = Label(self.delete_content_frame, text='E-mail', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            email_label.place(x=202, y=198)

                            address_label = Label(self.delete_content_frame, text='Address', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            address_label.place(x=202, y=242)

                            phone_label = Label(self.delete_content_frame, text='Phone Number', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            phone_label.place(x=202, y=286)

                            dob_label = Label(self.delete_content_frame, text='Date of birth', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            dob_label.place(x=202, y=330)

                            fullname_label1 = Label(self.delete_content_frame, text=fullname, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            fullname_label1.place(x=350, y=22)

                            password_label1 = Label(self.delete_content_frame, text=password, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            password_label1.place(x=350, y=66)

                            designation_label1 = Label(self.delete_content_frame, text=designation, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            designation_label1.place(x=350, y=110)

                            salary_label1 = Label(self.delete_content_frame, text=salary, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            salary_label1.place(x=350, y=154)

                            email_label1 = Label(self.delete_content_frame, text=email, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            email_label1.place(x=350, y=198)

                            address_label1 = Label(self.delete_content_frame, text=address, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            address_label1.place(x=350, y=242)

                            phone_label1 = Label(self.delete_content_frame, text=phone, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            phone_label1.place(x=350, y=286)

                            dob_label1 = Label(self.delete_content_frame, text=dob, font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
                            dob_label1.place(x=350, y=330)

                            # fullname_edit.delete(0, 'end')
                            # password_edit.delete(0, 'end')
                            # designation_edit.delete(0, 'end')
                            # salary_edit.delete(0, 'end')
                            # email_edit.delete(0, 'end')
                            # address_edit.delete(0, 'end')
                            # phone_edit.delete(0, 'end')
                            # dob_edit.delete(0, 'end')
                            #
                            # fullname_edit.insert(0, fullname)
                            # password_edit.insert(0, password)
                            # designation_edit.insert(0, designation)
                            # salary_edit.insert(0, salary)
                            # email_edit.insert(0, email)
                            # address_edit.insert(0, address)
                            # phone_edit.insert(0, phone)
                            # dob_edit.insert(0, dob)

                            delete_button = Button(self.delete_content_frame, cursor='hand2', image=self.delete_employee_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=delete)
                            delete_button.place(x=640, y=380)

                    except Exception as e:
                        alert_label.config(text='Sorry! Something went wrong..', bg='#AA2F2F', fg='white')
                        self.content_frame.after(1500, disappear_alert_label)

            for widget in self.content_frame.winfo_children():
                widget.destroy()

            self.delete_employee_bg_label = Label(self.content_frame, image=self.update_employee_bg_image)
            self.delete_employee_bg_label.place(x=-2, y=-2)

            delete_employee_label = Label(self.content_frame, text='DELETE EMPLOYEE', font=('Arial Rounded MT', 14, 'bold'), bg='#292B37', fg='#BBBBBB')
            delete_employee_label.place(x=50, y=40)

            username_search_label = Label(self.content_frame, text='Username', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
            username_search_label.place(x=220, y=90)

            search_edit = Entry(self.content_frame, width=41, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', borderwidth=0, fg='white')
            search_edit.place(x=332, y=90)
            search_edit.delete(0, 'end')

            search_button = Button(self.content_frame, cursor='hand2', image=self.search_button_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=search)
            search_button.place(x=680, y=78)

            self.delete_content_frame = Frame(self.content_frame, width=938, height=446, bg='#292B37')  # bg='#292B37'
            self.delete_content_frame.place(x=22, y=154)

            alert_label = Label(self.content_frame, width=32, height=2, text='Sorry, Invalid input..', font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#292B37')
            alert_label.place(x=90, y=560)

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
                            query = f'UPDATE user_table SET Full_Name="{name}", User_Password="{password}", Phone_Number="{phone}", Email="{email}", Address="{address}", DOB="{dob}" WHERE UserName="{self.username}"'
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

                password_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0,)
                password_entry.place(x=198, y=159)

                phone_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0,)
                phone_entry.place(x=198, y=207)

                email_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0,)
                email_entry.place(x=198, y=255)

                address_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0,)
                address_entry.place(x=198, y=303)

                dob_entry = Entry(prof, font=('Arial Rounded MT', 11, 'bold'), bg='#686972', fg='white',  borderwidth=0,)
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
        self.add_products_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/add_product_bg.png'))
        self.add_products_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/add_product_button.png'))
        self.update_product_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_product_bg.png'))
        self.search_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/search_button_img.png'))
        self.update_content_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_content.png'))
        self.update_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_button_img.png'))
        self.delete_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/delete_button_img.png'))
        self.add_employees_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/add_employee_bg.png'))
        self.add_employee_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/add_employee_button_img.png'))
        self.update_employee_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_employee_bg.png'))
        self.update_employee_content_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_employee_content.png'))
        self.update_employee_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/update_employee_button_img.png'))
        self.delete_employee_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/delete_employee_button.png'))
        self.show_employees_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/show_employees_title_bg.png'))
        self.show_employee_bg_image = ImageTk.PhotoImage( Image.open(directory_path + '/images/show_employee_bg.png'))
        self.sales_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/sales_bg.png'))
        self.ok_button_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/ok_button.png'))
        self.search_button_icon_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/search_icon.png'))
        self.selling_history_bg_image = ImageTk.PhotoImage(Image.open(directory_path + '/images/selling_history_bg.png'))
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

        self.profile_button = Button(self.root, cursor='hand2', image=self.user_icon_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=profile)
        self.profile_button.place(x=930, y=25)

        self.profile_name_label = Label(self.root, text=fullname, anchor='w', width=25, font=('Arial Rounded MT', 10, 'bold'), bg='#292B37', fg='#BBBBBB')
        self.profile_name_label.place(x=962, y=28)

        self.logout_button = Button(self.root, cursor='hand2', image=self.logout_icon_image, borderwidth=0, activebackground='#292B37', font=('Arial Rounded MT', 10), bg='#292B37', command=logout)
        self.logout_button.place(x=1200, y=22)

        self.content_frame = Frame(self.root, width=980, height=630, bg='#292B37') #bg='#292B37'
        self.content_frame.place(x=278, y=64)

        self.dashboard_bg_label = Label(self.content_frame, image=self.dashboard_bg_image)
        self.dashboard_bg_label.place(x=-2, y=-2)

        self.side_frame = Frame(self.root, width=255, height=425, bg='#292B37')  # bg='#292B37'
        self.side_frame.place(x=18, y=255)

        temp_frame = Frame(self.side_frame, width=230, height=421, bg='#292B37', border=None)
        temp_frame.place(x=2, y=2)

        showall_canvas = Canvas(temp_frame, width=230, height=421, bg='#292B37')

        vertical_bar = ttk.Scrollbar(temp_frame, orient='vertical', command=showall_canvas.yview)
        vertical_bar.pack(side=RIGHT, fill='y')

        showall_canvas.config(yscrollcommand=vertical_bar.set)

        final_frame = Frame(temp_frame, width=230, height=421, bg='#292B37')
        showall_canvas.create_window((0, 0), window=final_frame, anchor='nw')
        showall_canvas.bind('<Configure>', lambda e: showall_canvas.configure(scrollregion=showall_canvas.bbox('all')))

        final_frame.bind('<Enter>', bound_to_mousewheel)
        final_frame.bind('<Leave>', unbound_to_mousewheel)

        border_hide_label1 = Label(self.root, bg='#292B37', height=28, width=-1)
        border_hide_label1.place(x=17, y=255)

        border_hide_label2 = Label(self.root, bg='#292B37', height=0, width=36)
        border_hide_label2.place(x=16, y=238)

        border_hide_label3 = Label(self.root, bg='#292B37', height=28, width=-1)
        border_hide_label3.place(x=248, y=255)

        showall_canvas.config(yscrollcommand=vertical_bar.set)
        showall_canvas.pack(side=LEFT, expand=True, fill=BOTH)

        self.dashboard_button = Button(final_frame, text='DASHBOARD                 ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#3C3F4A', borderwidth=0, activebackground='#333640', activeforeground='white', command=dashboard_button_clicked)
        self.dashboard_button.pack()

        self.show_products_button = Button(final_frame, text='SHOW PRODUCTS       ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=show_products_button_clicked)
        self.show_products_button.pack()

        self.add_products_button = Button(final_frame, text='ADD PRODUCTS          ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=add_products_button_clicked)
        self.add_products_button.pack()

        self.update_products_button = Button(final_frame, text='UPDATE PRODUCTS   ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=update_products_button_clicked)
        self.update_products_button.pack()

        self.delete_products_button = Button(final_frame, text='DELETE PRODUCTS   ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=delete_products_button_clicked)
        self.delete_products_button.pack()

        self.sales_button = Button(final_frame, text='SALES                            ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=sales_button_clicked)
        self.sales_button.pack()

        self.selling_history_button = Button(final_frame, text='SELLING HISTORY      ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=selling_history_button_clicked)
        self.selling_history_button.pack()

        self.show_employees_button = Button(final_frame, text='SHOW EMPLOYEES    ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=show_employees_button_clicked)
        self.show_employees_button.pack()

        self.add_employees_button = Button(final_frame, text='ADD EMPLOYEES       ', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=add_employees_button_clicked)
        self.add_employees_button.pack()

        self.update_employees_button = Button(final_frame, text='UPDATE EMPLOYEES', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=update_employees_button_clicked)
        self.update_employees_button.pack()

        self.delete_employees_button = Button(final_frame, text='DELETE EMPLOYEES', cursor='hand2', font=('Arial Rounded MT', 11, 'bold'), height=2, width=25, fg='white', bg='#292B37', borderwidth=0, activebackground='#333640', activeforeground='white', command=delete_employees_button_clicked)
        self.delete_employees_button.pack()

        self.welcome_label = Label(self.content_frame, text='WELCOME,', font=('Arial Rounded MT', 13, 'bold'), bg='#292B37', fg='white')
        self.welcome_label.place(x=21, y=14)

        self.name_label = Label(self.content_frame, text=fullname, anchor='w', width=25, font=('Arial Rounded MT', 13, 'bold'), bg='#292B37', fg='#BBBBBB')
        self.name_label.place(x=118, y=14)

        self.recent_sells_label = Label(self.content_frame, text='Recent sells,', font=('Arial Rounded MT', 11, 'bold'), bg='#292B37', fg='white')
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

        self.root.mainloop()

# owner = tk.ThemedTk()
# owner.get_themes()
# owner.set_theme('black')
# EDO = Owner(owner, 'karim')