"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Connor White
Started 11/11/2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934
__author__ = 'Connor White'


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = int(value) * CONVERSION_FACTOR if value.isdigit() else 0.0
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """ handle increment, output result to input widget"""
        input_number = self.root.ids.input_number.text
        self.root.ids.input_number.text = str(int(input_number) + increment if input_number.isdigit() else increment)


ConvertMilesKmApp().run()
