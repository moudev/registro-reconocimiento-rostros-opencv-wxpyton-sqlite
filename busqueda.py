# -*- coding: utf-8 -*- 



import wx
import wx.xrc
import subprocess
import os
import sqlite3
import sqliteclass
import shutil
import fotografia
import entrenamiento
###########################################################################
## Class Busqueda
###########################################################################
class Busqueda( wx.Frame ):
	def __init__( self, parent ):
		
		#===================================================
		# Añadiendo imagen a Bitmap
		#===================================================
		
		self.ruta="orig_frame.jpg"
		
		if os.path.exists(self.ruta):
			os.remove(self.ruta)
			self.ruta="imgs/blank_img.png"
		else:
			self.ruta="imgs/blank_img.png"
			print "NO existia imagen de usuario en el sistema"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.ancho = 150
		self.alto = 200
		
		#===================================================
		
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
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(self.width), int(self.height) ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer71 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( int(self.width)*0.02, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Busqueda:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txtbusquedad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer3.Add( self.txtbusquedad, 0, wx.ALL, 5 )
		
		
		fgSizer71.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer6.AddSpacer( ( int(self.width)*0.02, 0), 1, wx.EXPAND, 5 )
		
		self.tab_busqueda = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,450 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
		self.tab_busqueda.SetFont(wx.Font(10, 79, 90, 90, False, "Monospace"))
		
		fgSizer6.Add( self.tab_busqueda, 0, wx.ALL, 5 )
		
		
		fgSizer71.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( fgSizer71, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.05, 0), 1, wx.EXPAND, 5 )
		
		fgSizer81 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer7 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.imagen = wx.StaticBitmap( self, wx.ID_ANY,wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		fgSizer7.Add( self.imagen, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_foto = wx.Button( self, wx.ID_ANY, u"Fotografia Principal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.btn_foto, 0, wx.ALL, 5 )
		
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txtid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txtid.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtid, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txtnom = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtnom.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtnom, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txtape = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtape.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtape, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txtdireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtdireccion.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtdireccion, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txtphone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtphone.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtphone, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"DUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer7.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.txtdui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtdui.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtdui, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"NIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.txtnit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtnit.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtnit, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Cargo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txtcargo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtcargo.SetMinSize( wx.Size( 225,-1 ) )
		
		fgSizer7.Add( self.txtcargo, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer81.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		
		
		self.btnmodificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnmodificar, 0, wx.ALL, 5 )
		
		self.btneliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btneliminar, 0, wx.ALL, 5 )
		
		self.btn_entrenamiento = wx.Button( self, wx.ID_ANY, u"Entrenamiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btn_entrenamiento, 0, wx.ALL, 5 )
		
		self.btn_menu = wx.Button( self, wx.ID_ANY, u"Menú", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btn_menu, 0, wx.ALL, 5 )
		
		
		fgSizer81.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( fgSizer81, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		#bindeo de eventos con def
		self.tab_busqueda.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Seleccionar)
		self.txtbusquedad.Bind( wx.EVT_TEXT, self.Busqueda )
		self.btnmodificar.Bind( wx.EVT_BUTTON, self.Actualizar )	
		self.btneliminar.Bind( wx.EVT_BUTTON, self.Eliminar )
		self.btn_menu.Bind( wx.EVT_BUTTON, self.Cancelar )
		self.btn_foto.Bind( wx.EVT_BUTTON, self.Foto )
		self.btn_entrenamiento.Bind( wx.EVT_BUTTON, self.Entrenamiento )
		self.Bind( wx.EVT_ACTIVATE, self.actualizarBitmap ) #Verifica si hay imagen temporal de usuario o no
		
		
		self.btnmodificar.Disable()
		self.btneliminar.Disable()
		self.btn_foto.Disable()
		self.btn_entrenamiento.Disable()
		
		self.tab_busqueda.InsertColumn(0, 'Id', width=30)
		self.tab_busqueda.InsertColumn(1, 'Nombre', width=100)
		self.tab_busqueda.InsertColumn(2, 'Apellido', width=100)
		self.tab_busqueda.InsertColumn(3, 'Direccion', width=100)
		self.tab_busqueda.InsertColumn(4, 'Telefono', width=80)
		self.tab_busqueda.InsertColumn(5, 'DUI', width=100)
		self.tab_busqueda.InsertColumn(6, 'NIT', width=170)
		self.tab_busqueda.InsertColumn(7, 'Cargo', width=130)
		# fin de codigo autogenerado por wxFormBuilder
		
		self.padre = parent
		self.padre.m_button1.Disable()
		
		
		#Conexion a la base de datos
		self.db = sqliteclass.Database("db_registro.sqlite") #Instanciar la conexion a la Bd.
		
		
		#establecemos el tamaño maximo de la imagen
		self.PhotoMaxSize = 150
		
		
		#cargamos los datos a la tabla por defecto
		self.cargar()
		
	def __del__( self ):
		self.padre.m_button1.Enable()	
		
		
	#cargamos los datos en la lista
	def cargar(self):
		#evento para cargar datos de la bd a la lista de 2 maneras todos si el ctrl texto esta vacio 
		#o dependiendo de la busqueda con like asi muestra los resultados
		self.tab_busqueda.DeleteAllItems() # quita los renglones de la lista
		cadena_buscar=self.txtbusquedad.GetValue()	
		if cadena_buscar!="":
			self.prod="%"+str(cadena_buscar)+"%"
			sql="SELECT * FROM usuarios WHERE nombre LIKE ?"
			data_param=self.prod
			typesql='SL'
			self.rows=self.db.query(sql,data_param,typesql)
		else:	
			sql="""SELECT * FROM usuarios"""
			data_param=''
			typesql='S'
			self.rows=self.db.query(sql,data_param,typesql)	
		self.row_count = 0
		#al tener el cursor se van insertando las columnas
		for row in self.rows:
			self.tab_busqueda.InsertStringItem(self.row_count, str(row[0]))
			self.tab_busqueda.SetStringItem(self.row_count,1, str(row[1]))
			self.tab_busqueda.SetStringItem(self.row_count,2, str(row[2]))
			self.tab_busqueda.SetStringItem(self.row_count,3, str(row[3]))
			self.tab_busqueda.SetStringItem(self.row_count,4, str(row[8]))
			self.tab_busqueda.SetStringItem(self.row_count,5, str(row[4]))
			self.tab_busqueda.SetStringItem(self.row_count,6, str(row[5]))
			self.tab_busqueda.SetStringItem(self.row_count,7, str(row[6]))
			if self.row_count % 2:
				self.tab_busqueda.SetItemBackgroundColour(self.row_count, "#EBEBEB")
			else:
				self.tab_busqueda.SetItemBackgroundColour(self.row_count, "#C4C4C4")
			self.row_count += 1
			
			
	# evento al modificarse el texto de la caja de busqueda
	def Busqueda( self, event ):
		self.cargar()
		
		
	# evento para el entrenamiento --posterior
	def Entrenamiento(self, event):
		entrenar = entrenamiento.Entrenamiento(self)
		self.id_user = str(self.txtid.GetValue())
		entrenar.Show()
		
		
	# evento para salir del formulario
	def Cancelar( self, event ):
		self.padre.m_button1.Enable()
		self.Close() 
		
		
	# evento al seleccionar un elemento del listado de registros cargados
	def Seleccionar(self, event):
		self.seleccionado = '' 
		self.id_seleccionado = '' 
		
		self.btn_entrenamiento.Enable()
		self.btnmodificar.Enable()
		self.btneliminar.Enable()
		self.btn_foto.Enable()
		self.btn_entrenamiento.Enable()
		
		self.seleccionado = self.tab_busqueda.GetFocusedItem() #traer la posicion del indice
		self.id_seleccionado = self.tab_busqueda.GetItemText(self.seleccionado)#traer el texto del primera columna segun la posicion del indice
		self.buscar_datos(self.id_seleccionado)
		
		
	#continamos con la busqueda y carga de información al seleccionar un elemento de la lista
	def buscar_datos( self, id_seleccionado):
		cadena_buscar = {'id_seleccionado':str(id_seleccionado)}
		if cadena_buscar!="":
			sql="""SELECT * FROM usuarios WHERE usuarios.id_usuario=:id_seleccionado"""	
			data_param=cadena_buscar
			typesql='S'
			self.rows=0
			self.rows=self.db.query(sql,data_param,typesql)
			if self.rows>0:					
				for row in self.rows:					
					if row[7] is None: #row[8] es la posicion del cursor del campo imagen
						self.rutaa='imgs/blank_img.png'
						self.redimensionar(self.rutaa)
						print self.rutaa
						print "Vacio"
					else:			
						
						self.txtid.SetValue(str(row[0])) 	
						self.txtnom.SetValue(str(row[1])) 	
						self.txtape.SetValue(str(row[2])) 	
						self.txtdireccion.SetValue(str(row[3])) 	
						self.txtphone.SetValue(str(row[8])) 	
						self.txtdui.SetValue(str(row[4])) 	
						self.txtnit.SetValue(str(row[5])) 	
						self.txtcargo.SetValue(str(row[6])) 
						self.jpg = str(row[7])
						self.rutaa = "usuarios/"+self.jpg
						print self.rutaa
						self.redimensionar(self.rutaa)
						
	
	#--- REDIMENSIONA LA IMAGEN DE LA RUTA QUE PASEMOS COMO PARAMETRO				
	def redimensionar(self,ruta):
		if os.path.exists(ruta):
			self.ruta=ruta
		else:
			self.ruta="imgs/blank_img.png"
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
		self.imagen.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()	
	
	
	#--- PERMITE ACTUALIZAR LA INFORMACION DE UN USARIO, Y SE DESEA MODIFICAR LA IMAGEN DEL MISMO
	def Actualizar( self, event ):
		id = str(self.txtid.GetValue())
		jpg = "user"+id+".jpg"
		param = {'nombrem':self.txtnom.GetValue(),'apelm':self.txtape.GetValue(),'direcm':self.txtdireccion.GetValue(),'telefm':self.txtphone.GetValue(),'duim':self.txtdui.GetValue(),'nitm':self.txtnit.GetValue(),'cargom':self.txtcargo.GetValue(),'jpg':jpg,'id_seleccionado':self.id_seleccionado}
		sql=""" UPDATE usuarios SET nombre=:nombrem, apellido=:apelm, direccion=:direcm, telefono=:telefm, dui=:duim, nit=:nitm, cargo=:cargom , imagen=:jpg WHERE id_usuario=:id_seleccionado"""				
		typesql='U'
		if self.db.query(sql,param,typesql):
			if os.path.exists("orig_frame.jpg"):
					if self.moverImg(jpg):
						self.limpiar()
						self.cargar()
						self.actualizarBitmap(event)
					else:
						self.dial = wx.MessageDialog(None, 'IMAGEN NO MOVIDA', 'INFO', wx.OK|wx.CENTRE)
						self.dial.ShowModal()
						self.actualizarBitmap(event)
			else:
				self.limpiar()
				self.cargar()
				self.actualizarBitmap(event)
		
		
	# evento que elimina el registro seleccionado
	def Eliminar(self, event):
		id_seleccionado = str(self.txtid.GetValue())
		if id_seleccionado != '':
			caja_dialogo = wx.MessageDialog(None, '¿Realmente desea eliminar este registro?', 'Eliminar', wx.YES_NO | wx.ICON_QUESTION)
			if caja_dialogo.ShowModal() == wx.ID_YES:
				sql="""DELETE  FROM usuarios WHERE id_usuario=:id_seleccionado"""
				data_param={'id_seleccionado':id_seleccionado}
				typesql='D'
				self.rows=self.db.query(sql,data_param,typesql)		
				self.cargar()
				self.limpiar()
				self.actualizarBitmap(event)
			caja_dialogo.Destroy()
			
			
	# funcion que limpia los cuandros de texto asi como reestablece la imagen, para luego cargar nuevamente el listado
	def limpiar(self):
		self.txtid.SetValue("") 	
		self.txtnom.SetValue("") 	
		self.txtape.SetValue("") 	
		self.txtdireccion.SetValue("") 	
		self.txtphone.SetValue("") 	
		self.txtdui.SetValue("") 	
		self.txtnit.SetValue("") 	
		self.txtcargo.SetValue("")		
		self.ruta='imgs/blank_img.png'
		self.btn_entrenamiento.Disable()
		
	
	
	# evento para tomar una foto del nuevo usuario creando objeto del archivo fotografia.py
	def Foto(self,event):
		foto = fotografia.Fotografia(self)
		foto.Show()
	
	
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
		self.imagen.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
		
		
	#--- FUNCION QUE NOS PERMITE MOVER UNA IMAGEN, 
	#    EN ESTE CASO LA TEMPORAL EN CASO QUE EXISTA---
	def moverImg(self,img):
		self.user_png = img
		if os.path.exists("orig_frame.jpg"):
			os.rename("orig_frame.jpg", self.user_png)
			if os.path.exists("usuarios/"+self.user_png):
				os.remove("usuarios/"+self.user_png)
				shutil.move(self.user_png ,"usuarios")
				return True
			else:
				shutil.move(self.user_png ,"usuarios")
				return True
		else:
			print "No existe foto de usuario para guardar"
