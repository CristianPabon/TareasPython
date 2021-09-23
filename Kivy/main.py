from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

class txtapp(App):
  def build(self):
    bl = BoxLayout()
    def tex(instance,value):
      print('Se ha oprimido')
    lb = Label(text = 'Esta es la etiqueta', font_size = 50)
    sl = Slider(orientation='horizontal',min=-5, max=5, value=0,value_track=True,value_track_color=(1,0,0,1))
    bt = Button(text='Este es Botón')
    bt.bind(state=tex)
    bl.add_widget(sl)
    bl.add_widget(bt)
    bl.add_widget(lb)

    return bl


if __name__ == "__main__":
  txtapp().run()