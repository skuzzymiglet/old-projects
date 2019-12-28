from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    pass
    def build(self):
        return Label(text="hello", font_size=100, color=(0.456, 0.9, 0, 1))

if __name__ == "__main__":
    MyApp().run()
