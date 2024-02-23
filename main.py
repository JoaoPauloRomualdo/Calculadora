import customtkinter
from tkinter import END 
#FUNÇÃO PARA ADICIONAR NUMEROS NA TELA
def button_click(number):

    # Concatena os números digitados
    e.insert(END, str(number))
    #COLOCA O VALOR DO ENTRY DENTRO DE UMA VARIAVEL
    current = e.get()
    #SETA O NUMERO PARA ZERO A CADA NOVO NUMERO DIGITADO
    e.delete(0, END)
    #CONCATEÇÃO DOS NUMEROS 
    e.insert(0, str(current) + str(number))
    

#FUNÇÃO PARA LIMPAR A TELA
def button_clear() :
    e.delete(0, END)


#FUNÇÃO PARA SOMAR
def button_adding():
    first_number = e.get()
    global f_num, match
    match = "somar"
    f_num = int(first_number)
    e.delete(0, END) 

def sub() :
    first_number = e.get()
    global f_num, match
    match = "sub"
    f_num = int(first_number)
    e.delete(0, END) 

def div():
    first_number = e.get()
    global f_num, match
    match = "div"
    f_num = int(first_number)
    e.delete(0, END) 

def mult():
    first_number = e.get()
    global f_num, match
    match = "mult"
    f_num = int(first_number)
    e.delete(0, END) 

def result_button():
    #ARMAZENA O VALOR DO SECUNDO NUMERO
    second_number = e.get()
    e.delete(0,END)
    if match == "somar":
        e.insert(0,f_num + int(second_number))
    if match == "sub":
        e.insert(0,f_num - int(second_number))
    if match == "div":
        e.insert(0,f_num / int(second_number))
    if match == "mult":
        e.insert(0,f_num * int(second_number))








#ARMAZANA A JANELA DO CUSTOMTKINTER DENTRO DA VARIAVEL ROOT
root = customtkinter.CTk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.resizable(False, False)
root.title("CALCULADORA SIMPOL")
#DEFINE O TEMA DA JANELA
customtkinter.set_appearance_mode('dark-blue')

#CRIA OS ELEMENTOS NA JANELA 
e = customtkinter.CTkEntry(
    root,
    placeholder_text="0",
    width=550,
    height=50,
    text_color='#f0f0f0',
    font=('Helvetica', 20, "bold")
)
e.grid(padx=10, pady=20,columnspan=3)
e.grid(row=0, column=0, columnspan=5, pady=20)
#------ BOTÃOS ------
button_1 = customtkinter.CTkButton(root, text="1",fg_color="transparent",border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(1))
button_2 = customtkinter.CTkButton(root, text="2",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(2))
button_3 = customtkinter.CTkButton(root, text="3",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(3))
button_4 = customtkinter.CTkButton(root, text="4",fg_color='transparent',border_width=1, hover_color="disabled",text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(4))
button_5 = customtkinter.CTkButton(root, text="5",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(5))
button_6 = customtkinter.CTkButton(root, text="6",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(6))
button_7 = customtkinter.CTkButton(root, text="7",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(7))
button_8 = customtkinter.CTkButton(root, text="8",fg_color='transparent',border_width=1, hover_color="disabled",text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(8))
button_9 = customtkinter.CTkButton(root, text="9",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(9))
button_0 = customtkinter.CTkButton(root, text="0",fg_color='transparent',border_width=1,hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=lambda: button_click(0))


button_c = customtkinter.CTkButton(root,text="C",fg_color="green",hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=button_clear)

button_add = customtkinter.CTkButton(root,text="+",fg_color="#B31312",hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=button_adding)

button_sub = customtkinter.CTkButton(root,text="-",fg_color="#116D6E",hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=sub)

button_div = customtkinter.CTkButton(root,text="/",fg_color="#E9B824",hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=div)

button_mult = customtkinter.CTkButton(root,text="*",fg_color="#0079FF",hover_color="disabled", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=mult)

button_result = customtkinter.CTkButton(root,text="=",fg_color="#0802A3",hover_color="#0802A3", text_color='#f0f0f0',font=('Helvetica', 18, "bold"),command=result_button)



#POSICIONA OS ELEMENTOS NA JANELA
button_3.grid(row=1,column=2,padx=10,pady=10)
button_2.grid(row=1,column=1)
button_1.grid(row=1,column=0)


button_6.grid(row=2,column=2)
button_5.grid(row=2,column=1,padx=10,pady=10)
button_4.grid(row=2,column=0)

button_9.grid(row=3,column=2)
button_8.grid(row=3,column=1)
button_7.grid(row=3,column=0,padx=10,pady=10)

button_0.grid(row=4,column=0)
button_c.grid(row=4,column=1)
button_result.grid(row=4,column=2)
button_add.grid(row=1,column=4)
button_sub.grid(row=2,column=4)
button_div.grid(row=3,column=4)
button_mult.grid(row=4,column=4,padx=10,pady=10)


#FICA RODANDO A JANELA DO CUSTOMTKINTER EM UM LOOP PARA NÃO FECHAR
root.mainloop()