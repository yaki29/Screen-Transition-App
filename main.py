from kivy.uix.button import Button 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView 
from kivy.lang import Builder
from kivy.app import App
Builder.load_string(
'''
<TransitionWidget>:
	border: '25dp'
	page: 1
    Button:
        
        background_color: 255, 0, 0, 1
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
		orientation: 'vertical'
		Label:
			id: 'head'
			text: 'This is to animate'
			font_size: 20
			size_hint_y: None
			height: '60dp'

		ScrollView:
			Label:
		        text: 'my name is Yash '*100
		        font_size: 50
		        text_size: self.width, None
		        size_hint_y: None
		        height: self.texture_size[1]
		        #on_scroll_start: cross.background_color = (1,0,0,00.5)
		        # background_color: 255, 0, 0, 1
		        AnchorLayout:
		        	size: self.parent.size
		        	pos: self.parent.pos
		        	anchor_x: 'right'
		        	anchor_y: 'top'
		        	Button:
		        		id: 'cross'
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
	pass
class ScreenApp(App):

	def build(self):
		return	TransitionWidget()
ScreenApp().run()