
# -*- coding: utf-8 -*- 


import wx
import time
import os,shutil
import os.path
import cv, cv2
import time
import traceback
import subprocess
import threading


class Entrenamiento ( wx.Frame ):
	def __init__(self, parent,  fps=7):
		
		#Llamado al archivo en donde se encuentra la informacion de deteccion de rostros
		self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		
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
		self.ancho_pantalla, self.alto_pantalla = resolucion.split('x')
		self.ancho_pantalla = int(self.ancho_pantalla)
		self.alto_pantalla  = int(self.alto_pantalla)
		#===================================================
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(self.ancho_pantalla), int(self.alto_pantalla) ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, (int(self.ancho_pantalla),int(self.alto_pantalla)), wx.TAB_TRAVERSAL )

		#==================================================
		#OBTENIEDO IMAGEN DE LA CAMARA, E INICIALIZANDOLA
		#==================================================

		capture = cv2.VideoCapture(0)
		self.capture = capture
		ret, self.frame = self.capture.read()
		height, width = self.frame.shape[:2]
		parent.SetSize((width, height))
		self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
		self.bmp = wx.BitmapFromBuffer(width, height, self.frame)
		#==================================================
		
		#===================================================
		# Aadiendo imagen a Bitmap
		#===================================================
		
		self.ruta="orig_frame.jpg"
		if os.path.exists(self.ruta):
			os.remove(self.ruta)
			self.ruta="imgs/blank_img.png"
		else:
			self.ruta="imgs/blank_img.png"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.ancho = 150
		self.alto = 200
		
		#===================================================
		
		
		#==================================================
		#INICIALIZANDO CONTADORES
		#==================================================
		
		self.contador = 1
		self.mostrar_en_pantalla = 1
		
		#==================================================
	
		
		
		
		self.timer = wx.Timer(self) #Encargado de actualizar la toma de la camara
		self.timer2 = wx.Timer(self)#Encargado de llevar tiempo de cada cuanto tomar una foto
		
		self.timer.Start(1000./fps)


		#==================================================
		#EVENTOS PARA TEMPORIZADORES
		#==================================================


		self.Bind(wx.EVT_TIMER, self.hilo_app,self.timer)
		self.Bind(wx.EVT_TIMER, self.fotografias_entrenamiento,self.timer2)
		
		#==================================================
	
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmap_principal = wx.StaticBitmap( self.panel, wx.ID_ANY, self.bmp, (int(self.ancho_pantalla/2),int(self.alto_pantalla/2)), (int(self.ancho_pantalla*0.35),int(self.alto_pantalla*0.35)), 0 )
		bSizer1.Add( self.bitmap_principal, 0, wx.ALL, 5 )
		
		self.btn_foto = wx.Button( self.panel, wx.ID_ANY, u"Captura", wx.DefaultPosition,wx.DefaultSize  , 0 )
		bSizer1.Add( self.btn_foto, 0, wx.ALL, 5 )
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.bitmap1 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap1, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap2 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap2, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap3 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition,  (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap3, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap4 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition,  (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap4, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap5 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition,  (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap5, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap6 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap6, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap7 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap7, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap8 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition,  (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap8, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap9 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap9, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bitmap10 = wx.StaticBitmap( self.panel, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, (int(self.ancho_pantalla*0.10),int(self.alto_pantalla*0.15)), 0 )
		gSizer1.Add( self.bitmap10, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.btn_captura = wx.Button( self.panel, wx.ID_ANY, u"Entrenar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_captura, 0, wx.ALL, 5 )
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_foto.Bind( wx.EVT_BUTTON, self.iniciar_hilo )
		self.btn_captura.Bind( wx.EVT_BUTTON, self.entrenar)
		
		self.padre =  parent
	
	
	#--- FUNCION ENCARGADA DE GUARDAR LAS FOTOS TEMPORALES DE LA SECUENCIA DE FOTOS---#
	
	"""
	Esta funcion lo que realiza es que cada 3 segundos toma una fotografia, 
	está relacionado con el timer2, que se inicia en la funcion 'iniciar_hilo',
	se a puesto que se tomen 10 fotografias para luego entrenar el archivo xml, pero
	pueden ser la cantidad que se deseen, en este caso solamente hay 10 bitmaps, pero porqe se muestran
	las fotografias en cada bitmap...
	
	Cuando el contador llegue a 11 detiene el timer para no seguir tomando fotografias, el nombre
	de la imagen se genera con el mismo contador. La bandera mostrar_en_pantalla sirve para saber
	si actualizar el bitmap o no, al momento de iniciar la toma de fotografia le decimos que deje de
	actualizarlo, ya que se mostrara una secuencia de imagenes numeradas del 1-10, para saber la secuencia,
	estas imagenes se mostraran en el bitmap principal.
	"""
	def fotografias_entrenamiento(self,event):
		if self.contador == 11:
			self.timer2.Stop()
			self.contador = 1 
			self.mostrar_en_pantalla = 1
		else:
			try:
				name_foto = str("origin_frame%i.jpg")%self.contador #generando el nombre de la imagen temporal
				
				name_pantalla = str("imgs/%i.png")%int(self.contador)#haciendo el nombre de la imagen de la secuencia
																	#que se mostrará, estas ya estan creadas	
				print name_foto
				self.mostrar_secuencia(name_pantalla)				#Mostrando la secuencia, con la funcion.
				cv2.imwrite(name_foto, self.imagen_guardar)			#Guardando la imagen temporal
				self.actualizarBitmap(name_foto,self.contador)		#Actualizando el bitmap segun el bitmap correspondiente
				self.contador+=1									#Aumenta el contador
			except AttributeError:
				traceback.print_exc()
	
	
	#--- FUNCION ENCARGADA DE INICIAR TIMER PARA LA CAPTURA DE FOTOS ---#
	def iniciar_hilo(self,event):
		self.timer2.Start(3000)
		self.mostrar_en_pantalla = 0
	
	
	#--- FUNCION ENCARGADA DE MOSTRAR LAS IMAGENES DE LA SECUENCIA ---#
	def mostrar_secuencia(self,ruta):
		self.PhotoMaxSize = 200
		self.ruta = ruta
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		W = img.GetWidth()
		H = img.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = img.Scale(NewW,NewH)
		self.bitmap_principal.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
		
	
	
	#--- FUNCION ENCARGADA DE EMPEZAR A ALMACENAR LAS FOTOGRAFIAS RECIEN TOMADAS  ---#
	def entrenar( self, event ):
		if self.guardarImg(self.padre.id_user): #recuperando ID de usuario traido desde el formulario padre que es el de busqueda
			caja_dialogo = wx.MessageDialog(None, 'Imagenes Guardadas con Exito para su posterior Entrenamiento', 'Exito', wx.OK | wx.ICON_QUESTION)
		else:
			caja_dialogo = wx.MessageDialog(None, 'No se guardaron las imagenes, porfavor intente de nuevo', 'Error', wx.OK | wx.ICON_QUESTION)
		if caja_dialogo.ShowModal() == wx.ID_OK:
			self.Close()
			
			
	#--- FUNCION ENCARGADA DE INICIAR HILO PARA MOSTRAR EN BITMAP LA CAPTURA DE LA CAMARA ---#
	def hilo_app(self, event):
		hilo = threading.Thread(target=self.NextFrame(self))
		hilo.setDaemon(True)
		hilo.start()
		

	#--- FUNCION ENCARGADA DE ACTUALIZAR EL BITMAP, VA JUNTO CON TIMER---#
	def NextFrame(self, event):
		ret, self.imagen_guardar = self.capture.read()
		if ret:
			self.frame = cv2.cvtColor(self.imagen_guardar, cv2.COLOR_BGR2RGB)
			frame2 = cv2.cvtColor(self.imagen_guardar, cv2.COLOR_BGR2GRAY)
			if self.mostrar_en_pantalla == 1:
				self.bmp.CopyFromBuffer(self.frame)			
				self.Refresh()
			
	#--- FUNCION ENCARGADA DE GUARGAR TODAS LAS IMAGENES DE LA SECUENCIA ---#
	
	"""
	Esta funcion lo que hace es verificar si hay una carpeta con el nombre del usuario
	en este caso con el nombre del ID del usuario, que se trae desde el formulario de busqueda
	en la funcion 'entrenamiento', si no hay carpeta con el ID del usario pues crea una y ahi va guardando
	las fotografias, y por cada imagen guardada correctamente aumenta un contador, para que solamente sea un
	exito cuando se han guardado correctametne todas la imagenes.
	"""
	def guardarImg(self, id_user):
		ruta = str(os.getcwd())+"/yalefaces/"+str(id_user)
		exito = 0
		print ruta
		if os.path.exists(ruta):
			for i in range(1,11):
				self.moverImg(i,ruta,id_user)
				exito=exito+1
		else:
			ruta = "yalefaces/"+str(id_user)
			os.mkdir(ruta, 0o777)
			for i in range(1,11):
				self.moverImg(i,ruta,id_user)
				exito=exito+1
		if exito == 10:
			return True
		else:
			False
			
			
	#--- FUNCION ENCARGADA DE MOVER Y RENOMBRAR LAS IMAGENES DE LA SECUENCIA ---#
	
	"""
	Esta funcion lo que hace es que verifica si hay una imagen temporal de la secuencia,
	si la hay entonces concatena, el parametro del id del usuario con el numero de foto que es, mas su extencion.
	
	Si existe la elimina y sustituye por la nueva fotografia, en la ruta que es ....  yalefaces/ID_USUARIO/
	"""
	def moverImg(self,iteracion,ruta,id_user):
		img = "origin_frame%i.jpg"%iteracion
		self.ruta = str(ruta )
		img_entrenamiento = str(id_user)+"-"+str(iteracion)+".jpg"
		if os.path.exists(img):
			os.rename(img, img_entrenamiento)
			if os.path.exists(self.ruta+"/"+img_entrenamiento):
				print "Habia imagen con el mismo usuario pero se a borrado"
				os.remove(self.ruta+"/"+img_entrenamiento)
				shutil.move(img_entrenamiento ,self.ruta)
			else:
				shutil.move(img_entrenamiento ,self.ruta)
			print "Movido y renombrado con exito"
		else:
			print "No existe foto de usuario para guardar"
			
			
			
			
	#--- FUNCION ENCARGADA DE ACTUALIZAR CADA BITMAP DE LA SECUENCIA DE FOTOS ---#
	def actualizarBitmap(self,ruta,bi_ma):
		self.PhotoMaxSize = 150
		self.ruta=ruta
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		W = img.GetWidth()
		H = img.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = img.Scale(NewW,NewH)
		if bi_ma == 1:
			self.bitmap1.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 2:
			self.bitmap2.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 3:
			self.bitmap3.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 4:
			self.bitmap4.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 5:
			self.bitmap5.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 6:
			self.bitmap6.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 7:
			self.bitmap7.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 8:
			self.bitmap8.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 9:
			self.bitmap9.SetBitmap(wx.BitmapFromImage(img))
		elif bi_ma == 10:
			self.bitmap10.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
		print "Se actualizo el bitmap %i"%bi_ma
		
		
	def __del__(self):
		pass
		
