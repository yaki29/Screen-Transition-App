from kivy.uix.button import Button 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView 
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.animation import Animation
from kivy.animation import AnimationTransition
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
Builder.load_string(
'''
<TransitionWidget>:

    Button:
        text: 'StartPage'
        background_color: 1, 1, 1, 0
        AnchorLayout:
        	size: self.parent.size
        	pos: self.parent.pos
        	anchor_x: 'right'
        	anchor_y: 'top'
        	Button:
        		size_hint: None, None
        		text: "next"
        		height: '60dp'
        		width: '60dp'
        		on_press: root.manager.current = 'second'
        		background_color: 0, 0.99, 0.59, 1
<SecondPage>:	
	BoxLayout:
		id: second_layout
		orientation: 'vertical'
		# Button:
		# 	text: 'anime'
		# 	on_press: root.anime()
		# 	size_hint: None, None
		# 	height: '50dp'
		# 	width: '50dp'
		# 	background_color: 0, 0.99, 0 ,1
		Label:
			id: head
			text: 'This is to animate'
			font_size: 40
			size_hint_y: None
			height: '20dp'
			# pos_hint_x: None
			# pos_hint_y: None
			markup: True
			halign: 'left'
			valign: 'top'

		ScrollView:
			bar_color: 1, 0 , 0, 1
			bar_width: 4
			scroll_y: 1
			on_scroll_start: root.decide(self.scroll_y)
			# on_scroll_start: root.animeup()
			Label:
		        text: 'my name is Yash '*100
		        font_size: 50
		        text_size: self.width, None
		        size_hint_y: None
		        height: self.texture_size[1]
		        
		        
		        # background_color: 1, 0, 0, 1
		        AnchorLayout:
		        	size: self.parent.size
		        	pos: self.parent.pos
		        	anchor_x: 'right'
		        	anchor_y: 'top'
		        	Button:
		        		id: cross
		        		text: "back"
		        		size_hint: None, None
		        		height: '60dp'
		        		width: '60dp'
		        		on_press: root.manager.current = 'start'
		        		on_press: root.change_base()
		        		background_color: 0, 0.99, 0.59, 1

''')

class TransitionWidget(Screen):
	pass

class SecondPage(Screen):
	def decide(self,sy):
		global previous
		if sy > previous:
			self.animeup()
		else :
			self.animedown()
		global previous
		previous = sy 
	def animedown(self): 
		# if flag == 0:
		lab = self.ids['head']
		ani = Animation(pos=(-self.width*0.05,self.height*0.93), size=(70, 70), t = 'out_bounce',duration=0.5) + Animation(pos=(-self.width*0.30,self.height*0.905), t = 'linear',duration=1)
		ani.start(lab)
			# global flag
			# flag += 1
	def animeup(self): 
		# if flag == 0:
		lab = self.ids['head']
		ani = Animation(pos=(-self.width*0.30,self.height*0.905), size=(70,70),duration=0.5) + Animation(pos=(-self.width*0.05,self.height*0.93), t = 'linear',duration=1)
		ani.start(lab)
			# global flag
			# flag += 1
	def change_base(self):
		global flag
		flag = 0
sm = ScreenManager(transition=SlideTransition(direction='up'))
sm.add_widget(TransitionWidget(name='start'))
sm.add_widget(SecondPage(name='second'))
global flag 
flag = 0
global previous 
previous = -1

class ScreenApp(App):
	
	def build(self):
		return	sm
ScreenApp().run()