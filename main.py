from kivy.uix.button import Button 
from kivy.uix.pagelayout import PageLayout 
from kivy.lang import Builder
from kivy.app import App
Builder.load_string(
'''
<PageLayout>:
    Button:
        text: 'page1'
        background_color: 255, 0, 0, 0.2
    Button:
        text: 'page2'
        background_color: 255, 0, 0, 0.4
    Button:
        text: 'page3'
        background_color: 255, 0, 0, 0.6

''')

class ScreenApp(App):
	def build(self):
		return	PageLayout()
ScreenApp().run()