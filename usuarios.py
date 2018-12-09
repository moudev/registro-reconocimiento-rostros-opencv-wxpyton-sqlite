# -*- coding: utf-8 -*- 



import wx
import wx.xrc
import os,shutil
import sqlite3
import cv, cv2
import subprocess
import sqliteclass
import fotografia

###########################################################################
## Class Registro
###########################################################################
class Registro ( wx.Frame ):
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
		
		#===================================================
		# Añadiendo imagen a Bitmap
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
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(self.width),int(self.height)), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 0, int(self.height)*0.30), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 200, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.25 , 0), 1, wx.EXPAND, 5 )
		
	
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txt_nombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		
		fgSizer2.Add( self.txt_nombre, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.25  , 0), 1, wx.EXPAND, 5 )
		
		self.user = wx.StaticText( self, wx.ID_ANY, u"Apellido:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user.Wrap( -1 )
		fgSizer2.Add( self.user, 0, wx.ALL, 5 )
		
		self.txt_apellido = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_apellido, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.25  , 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txt_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dir, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Telefono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txt_tel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_tel, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"DUI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_dui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dui, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"NIT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		self.txt_nit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_nit, 0, wx.ALL, 5 )
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Cargo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txt_cargo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_cargo, 0, wx.ALL, 5 )
		
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer ( (int(self.width)*0.05, int(self.height)*0.10), 1, wx.EXPAND, 5 )
		fgSizer3.AddSpacer ( (0,0), 1, wx.EXPAND, 5 )

		fgSizer3.AddSpacer ( (0,0), 1, wx.EXPAND, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( int(self.width)*0.30,int(self.height)*0.30 ), 0)
		fgSizer3.Add( self.m_bitmap1, 0, wx.ALL, 5 )
	
		
		fgSizer3.AddSpacer( (0, int(self.height)*0.09), 1, wx.EXPAND, 5 )
	
		
		self.btn_foto = wx.Button( self, wx.ID_ANY, u"Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btn_foto, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
				
		fgSizer4 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
	
		fgSizer4.AddSpacer( ( int(self.width)*0.05,0) ,1, wx.EXPAND, 5 )
		self.btn_guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_guardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		fgSizer4.AddSpacer( ( int(self.width)*0.05,0) ,1, wx.EXPAND, 5 )
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_cancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		
		#connect events
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.Guardar )
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.Cancelar )
		self.btn_foto.Bind( wx.EVT_BUTTON, self.Foto )
		self.Bind( wx.EVT_ACTIVATE, self.actualizarBitmap ) #Verifica si hay imagen temporal de usuario o no
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		# fin de codigo autogenerado por wxFormBuilder
		
		self.padre = parent
		self.padre.m_button2.Disable()
		# agregada la conexion a la base de datos
		self.db = sqliteclass.Database("db_registro.sqlite")
		
		
	def __del__( self ):
		self.padre.m_button2.Enable()
		
		
	# evento para cerrar el formulario
	def Cancelar( self, event ):
		self.padre.m_button1.Enable()
		self.Close()
		
		
	# evento para tomar una foto del nuevo usuario creando objeto del archivo fotografia.py
	def Foto(self,event):
		foto = fotografia.Fotografia(self)
		foto.Show()

	# guardar los datos de la persona leidos de los campos de texto en la base de datos
	def Guardar(self,event):
		
		#obtenemos los datos de los campos de texto
		nombre = self.txt_nombre.GetValue()
		apellido = self.txt_apellido.GetValue()
		direccion = self.txt_dir.GetValue()
		telefono = self.txt_tel.GetValue()
		dui = self.txt_dui.GetValue()
		nit = self.txt_nit.GetValue()
		cargo = self.txt_cargo.GetValue()
		
		#Primero se ingresa un registro vacio, para asi asegurarnos que el nombre de la imagen concuerde con
		#el ID del usuario, ya que si ingresamos de una sola vez, el contador interno de la base de datos
		#llevara una secuencia, que sera distinta al ID mas alto ingresado y que esta con registros,
		#ya que se renombra a la imagen temporal, con el ultimo ID mas alto registrado +1
		
		sql1= "INSERT INTO usuarios(nombre,apellido,direccion) VALUES ('', '','')"
		data_param=("")
		typesql='I'
		self.db.query(sql1, data_param, typesql)
		
		
		#Luego obtenemos el nombre de la Imagen, que se obtiene sacando el ID mas alto registrado
		#que se ingreso con el INSERT anterior
		self.jpg = self.nombreImg()
		self.ultimo = self.ultimoId()
		
		# insertamos los datos en la base de datos
		param = {'nombrem':nombre,'apelm':apellido,'direcm':direccion,'telefm':telefono,'duim':dui,'nitm':nit,'cargom':cargo,'jpg':self.jpg,'id_seleccionado':self.ultimo}
		sql=""" UPDATE usuarios SET nombre=:nombrem, apellido=:apelm, direccion=:direcm, telefono=:telefm, dui=:duim, nit=:nitm, cargo=:cargom , imagen=:jpg WHERE id_usuario=:id_seleccionado"""				
		typesql='U'
		if self.db.query(sql, param, typesql):
			self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS CON EXITO', 'Info', wx.OK|wx.CENTRE)
			if self.guardarImg(): #Movemos la imagen en dado que exista una temporal
				if self.dial.ShowModal() == wx.ID_OK:
					self.Close()
			else:
				self.dial = wx.MessageDialog(None, 'IMAGEN NO GUARDADA', 'ERROR', wx.OK|wx.CENTRE)
		else:
			self.dial = wx.MessageDialog(None, 'DATOS NO GUARDADOS VERIFIQUE BIEN SUS DATOS', 'ERROR', wx.OK|wx.CENTRE)
		
		
	
	#--- NOS PERMITE GUARDAR LA IMAGEN Y CREAR CARPETA EN DADO CASO NO EXISTA
	def guardarImg(self):
		self.user_png = self.nombreImg()
		ruta = str(os.getcwd())+"/usuarios"
		print ruta
		if os.path.exists(ruta):
			self.moverImg()
			return True
		else:
			os.mkdir("usuarios", 0o777)
			self.moverImg()
			return True
			
	#--- MUEVE NUESTRA IMAGEN TEMPORAL HACIA LA CARPETA DE USUARIOS
	def moverImg(self):
		if os.path.exists("orig_frame.jpg"):
			os.rename("orig_frame.jpg", self.user_png)
			if os.path.exists("usuarios/"+self.user_png):
				print "Habia imagen con el mismo usuario pero se a borrado"
				os.remove("usuarios/"+self.user_png)
				shutil.move(self.user_png ,"usuarios")
			else:
				shutil.move(self.user_png ,"usuarios")
			print "Movido y renombrado con exito"
		else:
			print "No existe foto de usuario para guardar"
		
	#--- OBTIENE EL ULTIMO ID MAS ALTO REGISTRADO EN LA BASE DE DATOS
	def ultimoId(self):
		sql="""select max(id_usuario) from usuarios """
		data_param=''
		typesql='S'
		self.datos = self.db.query(sql,data_param,typesql)	
		for dato in self.datos:
				self.id=dato[0]
				self.id=(str(self.id))
		
		return self.id
		
		
	#--- CREAMOS EL NOMBRE QUE TENDRA LA IMAGEN DEL USUARIO, SACANDO EL ID
	# MAS ALTO INGRESADO Y CONCATENANDO CON OTRAS CADENAS PARA FORMAR EL NOMBRE DE LA IMAGEN
	def nombreImg(self):
		id = self.ultimoId()
		name_img = "user"+id+".jpg"
		return name_img
	
	
	#--- PERMITE ACTUALIZAR EL BITMAP, SI HAY IMAGEN TEMPORAL, COLOCA ESA
	def actualizarBitmap(self, event):
		self.ruta="orig_frame.jpg"
		if os.path.exists(self.ruta):		
			self.ruta="orig_frame.jpg"
		else:
			self.ruta="imgs/blank_img.png"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		W = img.GetWidth()
		H = img.GetHeight()
		if W > H:
			NewW = self.ancho
			NewH = self.ancho * H / W
		else:
			NewH = self.ancho
			NewW = self.ancho * W / H
		img = img.Scale(NewW,NewH)
		self.m_bitmap1.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
