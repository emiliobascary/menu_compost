import lcddriver
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

display = lcddriver.lcd()
# display.lcd_display_string("UNRN Compostador",1,1)

buttons_list = [16, 17, 18, 19]
GPIO.setup(buttons_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global password_inicio
global inicar      # 0 para parar, 1 para iniciar
global pausar      # variable para indicar pausa de proceso

def buttonPressed(channel):
    global button
    if channel == 16:                  	#flag indicador de boton SEL presionado
		menu.update('s')
    elif channel == 17:	  				#flag indicador de boton DOWN presionado
		menu.update('s')
    elif channel == 18:	                #flag indicador de boton RIGHT presionado
		menu.update('s')
    elif channel == 19:                 #flag indicador de boton LEFT presionado
		menu.update('s')
		

for pin in buttons_list:
    GPIO.add_event_detect(pin, GPIO.RISING, callback=buttonPressed, bouncetime=150)

    
class menu:
    
    def __init__(self, currentIndex=0, currentMenu=0):
        self.currentIndex = currentIndex
        self.currentMenu = currentMenu
	
        
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
        menu02_text = ["Ingrese","password:","0123456789"]
        for i in range(3):
            display.lcd_display_string(menu02_text[i], i)
        
        #lcd.setCursor(position,3)
        display.lcd_display_string("*")
        i = 0

        if iniciar == 0:                               

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
                    

       
        else:                                           
            
            password_ingreso = []
            i = 0
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
        #menu visualizacion 1
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu04_text = [" Experimentacion"," en proceso"," Temp. :"," Hum. :"]
        for i in range(4):
            display.lcd_display_string(menu04_text[i], i)

    def menu05(self):
        #menu visualizacion 2
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu05_text = [" Experimentacion"," en proceso"," O2 :"," CO2 :"]
        for i in range(4):
            display.lcd_display_string(menu05_text[i], i)
    
    def menu06(self):
        #menu control
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu06_text = [" Iniciar"," Pausar"," Parar"," Volver"]
        for i in range(4):
            display.lcd_display_string(menu06_text[i], i)


    def menu07(self):
        #menu pausar
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu07_text = [" Experimentacion"," en pausa."," Reanudar"," Parar"]
        for i in range(4):
            display.lcd_display_string(menu07_text[i], i)
   
    def menu08(self):
        #menu configuracion
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex)
        menu08_text = [" Rango temp."," Rango O2"," Tiempo de medicion"," Volver"]
        for i in range(4):
            display.lcd_display_string(menu08_text[i])

    def menu09(self):
        #menu seleccionar temperatura minima
        display.lcd_display_string('Temp. Min. :', 0)
        display.lcd_display_string('             ^',1)
                 
        # flag = 0                               #agregar texto a display
        # rango_temp = [50,80]
        # global temp_min = 51
        
        # while(flag != 0):
            # if button == 2:
                # temp_min -=1
                # if temp_min == rango_temp[0]:
                    # temp_min = rango_temp[1]
            # if button == 1:
                # flag = 1
                

    def menu10(self):
        #menu seleccionar temperatura maxima
        display.lcd_display_string('Temp. Max. :', 0)
        display.lcd_display_string('             ^', 1)
        
        # flag = 0                               #agregar texto a display
        # rango_temp = [50,90]
        # global temp_max = 89
        
        # while(flag != 0):
            # if button == 2:
                # temp_max -=1
                # if temp_max == rango_temp[0]:
                    # temp_max = rango_temp[1]
            # if button == 1:
                # flag = 1

    def menu11(self):
        #menu seleccionar oxigeno minimo
        display.lcd_display_string('O2 Min. :', 0)
        display.lcd_display_string('          ^', 1)

    def menu12(self):
        #menu seleccionar oxigeno maximo
        display.lcd_display_string('O2 Max. :', 0)
        display.lcd_display_string('          ^', 1)

    def menu13(self):
        #menu seleccionar intervalo de medicion
        display.lcd_display_string('Tiempo: ', 0)
        display.lcd_display_string('        ^', 1)

        
    #actualizacion de menu   
    def update(self, command):
        
        if command == 's':
            self.select()
        elif command == 'd':
            self.down()
        elif command == 'r':
            self.right()
        elif command == 'l':
            self.left()
    
    
    def select(self):
        
        if self.currentMenu == 1:
            if self.currenIndex == 0:
                menu02()
                self.currentMenu = 2
            elif self.currentIndex == 1:
                menu03()
                self.currentMenu = 3
                self.currentIndex = 0
                
        elif self.currentMenu == 2:
            menu03()
            self.currentMenu = 3
            self.currentIndex = 0
            
        elif self.currentMenu == 3:
            if self.currenIndex == 0:
                menu04()
                self.currentMenu = 4
            elif self.currentIndex == 1:
                menu06()
                self.currentMenu = 6
            elif self.currentIndex == 2:
                menu08()
                self.currentMenu = 8
            elif self.currentIndex == 3:
                menu01()
                self.currentMenu = 1
                self.currentIndex = 0
                
        elif self.currentMenu == 6:
            if self.currenIndex == 0:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 1:
                menu07()
                self.currentMenu = 7
                self.currentIndex = 2
            elif self.currentIndex == 2:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 3:
                menu05()
                self.currentMenu = 5
                
        elif self.currentMenu == 7:         #por ahora parece que hace lo mismo sin impotar el indice, pero falta agregar logica
            if self.currenIndex == 2:
                menu01()
                self.currentMenu = 1
            elif self.currentIndex == 3:
                menu01()
                self.currentMenu = 1
                
        elif self.currentMenu == 8:
            if self.currenIndex == 0:
                menu09()
                self.currentMenu = 9
            elif self.currentIndex == 1:
                menu11()
                self.currentMenu = 11
            elif self.currentIndex == 2:
                menu13()
                self.currentMenu = 13
            elif self.currentIndex == 3:
                menu03()
                self.currentMenu = 3
                self.currentIndex = 0
                
        elif self.currentMenu == 9:
            menu09()
            self.currentMenu = 9
        
        elif self.currentMenu == 10:
            menu08()
            self.currentMenu = 8
        
        elif self.currentMenu == 11:
            menu11()
            self.currentMenu = 11
                    
        elif self.currentMenu == 12:
            menu08()
            self.currentMenu = 8
            self.currentIndex = 0
        
        elif self.currentMenu == 13:
            menu08()
            self.currentMenu == 8
        
        
    def down(self):
        
        if self.currentMenu == 1:
            if self.currenIndex == 0:
                self.currentIndex = 1
            else: self.currentIndex = 0
            
        elif self.currentMenu == 3:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            else:
                self.currentIndex = 0
                
        elif self.currentMenu == 6:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            else:
                self.currentIndex = 0
         
        elif self.currentMenu == 7:
            if self.currenIndex == 2:
                self.currentIndex = 3
            else:
                self.currentIndex = 2
        
        elif self.currentMenu == 8:
            if self.currenIndex == 0:
                self.currentIndex = 1
            elif self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            else:
                self.currentIndex = 0
         
        
    def right(self):            

        if self.currentMenu == 4:
            menu05()
            self.currentMenu = 5
                
        elif self.currentMenu == 5:
            menu05()
            self.currentMenu = 1
            self.currentIndex = 0
     
    
    def left(self):            
                
        if self.currentMenu == 5:
            menu04()
            self.currentMenu = 4
                

    
compost = menu()
# display.lcd_display_string('>', 0)

while True:
     
	pass
    # if button == 1:
        # button = 0
        # menu.update('s')

    # if button == 2:
        # button = 0
        # menu.update('d')

    # if button == 3:
        # button = 0
        # menu.update('r')

    # if button == 4:
        # button = 0
        # menu.update('l')
    
            
            