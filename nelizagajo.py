from tkinter import*
import sqlite3
root=Tk()
root.title("My Coffee Shop Management")
root.geometry("500x500")
root.config(bg="#e8daef")

conn=sqlite3.connect("E:/MAAM SOL/neliza_info.db")
c=conn.cursor()

def submit(): 
    conn = sqlite3.connect("E:/MAAM SOL/neliza_info.db")
    c=conn.cursor()

    c.execute("INSERT INTO customer_info Values(:customer_name,:coffee_type,:quantity,:total_price,:order_date)",
    {
                 'customer_name':customer_name.get(),
                 'coffee_type':coffee_type.get(),
                 'quantity':quantity.get(),
                 'total_price':total_price.get(),
                 'order_date':order_date.get(),
                           
             })
     
    conn.commit()
    conn.close() 
    customer_name.delete(0,END)
    coffee_type.delete(0,END)
    quantity.delete(0,END)
    total_price.delete(0,END)
    order_date.delete(0,END)
   
 
 
def query():
    conn=sqlite3.connect("E:/MAAM SOL/neliza_info.db" )
    c=conn.cursor()
    c.execute("SELECT *,oid FROM customer_info ")
    records=c.fetchall()

    print_records=''
    for record in records:
        print_records +=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+"/n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=30,column=0,columnspan=2)

    conn.commit
    conn.close()

def delete():
    conn=sqlite3.connect("E:/MAAM SOL/neliza_info.db")
    c=conn.cursor()
    c.execute("DELETE from customer_info  WHERE oid=?", (str(delete_box.get()),))

    conn.commit()
    conn.close()

def update():

    conn=sqlite3.connect("E:/MAAM SOL/neliza_info.db")
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute(""" UPDATE customer_info  SET
        customer_name'=:customer_name',
        coffee_type=:coffee_type,
        quantity=:quantity,
        total_price=:total_price,
        order_date=:order_date,   

        WHERE oid=:oid""",
            {
                'customer_name':customer_name_editor.get(),
                'coffee_type':coffee_type_editor.get(),
                'quantity':quantity_editor.get(),
                'total_price':total_price_editor.get(),
                'order_date':order_date_editor.get(),
                'oid':record_id     

                })

    conn.commit()
    conn.close()

def edit():
    editor=Tk()
    editor.title('Update Record from database')
    editor.geometry("500x500")
    editor.config(bg="#e8daef")
    conn=sqlite3.connect("E:/MAAM SOL/neliza_info.db")
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT * FROM customer_info  WHERE oid=?",(str(record_id),))
    records=c.fetchall()

    global customer_name_editor
    global coffee_type_editor
    global quantity_editor
    global total_price_editor
    global order_date_editor
   
    
    customer_name_editor=Entry(editor,width=30)
    customer_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    coffee_type_editor=Entry(editor,width=30)
    coffee_type_editor.grid(row=1,column=1,padx=20)
    quantity_editor=Entry(editor,width=30)
    quantity_editor.grid(row=2,column=1,padx=20)
    total_price_editor=Entry(editor,width=30)
    total_price_editor.grid(row=3,column=1,padx=20)
    order_date_editor=Entry(editor,width=30)
    order_date_editor.grid(row=4,column=1,padx=20)
   

    customer_name_label=Label(editor,text="Customer Name")
    customer_name_label.grid(row=0,column=0)
    coffee_type_label=Label(editor,text="Coffee Type")
    coffee_type_label.grid(row=1,column=0)
    quantity_label_label=Label(editor,text= "Quantity")
    quantity_label_label.grid(row=2,column=0)
    total_price_label_label=Label(editor,text= "Total Price")
    total_price_label_label.grid(row=3,column=0)
    order_date_label_label=Label(editor,text= "Order Date")
    order_date_label_label.grid(row=4,column=0)
    
   
    for record in records:
       customer_name_editor.insert(0, record[0])
       coffee_type_editor.insert(0, record[1])
       quantity_editor.insert(0, record[2])
       total_price_editor.insert(0, record[3])
       order_date_editor.insert(0, record[4])
       

    save_btn=Button(editor,text="Save Record", command=update)
    save_btn.grid(row=10, column=0, columnspan=2,pady=10,padx=10,ipadx=140)


    conn.commit()
    conn.close()
'''
    
c.execute("""CREATE TABLE customer_info(
          "customer_name"    TEXT,
          "coffee_type      TEXT,
          "quantity         INTEGER,
          "total_price      TEXT,
          "order_date       TEXT 
          )""");
'''

customer_name=Entry(root,width=30,bg="light gray", fg="black")
customer_name.grid(row=0,column=1,padx=10)

coffee_type=Entry(root,width=30,bg="lightgray", fg="black")
coffee_type.grid(row=1,column=1,padx=10)

quantity=Entry(root,width=30,bg="lightgray", fg="black")
quantity.grid(row=2,column=1,padx=20)

total_price=Entry(root,width=30,bg="lightgray", fg="black")
total_price.grid(row=3,column=1,padx=20)

order_date=Entry(root,width=30,bg="lightgray", fg="black")
order_date.grid(row=4,column=1,padx=20)


customer_name_label=Label(root,text=" Customer Name")
customer_name_label.grid(row=0,column=0)
coffee_type_label=Label(root,text="Coffee Type")
coffee_type_label.grid(row=1,column=0)
quantity_label_label=Label(root,text= "Quantity")
quantity_label_label.grid(row=2,column=0)
total_price_label_label=Label(root,text= "Total Price")
total_price_label_label.grid(row=3,column=0)
order_date_label_label=Label(root,text= "Order Date")
order_date_label_label.grid(row=4,column=0)


submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=110)

query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

delete_box=Entry(root,width=30,bg="lightgray",fg="black")
delete_box.grid(row=10,column=1)

delete_box_label=Label(root,text= "Select ID.No")
delete_box_label.grid(row=10,column=0)

query_btn=Button(root,text="Delete Records",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=134)

edit_btn=Button(root,text= "Edit Record", command=edit)
edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=142)

                                                                                                                          
