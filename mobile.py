from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.app import App
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
        		background_color: 0, 0.99, 0 ,1
    		
<SecondPage>:	
	BoxLayout:
		id: second_layout
		orientation: 'vertical'
		Button:
			text: 'Back'
			on_press: root.manager.current = 'start'
			size_hint: None, None
			height: '50dp'
			width: '50dp'
			background_color: 0, 0.99, 0 ,1
		BoxLayout:
			size_hint_y: None
			Label:
				id: head
				text: 'This is to animate'
				font_size: 40
				pos_hint_x: None
				pos_hint_y: None
				pos: (-90, 558)
				width: self.texture_size[0]
				height: self.texture_size[1]
				size_hint_y: None
				halign: 'left'
				valign: 'top'
        		
        

		ScrollView:
			id: scroller
			bar_color: 1, 0 , 0, 1
			bar_width: 4
			scroll_y: 1
			on_scroll_start: root.animeup(self.scroll_y)
			Label:
		        text: 'my name is Yash '*100
		        font_size: 50
		        text_size: self.width, None
		        size_hint_y: None
		        height: self.texture_size[1]
		        
		        

''')

class TransitionWidget(Screen):
	pass

class SecondPage(Screen):
	def animeup(self,sy): 
		scr = self.ids['scroller']
		lab = self.ids['head']
		# lab.font_size = 50  - scr.scroll_y*10
		lab.pos[1] =  lab.parent.parent.height*0.85 + scr.scroll_y * 48
		lab.pos[0] =  - lab.parent.parent.width*0.30 + scr.scroll_y * 150
		
		print lab.pos[1], lab.pos[0]
		print scr.scroll_y

sm = ScreenManager(transition=SlideTransition(direction='up'))
sm.add_widget(TransitionWidget(name='start'))
sm.add_widget(SecondPage(name='second'))


class ScreenApp(App):
	def build(self):
		return	sm
ScreenApp().run()