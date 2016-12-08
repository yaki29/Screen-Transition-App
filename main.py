from kivy.uix.button import Button 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.app import App
Builder.load_string(
'''
<PageLayout>:
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
	
	ScrollView:
    	Label:
	        text: 'my name is Yash '*100
	        font_size: 50
	        text_size: self.width, None
	        size_hint_y: None
	        height: self.texture_size[1]
	        # background_color: 255, 0, 0, 1
	        AnchorLayout:
	        	size: self.parent.size
	        	pos: self.parent.pos
	        	anchor_x: 'right'
	        	anchor_y: 'top'
	        	Button:
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

class ScreenApp(App):
	def build(self):
		return	PageLayout()
ScreenApp().run()