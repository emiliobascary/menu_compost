#!/usr/bin/env python
# coding: utf-8

# In[3]:


import lcddriver
import time
import datetime


# In[2]:


display = lcddriver.lcd()
display.lcd_display_string("UNRN \n Compostador")

buttons_list = [16, 17, 18, 19]
GPIO.setup(buttons_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global password_inicio
global inicar      # 0 para parar, 1 para iniciar
global pausar      # variable para indicar pausa de proceso

def buttonPressed(channel):
    global button
    if channel == 16:
        button = 1                   #flag indicador de boton SEL presionado
    elif channel == 17:
        button = 2                   #flag indicador de boton DOWN presionado
    elif channel == 18:
        button = 3                   #flag indicador de boton RIGHT presionado
    elif channel == 19:
        button = 4                   #flag indicador de boton LEFT presionado        

for pin in buttons_list:
    GPIO.add_event_detect(pin, GPIO.RISING, callback=buttonPressed, bouncetime=150)

class menu:
    
    def __init__(self):
        self.currentIndex = 0
        self.currentMenu = 0
        
    def menu01(self):
        #menu inicio, admin/visita
        display.lcd_clear()
        menu01_text = [" Admin"," Visita"]
        for i in range(2):
            display.lcd_display_string(menu01_text[i], i)

    def menu02(self):
        #menu ingrese password
        position = 0
        display.lcd_clear()
        menu02_text = ["Ingrese","password","0123456789"]
        for i in range(3):
            display.lcd_display_string(menu02_text[i], i)
        
        #lcd.setCursor(position,3)
        display.lcd_display_string("*")
        i = 0

        if iniciar == 0:                                   #si el proceso no inicio, creo contraseña

            while(i!=4):
                
                if button == 1:
                    password_inicio[i] = position
                    i = i + 1
                    button = 0
                elif (button == 3 or button ==4):
                    lcd.setCursor(position,3)
                    display.lcd_display_string(" ")
                    if (position >= 0 and position <= 9):
                        if button == 3:
                            position = position + 1
                        else:
                            position = position - 1
                    lcd.setCursor(position,3)
                    display.lcd_display_string("*")
                    button = 0
                    

        password_ingreso = []
        i = 0

        else:                                           #si el proceso ya está iniciado, verifico la contraseña

            while(i!=4):
                
                if button == 1:
                    password_ingreso[i] = position
                    i = i + 1
                    button = 0
                elif (button == 3 or button ==4):
                    lcd.setCursor(position,3)
                    display.lcd_display_string(" ")
                    if (position >= 0 and position <= 9):
                        if button == 3:
                            position = position + 1
                        else:
                            position = position - 1
                    lcd.setCursor(position,3)
                    display.lcd_display_string("*")
                    button = 0


        if password_ingreso != password_inicio:
            display.lcd_clear()
            lcd.setCursor(1,0)
            display.lcd_display_string('Password \n incorrecta.')
            sleep(1)
            menu01

    def menu03(self):
        #menu visualizacion/control/configuracion/volver
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu03_text = ["Visualizacion","Control","Configuracion","Volver"]
        for i in range(4):
            lcd.setCursor(1,i)
            display.lcd_display_string(menu03_text[i])

    def menu04(self):
        #menu visualizacion
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu04_text = [" Experimentacion"," en proceso"," Temp. :"," Hum. :"]
        for i in range(4):
            display.lcd_display_string(menu04_text[i], i)

    def menu05(self):
        #menu control
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu05_text = [" Iniciar"," Pausar"," Parar"," Volver"]
        for i in range(4):
            display.lcd_display_string(menu05_text[i], i)

    def menu06(self):
        #menu pausar
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu06_text = [" Experimentacion"," en pausa."," Reanudar"," Parar"]
        for i in range(4):
            display.lcd_display_string(menu06_text[i], i)
   
    def menu07(self):
        #menu configuracion
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu07_text = [" Rango temp."," Rango O2"," Tiempo de medicion"," Volver"]
        for i in range(4):
            display.lcd_display_string(menu07_text[i])

    def menu08(self):
        #menu seleccionar temperatura minima
        display.lcd_display_string('Temp. Min. :', 0)
        display.lcd_display_string('             ^',1)

    def menu09(self):
        #menu seleccionar temperatura maxima
        display.lcd_display_string('Temp. Max. :', 0)
        display.lcd_display_string('             ^', 1)

    def menu10(self):
        #menu seleccionar oxigeno minimo
        display.lcd_display_string('O2 Min. :', 0)
        display.lcd_display_string('          ^', 1)

    def menu11(self):
        #menu seleccionar oxigeno maximo
        display.lcd_display_string('O2 Max. :', 0)
        display.lcd_display_string('          ^', 1)

    def menu12(self):
        #menu seleccionar intervalo de medicion
        display.lcd_display_string('Tiempo: ', 0)
        display.lcd_display_string('        ^', 1)

    def menu13(self):
        #menu visualizacion
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu13_text = [" Experimentacion"," en proceso"," O2 :"," CO2 :"]
        for i in range(4):
            display.lcd_display_string(menu13_text[i], i)
        
    def update(self, command):
        if command == 's'
            self.select()
        elif command == 'd'
            self.down()
        elif command == 'r'
            self.right()
        elif command == 'l'
            self.left()
            
    def select(self):
        if self.currentMenu == 1:
            if self.currenIndex == 0:
                menu02()
                self.currentMenu = 2
            elif self.currentIndex == 1:
                menu03()
                self.currentMenu = 3
                
        elif self.currentMenu == 2:
            menu03()
            self.currentMenu = 3
            
        elif self.currentMenu == 3:
            if self.currenIndex == 0:
                menu04()
                self.currentMenu = 4
            elif self.currentIndex == 1:
                menu05()
                self.currentMenu = 5
            elif self.currentIndex == 2:
                menu07()
                self.currentMenu = 7
            elif self.currentIndex == 3:
                menu01()
                self.currentMenu = 1
                
        elif self.currentMenu == 5:
            if self.currenIndex == 0:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 1:
                menu06()
                self.currentMenu = 6
            elif self.currentIndex == 2:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 3:
                menu05()
                self.currentMenu = 5
                
        elif self.currentMenu == 6:
            if self.currenIndex == 2:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 3:
                menu01()
                self.currentMenu = 1
                
        elif self.currentMenu == 7:
            if self.currenIndex == 0:
                menu08()
                self.currentMenu = 8
            elif self.currentIndex == 1:
                menu10()
                self.currentMenu = 10
            elif self.currentIndex == 2:
                menu12()
                self.currentMenu = 12
            elif self.currentIndex == 3:
                menu03()
                self.currentMenu = 3
                
        elif self.currentMenu == 8:
            menu09()
            self.currentMenu = 9
        
        elif self.currentMenu == 9:
            menu07()
            self.currentMenu = 7
        
        elif self.currentMenu == 10:
            menu01()
            self.currentMenu = 11
                    
        elif self.currentMenu == 11:
            menu07()
            self.currentMenu = 7
        
        elif self.currentMenu == 12:
            menu07()
            self.currentMenu == 7
            
    def down(self):
        if self.currentMenu == 1:
            if self.currenIndex == 0:
                self.currentIndex == 1:
            
        elif self.currentMenu == 3:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
                
        elif self.currentMenu == 5:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
                
        elif self.currentMenu == 6:
            if self.currenIndex == 2:
                self.currentIndex = 3
                
        elif self.currentMenu == 7:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
                
    def right(self):            
                
        if self.currentMenu == 4:
            menu12()
            self.currentMenu = 12
                
        elif self.currentMenu == 12:
            menu01()
            self.currentMenu = 1
            
    def left(self):            
                
        if self.currentMenu == 12:
            menu04()
            self.currentMenu = 4
                


menu01()
display.lcd_display_string('>', 0)

while True:
    
    # button = input('1 = sel, 2 = down, 3 = right, 4 = left')   
    if button == 1:
        button = 0
        display.update('s')

    if button == 2:
        button = 0
        display.update('d')

    if button == 3:
        button = 0
        display.update('r')

    if button == 4:
        button = 0
        display.update('l')
    
    button = 0
            
            


# In[ ]:




