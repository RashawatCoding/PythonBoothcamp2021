#GUIWiki.py
import wikipedia

#เปลี่ยนเป็นภาษาไทย
wikipedia.set_lang('th')
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('โปรแกรม wiki')
GUI.geometry('400x300')

#config
FONT1 = ('Angsananew',15)

#คำอธิบาย
L = ttk.Label(GUI,text = 'ค้นหาบทความ',font = FONT1)
L.pack()

#ช่ิองค้นหาข้อมูล
v_search = StringVar() #กล่องสำหรับเก็บ key word
E1 = ttk.Entry(GUI,textvariable = v_search,font = FONT1,width = 35)
E1.pack(pady = 10)

#ปุ่มค้นหา
def search():
    keyword = v_search.get() #เป็นการดึงข้อมูลเข้ามา .get ใช้ได้กับ StraingVar() เท่านั้น
    print(wikipedia.search(keyword))#เป็นการบอกว่าคำที่เรา search มีทั้งหมดกี่คำ
    result = wikipedia.summary(keyword)
    print(result)
    
B1 = ttk.Button(GUI,text = 'Search',command = search)
B1.pack(ipadx = 20,ipady = 10)

GUI.mainloop()


