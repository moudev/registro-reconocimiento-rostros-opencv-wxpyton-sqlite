
# -*- coding: utf-8 -*- 


import wx
import wx.xrc
import subprocess
import busqueda
import usuarios
import procesamiento
import cv, cv2
import threading
import os
import datos_individuales
###########################################################################
## Class Menu
###########################################################################

class Menu ( wx.Frame ):
	
	def __init__( self, parent ):
		
		
		
		#===================================================
		# Obteniendo ancho y alto de la pantalla
		#===================================================
		inst = ['xrandr']
		inst2 = ['grep', '*']
		p1 = subprocess.Popen(inst, stdout=subprocess.PIPE)
		p2 = subprocess.Popen(inst2, stdin=p1.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()
		resolucion_scren,junk = p2.communicate()
		resolucion = resolucion_scren.split()[0]
		self.width, self.height = resolucion.split('x')
		#===================================================
		
		
		
		#variables para redimension de imagen, al cambiar estos valores cambia la dimension
		self.ancho = 75
		self.alto = 150
		
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(self.width),int(self.height) ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.AddSpacer ( (int(self.width)*0.35, int(self.height)*0.10), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		
		self.m_button1 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/add_user.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( int(self.width)*0.12, int(self.height)*0.26), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/busqueda.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/refrescar.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, int(self.height)*0.26), 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/face.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button5 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/add_user.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button6 = wx.BitmapButton( self, wx.ID_ANY, wx.BitmapFromImage(self.redimension("imgs/exit.png")), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		
		
		
		#connect events
		self.m_button6.Bind( wx.EVT_BUTTON, self.salir )
		self.m_button1.Bind( wx.EVT_BUTTON, self.hilo_formulario_registro )
		self.m_button2.Bind( wx.EVT_BUTTON, self.busqueda )
		self.m_button3.Bind( wx.EVT_BUTTON, self.entrenar )
		self.m_button4.Bind( wx.EVT_BUTTON, self.inicio_hilo_reconocimiento )
		
		self.padre = parent
		self.padre.Hide()
		self.frm_busqueda = ""
		
		
		
		
		
		# fin de codigo autogenerado por wxFormBuilder
	def __del__( self ):
		pass
		
		
	# funcion para ajustar las imagenes
	def redimension(self, ruta):
		img = wx.Image(ruta, wx.BITMAP_TYPE_ANY)
		W = img.GetWidth()
		H = img.GetHeight()
					
		if W > H:
			NewW = self.ancho
			NewH = self.ancho * H / W
		else:
			NewH = self.ancho
			NewW = self.ancho * W / H
		img = img.Scale(NewW,NewH)
		return img
		
		
	# cerrar el formulario
	def salir (self, event):
		self.Close()
		
		
	# abrir el formulario de busqueda, edicion y eliminacion de registros
	def busqueda (self, event):
		self.frm_busqueda = busqueda.Busqueda(self)
		self.frm_busqueda.Show(True)
		
		
	# abrir el formulario de registro
	def registro (self):
		self.frm_registro = usuarios.Registro(self)
		self.frm_registro.Show(True)
		print "Fin de hilo de formualrio de registro"	
	
	# abrir el formulario de entrenamiento, con las imagenes recient tomadas de un usuario
	def entrenar(self,event):
		entren = procesamiento.Procesamiento(self)
		entren.Show(True)
		
	def hilo_formulario_registro(self,event):
		print "Hilo der formulario de registro"
		hilo = threading.Thread(target = self.registro())
		hilo.setDaemon(True)
		hilo.start()
	
	def inicio_hilo_reconocimiento(self,event):
		hilo = threading.Thread(target = self.reconocer())
		hilo.setDaemon(True)
		hilo.start()
		
	def imprimir(self):
		print "Imprimiendo"
		
		
		
	#--- FUNCION PARA RECONOCIMIENTO DE ROSTROS --#
	
	"""
	Esta funcion es la encargada de reconocer un rostro, si es que esta registrado o no,
	los rostros registrados se encuentran en el archivo 'individual_face.xml', dentro de el están
	todos los rostros con los cual es sistema está entrenado, primero se crea un objeto cv2.createLBPHFaceRecognizer,
	que sera el encargado de revisar nuestro xml, y posteriormente encontrar el xml, esto lo hacemos con os.path, que nos sirve
	para navegar entre las direcciones de nuestros direcctorios, y concatenando con join.
	
	Luego cargamos el xml con face_recognizer.load, para cargar toda la data del archivo, pasandole como parametro el 
	xml el cual está entrenado. Luego de eso necesitamos un xml que nos ayude a detectar cuando un rostro está en frente
	de la cámara, y este xml es 'haarcascade_frontalface_default.xml', ahora solo queda activar la cámara para que esta
	vaya leyendo frame a frame nuestra captura, con cv2.VideoCapture.
	
	Se tiene 3 variables; 
		-precision = esta variable indicará el nivel de precision que tiene la captura que se está realizando
					con los rostros registrados en el xml, 'individual_face.xml'
					
		-tiempo = es una flag booleana, su valor inicial será True para poder empezar el while,
					el valor de esta flag cambiará, cuando el valor de la variable precision
					esté en el rango de 0 a 45.
					
		- id = esta variable almacenara el id del usuario encontrado para luego realizar la busquedad de él,
				a nuestra base de datos con su ID.
					
	
	Ahora se procese a la captura de la imagen, que se almacena en img, para poder detectar rostros hay que convertir la imagen
	a escala de grises con cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), luego se tiene que verificar si hay rostros o no
	dentro de la captura, con el objeto face_cascade, y las almacena en la variable faces.
	
	Si detecta un rostro lo que hace es recortar justo en la zona en donde se a detectado,
	luego se pasa al fase de tratar de reconocer si el rostro encontrado coincide con unos de con los
	cuales tenemos entrenado en individual_face.xml.
	
	Luego de ver si coincide con uno de los rostros entrenados, tenemos que saber su nivel de confianza, o meor dicho precision
	... esto se sabe con los valores que retorna self.face_recognizer.predict(face_region_of_interest),
	tomamos el valor de precision, y si está en el rango de 0 a 45 le decimos que cambie la flag tiempo a False,
	cuando cambie a False le decimos que guarde el label del rostro, y que al cambiar tiempo de valor
	que nos muestre un formulario con los datos del usuario, en este caso que lo guarde en una variable y que nos abra el formulario,
	el formualrio a abrir luego recoge el valor de ese ID y hace la busqueda.
	"""	
	def reconocer(self):
		self.face_recognizer = cv2.createLBPHFaceRecognizer()
		train_face_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'individual_face.xml')
       
		self.face_recognizer.load(train_face_filepath)
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		cap = cv2.VideoCapture(0)
		print("Identifying your face!")
		precision = 0
		tiempo = True
		id = 0
      
		while tiempo:
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			self.frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			if len(faces)==1:
				print "hay un rostro"
				for (x, y, w, h) in faces:
					#cv2.rectangle(self.frame, (x,y), (x+w, y+h), (125,255,0), 2)
					face_region_of_interest = gray[x:x+w, y:y+h]
					label , precision = self.face_recognizer.predict(face_region_of_interest)
					if precision>=0 and precision<=100:
						print "Vaya estas registrado :D"
						id = str(label)
						tiempo = False
					print('Estimated Trained Face : {}, {}'.format( label,precision))
					#cv2.imshow('FACE', self.frame)
				cv2.destroyAllWindows()
			else:
				print "No hay rostros"
		if tiempo == False:
			print "Encontrado"
			self.id_user = id
			datos = datos_individuales.Datos(self) #llamando al archivo en donde se encuentra el formulario para mostrar el registro
			datos.Show()

