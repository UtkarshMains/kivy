from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'resizable', True)
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

# Declare both screens

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.button = Button(
                     color =(1, 0, .65, 1),
                     size_hint = (.2, .2),
                     pos_hint = {"x":0.4, "y":0.7}
                   )
        self.img = Image(source='teacher.jpeg',pos_hint = {"x":0.4, "y":0.7},size_hint_x = 0.2,size_hint_y=0.2,allow_stretch = True,keep_ratio = False)

        self.button.bind(on_press=self.change_screen)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.img)
        self.button2 = Button(
            color=(1, 0, .65, 1),
            size_hint=(.2, .2),
            pos_hint={"x": 0.4, "y": 0.35}
        )
        self.img2 = Image(source='student.png', pos_hint={"x": 0.4, "y": 0.35}, size_hint_x=0.2, size_hint_y=0.2,
                         allow_stretch=True, keep_ratio=False)

        self.button2.bind(on_press=self.change_screen2)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.img2)

    def change_screen(self, event):
        self.manager.transition.direction = 'down'
        self.manager.transition.duration = 0.5
        self.manager.current = 'settings'
    def change_screen2(self, event):
        self.manager.transition.direction = 'up'
        self.manager.transition.duration = 0.5
        self.manager.current = 'Sreg'

class StudentRegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.l2 = Label(text='[b]Student Registration[/b]',font_size = '20sp', markup = True,pos_hint={"x": 0.01, "y": 0.4},color=('#FFFFFF'))
        self.layout.add_widget(self.l2)
        self.user=Label(text="Username",font_size='20sp',markup=True,pos_hint={"x": -0.34, "y": 0.3},color=('#FFFFFF'))
        self.userip=TextInput(font_size=20,
                  size_hint_y=0.08,size_hint_x=0.5,
                  height=50,pos_hint={"x": 0.1, "y": 0.7})
        self.layout.add_widget(self.user)
        self.layout.add_widget(self.userip)
        self.password = Label(text="Password", font_size='20sp', markup=True, pos_hint={"x": -0.34, "y": 0.1},
                          color=('#FFFFFF'))
        self.passwordip = TextInput(font_size=20,
                                size_hint_y=0.08, size_hint_x=0.5,
                                height=50, pos_hint={"x": 0.1, "y": 0.5})
        self.layout.add_widget(self.password)
        self.layout.add_widget(self.passwordip)
        self.submit=Button(text="Submit",border = (30, 30, 30, 30),size_hint = (.3, .3),pos_hint = {"x":0.35, "y":0.3})
        self.layout.add_widget(self.submit)
        self.pas=self.passwordip.text
        print(self.pas)


# Create the screen manager

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(StudentRegisterScreen(name='Sreg'))



class TestApp(App):

    def build(self):
        Window.clearcolor = ('#09BBF2')
        return sm


if __name__ == '__main__':
    TestApp().run()