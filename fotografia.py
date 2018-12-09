
# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import os,shutil
import cv, cv2
import subprocess
import time

class Fotografia ( wx.Frame ):
	
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
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Toma de Fotografía", pos = wx.DefaultPosition, size = wx.Size( int(self.width),int(self.height)), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 3, 0, 0 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
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
		
		self.bitmap_foto = wx.StaticBitmap( self, wx.ID_ANY, self.bmp, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.bitmap_foto, 0, wx.ALL, 5 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )
		
		
		gSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_foto = wx.Button( self, wx.ID_ANY, u"Fotografía", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.btn_foto, 0, wx.ALL, 5 )
		
		
		gSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_cancelar, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		
		
		#timer
		fps = 7
		self.timer = wx.Timer(self) #Timer
		self.timer.Start(1000./fps)
		
		# Connect Events
		self.btn_foto.Bind( wx.EVT_BUTTON, self.foto )
		self.Bind(wx.EVT_TIMER, self.NextFrame,self.timer)
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	
	
	#--- FUNCION ENCARGADA DE ACTUALIZAR EL BITMAP, VA JUNTO CON TIMER---#
	#Esta funcion se ejecuta cada cierto tiempo con el evento EVT_TIMER de wxpython
	#Para cambiar la velocidad con que se actualizar el bitmap en donde se mostrará la imagen
	#solo hay que modificar el valor de fps, que esta  un poco mas arriba
	def NextFrame(self, event):
		ret, self.imagen_guardar = self.capture.read()
		if ret:
			self.frame = cv2.cvtColor(self.imagen_guardar, cv2.COLOR_BGR2RGB)
			self.bmp.CopyFromBuffer(self.frame)			
			self.Refresh()
	
	
	#--- FUNCION ENCARGADA DE GUARDAR UNA IMAGEN TEMPORAL---#
	#Hace que la camara deje de tomar captura y luego guarda una imagen temporal
	#con el frame justo al presionar el boton de tomar fotografia
	def foto( self, event ):
		self.timer.Stop()
		try:
			cv2.imwrite('orig_frame.jpg', self.imagen_guardar)
			self.Close() 
		except AttributeError:
			traceback.print_exc()
			
			
	def cancelar(self,event):
		self.Close()
	
