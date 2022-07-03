# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
#from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class IndexPage(BoxLayout):
    def __init__(self,**kwargs):
        super(IndexPage, self).__init__(**kwargs)
        #self.join = Button(text = " Hello World!")
        #self.add_widget(self.join)

class TestApp(App):
    def build(self):
        return IndexPage()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TestApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
