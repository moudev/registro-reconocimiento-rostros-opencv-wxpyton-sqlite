# -*- coding: utf-8 -*- 


import wx
import wx.xrc
import subprocess
import sqliteclass #clase de conexion
import menu
import time
###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):
	
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
		
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( int(self.width),int(self.height) ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, 73, 90, 90, False, "Droid Sans Mono" ) )
		
		fgSizer7 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer4.AddSpacer(( 0, (int(self.height)*0.20)), 1, wx.EXPAND, 5 )
		
		
		fgSizer7.Add( fgSizer4, 1, wx.EXPAND, 5 )
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer8.AddSpacer( ( int(self.width)*0.48, int(self.height)*0.10), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 20, 72, 90, 90, False, "Liberation Serif" ) )
		
		fgSizer8.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer7.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		fgSizer10 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer10.AddSpacer( ( 0, int(self.height)*0.10), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 11, 72, 90, 90, False, "Liberation Serif" ) )
		
		
		fgSizer10.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.txtnom= wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtnom.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer10.Add( self.txtnom, 0, wx.ALL, 5 )
		
		
		fgSizer10.AddSpacer( (int(self.width)*0.42,  int(self.height)*0.10), 1, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 11, 72, 90, 90, False, "Liberation Serif" ) )
		
		fgSizer10.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txtpass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_PASSWORD )
		self.txtpass.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer10.Add( self.txtpass, 0, wx.ALL, 5 )
		
		
		fgSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer10.AddSpacer( ( 0,0), 1, wx.EXPAND, 5 )
		self.lblerror = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblerror.Wrap( -1 )
		self.lblerror.SetFont( wx.Font( 13, 72, 93, 90, False, "Serif" ) )
		self.lblerror.SetForegroundColour( wx.Colour( 242, 21, 35 ) )
		
		fgSizer10.Add( self.lblerror, 0, wx.ALL, 5 )
		
		
		fgSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		fgSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Ingresar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 11, 72, 90, 90, False, "Liberation Serif" ) )
		fgSizer10.Add( self.m_button1, 0, wx.ALL, 5 )
		
		fgSizer7.Add( fgSizer10, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer7 )
		self.Layout()
		self.frm_menu = ""
		self.Centre( wx.BOTH )
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.ingresar )
		# fin de codigo autogenerado por wxFormBuilder
		
		#conectamos a la base de datos
		self.db = sqliteclass.Database("db_registro.sqlite")
		
	def __del__( self ):
		pass
		
	# evento para validar la cuenta del usuario que inicia sesion
	def ingresar(self, event):
		sql="""SELECT contrasenia FROM login WHERE login.usuario=:nombre"""
		data_param={'nombre':self.txtnom.GetValue()}
		typesql='S'
		#db=self.db
		rows=self.db.query(sql,data_param,typesql)
		if len(str(rows))>2:
			for row in rows:
				if str(row[0]) == self.txtpass.GetValue():
					
					self.frm_menu = menu.Menu(self)
					self.frm_menu.Show(True)			
				else:
					self.lblerror.SetLabel("Contraseña incorrecta")
		else:
			self.lblerror.SetLabel("El usuario no existe")		
			
	
		
class my_app(wx.App):
	def OnInit(self):
		formulario=Login(None)
		formulario.Show()
		return 1
myaap = my_app(0)
myaap.MainLoop()
