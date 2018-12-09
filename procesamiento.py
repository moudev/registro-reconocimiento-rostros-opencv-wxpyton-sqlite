# -*- coding: utf-8 -*- 


import wx
import wx.xrc
import os,sys
import cv, cv2
import numpy as np
import time
class Procesamiento ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Procesando imagenes para entrenamiento", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,300 ), wx.Size( 500,300 ) )
		
		gSizer1 = wx.GridSizer( 3, 3, 0, 0 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bit_map = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.bit_map, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"      Se esta procesando las imagenes de entrenamiento de cada usuario, \n               esto puede llevar varios minutos, espere porfavor.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.btn_confirmar = wx.Button( self, wx.ID_ANY, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_confirmar, 0, wx.ALL, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_cancelar, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.Cancelar )
		self.btn_confirmar.Bind( wx.EVT_BUTTON, self.Confirmar )
		
		self.padre = parent
		self.padre.m_button1.Disable()
		self.padre.m_button2.Disable()
		self.padre.m_button3.Disable()
		self.padre.m_button4.Disable()
		self.padre.m_button5.Disable()
		self.padre.m_button6.Disable()
		
		
	#--- FUNCION QUE SE ACTIVA AL CONFIRMAR QUE QUEREMOS ENTRENAR EL SISTEMA CON LOS NUEVOS USUARIOS AGREGADOS --#
	def Confirmar(self,event):
		if self.entrenar():
			caja_dialogo = wx.MessageDialog(None, 'ENTRENAMIENTO REALIZADO CON EXITO', 'Exito', wx.OK | wx.ICON_QUESTION)
		else:
			caja_dialogo = wx.MessageDialog(None, 'NO SE PUDO REALIZAR EL ENTRENAMIENTO', 'Error', wx.OK | wx.ICON_QUESTION)
		if caja_dialogo.ShowModal() == wx.ID_OK:
			self.Close()
	
	
	
	def __del__( self ):
		self.padre.m_button1.Enable()
		self.padre.m_button2.Enable()
		self.padre.m_button3.Enable()
		self.padre.m_button4.Enable()
		self.padre.m_button5.Enable()
		self.padre.m_button6.Enable()
	
	
	
	
	# Virtual event handlers, overide them in your derived class
	def Cancelar( self, event ):
		self.Close()
	
	
	
	
	#--- FUNCION QUE LEE TODAS LAS IMAGENES DE LOS USUARIOS REGITRADOS --#
	"""
	En esta funcion lo que se hace es navegar entre las carpetas de los uaurios registrados.
	Primero accedemos a la carpeta principan de donde estan la foto de los usuarios, cada uno en su respectiva
	carpeta, con el nombre del ID del usuario.
	
	dirnames, es el listado completo de todas las carpetas, y subdirname es el nombre de la carpeta
	que se recorre en el for, luego de eso unimos el nombre de la carpeta raiz de la imagenes, con el nombre de la carpeta
	del usuario, teniendo asi la direccion de carpeta del usuario del for.
	Luego se listan todos los archivos dentro de la carpeta del usuario, que serian solametne las fotografias,
	10 que decidimos que fueran en el archivo "entrenamiento.py".
	
	Con opencv leemos cada imagen a la vez, y la convertimos a escala de grises, y se prosigue
	a que identifique si en la imagen hay rostro o no, si hay rostro le ordenamos que recorte la imagen
	con las dimensiones del rostro. 
	
	X = el listado de imagenes que contienen rostro,
	y = es el label, o identificador que estara relacionado con la imagen que recien se acaba de agregar
		al listado de rostros, esto para que siempre coincida con el numero de imagenes que hay en el listado.
		
	
	"""
	def read_images(self,path):
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		X, y = [],[]
		for dirname, dirnames, filenames in os.walk(path):
			
			for subdirname in dirnames:
				print "<----------------------------   id   ---------------->>>>>>>>>>>"
				
				print subdirname
				subject_path = os.path.join(dirname, subdirname)
				for filename in os.listdir(subject_path):
					try:
						#print filename
						print os.path.join(subject_path, filename)
						imagen=cv2.imread(os.path.join(subject_path, filename),cv2.IMREAD_GRAYSCALE)
						faces = face_cascade.detectMultiScale(imagen, 1.3, 5)
						if len(faces) >= 1:
							print "Rostro"
							(x, Y, w, h) = faces[0]
							face_region_of_interest = imagen[Y: Y + h, x: x + w]
							#nombre = "recorte-"+str(filename)
							#cv2.imwrite(os.path.join(subject_path, nombre),face_region_of_interest)
							X.append(face_region_of_interest)
							label =str(subdirname)
							y.append(label)
					except IOError, (errno, strerror):
						print "I/O error({0}): {1}".format(errno, strerror)
		return [X,y]#retorna el listado de imagenes, y el listado de labels, que son el id de cada usuario dentro de las carpetas


	
	#--- FUNCION PARA CREAR EL ARCHIVO QUE CONTIENE TODA LA DATA DE LOS USUARIOS DEL SISTEMA --#
	
	"""
	http://docs.scipy.org/doc/numpy/reference/generated/numpy.asarray.html
	
	En esta funcion recibimos los datos returnados en la lectura de imagenes.
	
	Tenemos que crear un objeto cv2.createLBPHFaceRecognizer, luego a ese objeto llamamos
	al metodo train, que como por parametros tenemos que pasar el listado de imagenes, y leugo el listado
	de labels, el objeto crea por completo toda la estructura del archivo xml, cabe recalcar que esta es la parte
	mas importante de todas, ya que es en donde se crea el archivo que contiene toda la informacion de los rostros,
	sin este xml seria imporsible saber quie esta enfrente de nuestra camara.
	
	Luego de entrenarlo, tenemos que decirle donde guardara toda esa informacion, y le especificamos que en el
	archivo 'individual_face.xml', si no está creado se crea, y de estar creado, este se actualiza
	con la informacion recien agregada. Y dependiendo de lo que retorna asi sera el mensaje en la funcion confirmar.
	"""
	def entrenar(self):
		[X,y] = self.read_images("yalefaces")
		y=np.asarray(y,dtype=np.int32)
		model = cv2.createLBPHFaceRecognizer()
		model.train(X, np.asarray(y))
		if model.save('individual_face.xml'):
			return False
		else:
			return True
	
	
