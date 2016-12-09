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
Builder.load_string(
'''
<TransitionWidget>:
	border: '25dp'
	page: 1
    Button:
        
        background_color: 1, 1, 1, 0
        AnchorLayout:
        	size: self.parent.size
        	pos: self.parent.pos
        	anchor_x: 'right'
        	anchor_y: 'top'
        	Button:
        		size_hint: None, None
        		height: '60dp'
        		width: '60dp'
        		on_press: root.page = 1
        		background_color: 0, 255, 0, 1
        		BoxLayout:
        			size: self.parent.size
        			pos: self.parent.pos
		        	Image: 
		        		source: 'next.png'
		        		pos: self.pos
		        		size: self.size
	BoxLayout:
		id: second_layout
		orientation: 'vertical'
		Button:
			text: 'anime'
			on_press: root.anime()
			size_hint: None, None
			height: '50dp'
			width: '50dp'
		Label:
			id: head
			text: 'This is to animate'
			font_size: 40
			size_hint_y: None
			height: '60dp'
			# pos_hint_x: None
			# pos_hint_y: None
			markup: True
			halign: 'left'
			valign: 'top'

		ScrollView:
			bar_color: 1, 0 , 0, 1
			bar_width: 4
			Label:
		        text: 'my name is Yash '*100
		        font_size: 50
		        text_size: self.width, None
		        size_hint_y: None
		        height: self.texture_size[1]
		        # on_scroll_start: root.anime()
		        # background_color: 255, 0, 0, 1
		        AnchorLayout:
		        	size: self.parent.size
		        	pos: self.parent.pos
		        	anchor_x: 'right'
		        	anchor_y: 'top'
		        	Button:
		        		id: cross
		        		size_hint: None, None
		        		height: '60dp'
		        		width: '60dp'
		        		on_press: root.page = 0
		        		background_color: 0, 255, 0, 1
		        		BoxLayout:
		        			size: self.parent.size
		        			pos: self.parent.pos
				        	Image: 
				        		source: 'cross.png'
				        		pos: self.pos
				        		size: self.size


''')

class TransitionWidget(PageLayout):
	def anime(self):
		lab = self.ids['head']
		ani = Animation(pos=(500,800), size=(10, 10), t = 'linear',duration=0.5)
		ani.start(lab)
class ScreenApp(App):

	def build(self):
		return	TransitionWidget()
ScreenApp().run()