import lcddriver
import time
import RPi.GPIO as GPIO
from adquisition import COMPOSTtemperature
GPIO.setmode(GPIO.BCM)

display = lcddriver.lcd()

led_list = [5, 6, 13]
for j in range(len(led_list)):
	GPIO.setup(led_list[j], GPIO.OUT)
	
buttons_list = [16, 19, 20, 26]
for j in range(len(buttons_list)):
	GPIO.setup(buttons_list[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonPressed(channel):
    if GPIO.input(16):
        compost.update('s')
    elif GPIO.input(19):
        compost.update('d')
    elif GPIO.input(20):
        compost.update('r')
    elif GPIO.input(26):
        compost.update('l')

for j in range(len(buttons_list)):		
	GPIO.add_event_detect(buttons_list[j], GPIO.RISING, callback = buttonPressed, bouncetime = 150)

global pausar

def test_adquisition():
	temp=COMPOSTtemperature()
	count=temp.device_count()
	tempSuma = 0
	while i < count:
		tempSuma += temp.tempC(i)
		i += 1
	tempPromedio = tempSuma / count
	return tempPromedio

class menu:

    def __init__(self, currentIndex = 1, currentMenu = 1):
        self.currentIndex = currentIndex
        self.currentMenu = currentMenu
        display.lcd_clear()
        display.lcd_display_string("Compostador", 1, 5)
        display.lcd_display_string("UNRN", 2, 8)
		display.lcd_display_string("Iniciando...", 4, 5)
        time.sleep(3)
        display.lcd_clear()

    def menu01(self):
        #menu inicio, admin/visita
        display.lcd_clear()
        menu01_text = ["Admin","Visita"]
        display.lcd_display_string('>', self.currentIndex, 1)
        for i in range(2):
            display.lcd_display_string(menu01_text[i], i+1, 2)

    def menu02(self, command = 0):
        #menu ingrese password
        display.lcd_clear()
        menu02_text = ["Ingrese","password:","0123456789"]
        for i in range(3):
            display.lcd_display_string(menu02_text[i], i+1,1)


        asteriscos = ["*","**","***","****"]
        
        if iniciar == 0: 
            if command == 1:
                global j
                global position
                j += 1
                password_inicio[j-1] = position
                display.lcd_display_string(asteriscos[j-1], 2, 11+j)
            elif command == 3:
                position += 1
                if position == 10:
                    position = 0
            elif command == 4:
                position -= 1
                if position == -1:
                    position = 9
            display.lcd_display_string(" ^ ", 4, position)
            command = 0

            if j == 4:
                global iniciar
                display.lcd_clear()
                for i in range(4):
                    display.lcd_display_string("%d" % password_inicio[i], 1, i+1)
                sleep(2)
                self.menu03()
                self.currentMenu = 3
                iniciar = 1
                position = 0
                j = 0
            
        elif iniciar == 1: 
            if command == 1:
                global j
                global position
                j += 1
                password_ingreso[j-1] = position
                display.lcd_display_string("%d" % j, 1, 15)
            elif command == 3:
                position += 1
                if position == 10:
                    position = 0
            elif command == 4:
                position -= 1
                if position == -1:
                    position = 9
            display.lcd_display_string(" ^ ", 4, position)
            command = 0

            if j == 4:
                if password_ingreso != password_inicio:
                    display.lcd_clear()
                    display.lcd_display_string('Password incorrecta.',1,1)
                    sleep(1)
                    self.menu01()
        
                else:
                    self.menu03()
                    self.currentMenu = 3
                    position = 0
                    j = 0


    def menu03(self):
        #menu visualizacion/control/configuracion/volver
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex, 1)
        menu03_text = ["Visualizacion","Control","Configuracion","Volver"]
        for i in range(4):
            display.lcd_display_string(menu03_text[i], i+1, 2)


    def menu04(self):
        #menu visualizacion 1
        display.lcd_clear()
        menu04_text = ["Experimentacion","en proceso...","Temp. :","Hum.  :"]
        for i in range(4):
            display.lcd_display_string(menu04_text[i], i+1, 1)
		flag = 0
		while flag == 0:
			display.lcd_display_string("          ", 3, 9)
			display.lcd_display_string("%.2f C" %test_adquisition(), 3, 9)
			timeInitial = time.time()
			timeFinal   = time.time()
			while( (timeFinal - timeInitial ) < tiempo_medicion ):
				timeFinal = time.time()
				if GPIO.input(16):
					self.update('s')
					flag = 1
				elif GPIO.input(20):
					self.update('r')
					flag = 1


    def menu05(self):
        #menu visualizacion 2
        display.lcd_clear()
        menu05_text = ["Experimentacion","en proceso...","O2  :","CO2 :"]
        for i in range(4):
            display.lcd_display_string(menu05_text[i], i+1, 1)
		flag = 0
		while flag == 0:
			display.lcd_display_string("          ", 3, 9)
			display.lcd_display_string("%.2f C" %test_adquisition(), 3, 9)
			timeInitial = time.time()
			timeFinal   = time.time()
			while( (timeFinal - timeInitial ) < tiempo_medicion ):
				timeFinal = time.time()
				if GPIO.input(16):
					self.update('s')
					flag = 1
				elif GPIO.input(20):
					self.update('r')
					flag = 1
				elif GPIO.input(26):
					self.update('l')
					flag = 1
					

    def menu06(self):
        #menu control
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex, 1)
        menu06_text = ["Iniciar","Pausar","Parar","Volver"]
        for i in range(4):
            display.lcd_display_string(menu06_text[i], i+1, 2)

    def menu07(self):
        #menu pausar
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex, 1)
        menu07_text = ["Experimentacion","en pausa.","Reanudar","Parar"]
        for i in range(4):
            display.lcd_display_string(menu07_text[i], i+1, 2)

    def menu08(self):
        #menu configuracion
        display.lcd_clear()
        display.lcd_display_string('>', self.currentIndex, 1)
        menu08_text = ["Rango temperatura","Rango O2","Tiempo de medicion","Volver"]
        for i in range(4):
            display.lcd_display_string(menu08_text[i], i+1, 2)

    def menu09(self, command = 0):
        #menu seleccionar temperatura minima
		display.lcd_clear()
        global temp_min
        display.lcd_display_string('Temp. Min. : %d' % temp_min, 1, 1)
        display.lcd_display_string('v', 2, 15)
        
        if command == 2:
            temp_min = temp_min - 1
            if temp_min == 45:
                temp_min = 60
        command = 0

    def menu10(self, command = 0):
        #menu seleccionar temperatura maxima
		display.lcd_clear()
        global temp_max
        display.lcd_display_string('Temp. Max. : %d' % temp_max, 1, 1)
        display.lcd_display_string('v', 2, 15)
        
        if command == 2:
            temp_max = temp_max - 1
            if temp_max == 60:
                temp_max = 80
        command = 0

    def menu11(self, command = 0):
        #menu seleccionar oxigeno minimo
		display.lcd_clear()
        global o2_min
        display.lcd_display_string('O2 Min. : %d' % o2_min, 1, 1)
        display.lcd_display_string('v', 2, 12)
        
        if command == 2:
            o2_min = o2_min - 1
            if o2_min == 200:
                o2_min = 220
        command = 0

    def menu12(self, command = 0):
        #menu seleccionar oxigeno maximo
		display.lcd_clear()
        global o2_max
        display.lcd_display_string('O2 Max. : %d' % o2_max, 1, 1)
        display.lcd_display_string('v', 2, 12)
        
        if command == 2:
            o2_max = o2_max - 1
            if o2_max == 300:
                o2_max = 320
        command = 0

    def menu13(self, command = 0):
        #menu seleccionar intervalo de medicion
		display.lcd_clear()
        global tiempo_medicion
		global tiempo_medicion_string
        global i
        tiempo_seleccion_string = ['30 minutos', '1 hora', '2 horas', '3 horas', '4 horas']
        tiempo_seleccion 		= [1800, 3600, 7200, 10800, 14400]
		
        if command == 2:
            i-=1
            if i == -1:
                i = (len(tiempo_seleccion) - 1)
			tiempo_medicion_string = tiempo_seleccion_string[i-]
            tiempo_medicion 	   = tiempo_seleccion[i]
        command = 0
        display.lcd_display_string("Tiempo: %s" % tiempo_medicion_string, 1, 1)
        display.lcd_display_string('v', 2, 12)
		display.lcd_display_string("Tiempo: %d" % tiempo_medicion, 1, 1)
        display.lcd_display_string('v', 4, 12)

    def indicator_leds(self, command = 2):
		#funcion indicando estado de compost a través de 3 leds (0 = iniciar, 1 = pausar, 2 = parar)
		GPIO.output(led_list, GPIO.LOW)
		GPIO.output(led_list[command], GPIO.HIGH)
		 
    def update(self, command):
        #actualizacion de menu  
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
            if self.currentIndex == 1:
                self.currentMenu = 2
                self.menu02()
            elif self.currentIndex == 2:
                self.currentMenu = 3
                self.currentIndex = 1
                self.menu03()
                
        elif self.currentMenu == 2:
            self.menu02(1)
            
        elif self.currentMenu == 3:
            if self.currentIndex == 1:
                self.currentMenu = 4
                self.menu04()
            elif self.currentIndex == 2:
                self.currentMenu = 6
                self.currentIndex = 1
                self.menu06()
            elif self.currentIndex == 3:
                self.currentMenu = 8
                self.currentIndex = 1
                self.menu08()
            elif self.currentIndex == 4:
                self.currentMenu = 1
                self.currentIndex = 1
                self.menu01()
		
		elif self.currentMenu == 4:
			self.currentMenu = 1
			self.menu01()
		
		elif self.currentMenu == 5:
			self.currentMenu = 1
			self.menu01()
		
        elif self.currentMenu == 6:
            if self.currentIndex == 1:
                self.currentMenu = 4
                self.menu04()
				self.indicator_leds(0)
            elif self.currentIndex == 2:
                self.currentMenu = 7
                self.currentIndex = 3
                self.menu07()
				self.indicator_leds(1)
            elif self.currentIndex == 3:
                self.currentMenu = 1
                self.menu01()
				self.indicator_leds(2)
            elif self.currentIndex == 4:
                self.currentMenu = 3
                self.currentIndex = 1
                self.menu03()
                
        elif self.currentMenu == 7:         #por ahora parece que hace lo mismo sin impotar el indice, pero falta agregar logica
            if self.currentIndex == 3:
                self.currentMenu = 1
                self.currentIndex = 1
                self.menu01()
				self.indicator_leds(0)
            elif self.currentIndex == 4:
                self.currentMenu = 1
                self.currentIndex = 1
                self.menu01()
				self.indicator_leds(2)
                
        elif self.currentMenu == 8:
            if self.currentIndex == 1:
                self.currentMenu = 9
                self.menu09()
            elif self.currentIndex == 2:
                self.currentMenu = 11
                self.currentIndex = 1
                self.menu11(0)
            elif self.currentIndex == 3:
                self.currentMenu = 13
                self.currentIndex = 1
                self.menu13()
            elif self.currentIndex == 4:
                self.currentMenu = 3
                self.currentIndex = 1
                self.menu03()
                
        elif self.currentMenu == 9:
            self.currentMenu = 10
            self.menu10(0)
        
        elif self.currentMenu == 10:
            self.currentMenu = 8
            self.menu08()
        
        elif self.currentMenu == 11:
            self.currentMenu = 12
            self.menu12(0)
                    
        elif self.currentMenu == 12:
            self.currentMenu = 8
            self.menu08()
        
        elif self.currentMenu == 13:
            self.currentMenu == 8
            self.menu08()

        else:
            pass
        
        
    def down(self):
        
        if self.currentMenu == 1:
            if self.currentIndex == 1:
                self.currentIndex = 2
            else: self.currentIndex = 1
            self.menu01()
            
        elif self.currentMenu == 3:
            if self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            elif self.currentIndex == 3:
                self.currentIndex = 4
            else:
                self.currentIndex = 1
            self.menu03()
                
        elif self.currentMenu == 6:
            if self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            elif self.currentIndex == 3:
                self.currentIndex = 4
            else:
                self.currentIndex = 1
            self.menu06()
         
        elif self.currentMenu == 7:
            if self.currentIndex == 3:
                self.currentIndex = 4
            else:
                self.currentIndex = 3
            self.menu07()
        
        elif self.currentMenu == 8:
            if self.currentIndex == 1:
                self.currentIndex = 2
            elif self.currentIndex == 2:
                self.currentIndex = 3
            elif self.currentIndex == 3:
                self.currentIndex = 4
            else:
                self.currentIndex = 1
            self.menu08()
        
        elif self.currentMenu == 9:
            self.menu09(2)
            
        elif self.currentMenu == 10:
            self.menu10(2)

        elif self.currentMenu == 11:
            self.menu11(2)

        elif self.currentMenu == 12:
            self.menu12(2)

        elif self.currentMenu == 13:
            self.menu13(2)
        
    def right(self):            
        if self.currentMenu == 2:
            self.menu02(3)
        elif self.currentMenu == 4:
            self.currentMenu = 5
            self.menu05()        
        elif self.currentMenu == 5:
            self.currentMenu = 1
            self.currentIndex = 1
            self.menu01()

    def left(self):     
        if self.currentMenu == 2:
            self.menu02(4)
        elif self.currentMenu == 5:
            self.currentMenu = 4
            self.menu04()
        elif self.currentMenu == 4:
            self.currentMenu = 4
            self.menu04()

compost = menu()
compost.menu01()
iniciar = 0
j=0
i=0
position=0
password_inicio=[1,2,3,4]
password_ingreso=[5,6,7,8]
temp_min=55
temp_max=70
o2_min=210
o2_max=310
tiempo_medicion_string='30 minutos'
tiempo_medicion=3600

def main():
    while True:
        pass


if __name__ == '__main__':
    try:
        main()
    except:
        pass
    finally:
        GPIO.cleanup()
         
