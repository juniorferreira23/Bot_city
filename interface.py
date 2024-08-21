import customtkinter as ctk
from tkinter import *
from tkinter.filedialog import askopenfilename
import amil
import bot

# Configurando aparência padrão do sistema
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.apperence()
        self.system()
        
        
    def layout_config(self):
        self.title('Sistema de Verificação de Recebidos')
        self.geometry('600x500')


    def apperence(self):
        self.lb_opm = ctk.CTkLabel(self, text='Tema', bg_color='transparent', text_color=['#000', '#fff']).place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=['System', 'Light', 'Dark'], command=self.change_apperence).place(x=50, y=460)
        
        
    def change_apperence(self, new_apperence_mode):
        ctk.set_appearance_mode(new_apperence_mode)
         
        
    def system(self):
        
        def submit():
            #Pegando os dados dos Entrys
            operator = operator_combobox.get()
            print(operator)
            date = date_value.get()
            print(date)
            print(self.path)
            
            if operator == 'Amil':
                extrato = amil.extrair_dados_amil(self.path)
                bot.main(extrato)
            
            
        def get_path():
            self.path = askopenfilename(title='Selecione uma pasta do computador:')
            
            
        #Variaveis de texto
        date_value = StringVar()
        self.path = None
            
        
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='teal' ,fg_color='teal').place(x=0, y=10)
        title = ctk.CTkLabel(frame, text='Sistema de Verificação de Recebidos', font=('Century Gothic bold', 24), fg_color='teal').place(x=100, y=20)
        span = ctk.CTkLabel(self, text='Por favor, preencher todos os campos do formulário!', font=('Century Gothic bold', 16), text_color=['#000', '#fff']).place(x=50, y=70)
        
        #Labels
        lb_operator = ctk.CTkLabel(self, text='Operadora:', font=('Century Gothic bold', 16), text_color=['#000', '#fff'])
        lb_date = ctk.CTkLabel(self, text='Data de Recebimento:', font=('Century Gothic bold', 16), text_color=['#000', '#fff'])
        lb_path = ctk.CTkLabel(self, text='Selecione o arquivo:', font=('Century Gothic bold', 16), text_color=['#000', '#fff'])
        
        #Anexar caminho do relatório
        btn_path = ctk.CTkButton(self, text='Selecione o Arquvio', command=get_path)
        
        #Combox
        operator_combobox = ctk.CTkComboBox(self, values=['Amil', 'Bradesco', 'SulAmerica', 'Unimed', 'Hapvida'], font=('Century Gothic bold', 16))
        operator_combobox.set('Amil')
        
        #Entrys
        date_entry = ctk.CTkEntry(self, width=140, textvariable=date_value, font=('Century Gothic bold', 16), fg_color='transparent')
        
        #Buttom
        btn_submit = ctk.CTkButton(self, text='Executar', command=submit, fg_color='#151', hover_color='#131')
        
        #Posicionando os elementos na janela
        lb_operator.place(x=50, y=140)
        operator_combobox.place(x=50, y=170)
        lb_path.place(x=50, y=210)
        btn_path.place(x=50, y=240)
        lb_date.place(x=50, y=280)
        date_entry.place(x=50, y=310)
        btn_submit.place(x=300, y=310)
        
                 

if __name__ == "__main__":
    app = App()
    app.mainloop()