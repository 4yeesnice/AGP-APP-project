from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from create_pdf import create_pdf
from kivymd.app import MDApp
import datetime

from kivymd.theming import ThemeManager

class MainWindow(Screen):
    pass


class PDFWindow(Screen):

    volume = 0
    pressure = 0
    temperature = 0
    z_factor = 0
    flow = 0

    def create(self):
        object_name = str(self.ids.object.text)
        time = str(self.ids.time.text)
        name1 = str(self.ids.name1.text)
        name2 = str(self.ids.name2.text)
        name3 = str(self.ids.name3.text)


        if time is "":
            now = datetime.datetime.now()
            time = f'{now.hour}:{now.minute}'

        create_pdf(object_name, time, PDFWindow.volume, PDFWindow.pressure, PDFWindow.temperature,
                   PDFWindow.z_factor, PDFWindow.flow, name1, name2, name3)


class FirstWindow(Screen):

    def __init__(self, **kwargs):
        super(FirstWindow, self).__init__(**kwargs)

    def calculate(self):
        try:
            volume = float(self.ids.volume.text)
            pressure = float(self.ids.pressure.text)
            temperature = float(self.ids.temperature.text)
            z_factor = float(self.ids.z_factor.text)

            q = (283.8 * (pressure * volume) / (temperature * z_factor)) + 3 * volume
            index = str(q).find(".")

            self.ids.flow.text = str(q)[0:index+3]


        except:

            self.ids.flow.text = "введите числа"


    def next_pdf(self):
        volume = self.ids.volume.text
        pressure = self.ids.pressure.text
        temperature = self.ids.temperature.text
        z_factor = self.ids.z_factor.text
        flow = self.ids.flow.text


        PDFWindow.volume = volume
        PDFWindow.pressure = pressure
        PDFWindow.temperature = temperature
        PDFWindow.z_factor = z_factor
        PDFWindow.flow = flow






class SecondWindow(Screen):

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

    def calculate(self):
        try:
            volume = float(self.ids.volume.text)
            pressure = float(self.ids.pressure.text)
            temperature = float(self.ids.temperature.text)
            z_factor = float(self.ids.z_factor.text)

            q = 283.8*(volume/temperature)*((pressure/z_factor) - 1)
            index = str(q).find(".")

            self.ids.flow.text = str(q)[0:index + 3]


        except:

            self.ids.flow.text = "введите числа"


    def next_pdf(self):
        volume = self.ids.volume.text
        pressure = self.ids.pressure.text
        temperature = self.ids.temperature.text
        z_factor = self.ids.z_factor.text
        flow = self.ids.flow.text

        PDFWindow.volume = volume
        PDFWindow.pressure = pressure
        PDFWindow.temperature = temperature
        PDFWindow.z_factor = z_factor
        PDFWindow.flow = flow





class WindowManager(ScreenManager):
    pass





class MyApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        kv = Builder.load_file('my.kv')

        return kv



if __name__ == "__main__":
    MyApp().run()
