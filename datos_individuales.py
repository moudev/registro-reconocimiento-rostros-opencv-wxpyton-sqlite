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
class Datos ( wx.Frame ):
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
		
		self.db = sqliteclass.Database("db_registro.sqlite")
		
		
		
		#===================================================
		# Añadiendo imagen a Bitmap
		#===================================================
		
		self.ruta="imgs/blank_img.png"
		if os.path.exists(self.ruta):
			
			self.ruta=self.ruta
		else:
			self.ruta="imgs/blank_img.png"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.ancho = 400
		self.alto = 200
		
		#===================================================
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Datos individuales", pos = wx.DefaultPosition, size = wx.Size( int(self.width),int(self.height)), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 0, int(self.height)*0.30), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 200, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 200, 0), 1, wx.EXPAND, 5 )
		
	
		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )
		fgSizer2.Add( self.m_staticText122, 0, wx.ALL, 5 )
		
		self.txt_idd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY)
		
		fgSizer2.Add( self.txt_idd, 0, wx.ALL, 5 )
	
	
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txt_nombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY)
		
		fgSizer2.Add( self.txt_nombre, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.25  , 0), 1, wx.EXPAND, 5 )
		
		self.user = wx.StaticText( self, wx.ID_ANY, u"Apellido:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user.Wrap( -1 )
		fgSizer2.Add( self.user, 0, wx.ALL, 5 )
		
		self.txt_apellido = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer2.Add( self.txt_apellido, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( int(self.width)*0.25  , 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txt_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY)
		fgSizer2.Add( self.txt_dir, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Telefono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txt_tel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY)
		fgSizer2.Add( self.txt_tel, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"DUI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_dui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY)
		fgSizer2.Add( self.txt_dui, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"NIT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		self.txt_nit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer2.Add( self.txt_nit, 0, wx.ALL, 5 )
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Cargo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txt_cargo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
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
		fgSizer3.AddSpacer( (0, int(self.height)*0.09), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
		fgSizer3.AddSpacer( ( 0,0) ,1, wx.EXPAND, 5 )
				
		fgSizer4 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
	
		fgSizer4.AddSpacer( ( int(self.width)*0.05,0) ,1, wx.EXPAND, 5 )
		fgSizer4.AddSpacer( ( int(self.width)*0.05,0) ,1, wx.EXPAND, 5 )
		fgSizer4.AddSpacer( ( int(self.width)*0.05,0) ,1, wx.EXPAND, 5 )
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_cancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		#connect events
	
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.Cancelar )
	
		#====================================
		#TRAER DATOS
		#====================================
		self.padre = parent
		self.datos(self.padre.id_user)
		
		#====================================
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		# fin de codigo autogenerado por wxFormBuilder
		
		
		
		# agregada la conexion a la base de datos
		
		
	def __del__( self ):
		#self.padre.m_button2.Enable()
		pass
	# evento para cerrar el formulario
	def Cancelar( self, event ):
		self.Close()
		
	def datos(self,id_user):
		
		sql="select * from usuarios where id_usuario='"+str(id_user)+"'"
		typesql='S'
		data_param = ""
		rows=self.db.query(sql,data_param,typesql)
		if len(rows) >=1:
			for row in rows:
				self.txt_idd.SetValue(str(row[0])) 	
				self.txt_nombre.SetValue(str(row[1])) 	
				self.txt_apellido.SetValue(str(row[2])) 	
				self.txt_dir.SetValue(str(row[3])) 	
				self.txt_tel.SetValue(str(row[8])) 	
				self.txt_dui.SetValue(str(row[5])) 	
				self.txt_nit.SetValue(str(row[4])) 	
				self.txt_cargo.SetValue(str(row[6])) 
				self.jpg = str(row[7])
				self.ruta = "usuarios/"+self.jpg
				if os.path.exists(self.ruta):		
					self.ruta=self.ruta
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
	
