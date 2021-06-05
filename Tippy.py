import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider



class MyGrid(Widget):

    def slide(self, *args):
        dollar_amount = self.ids.bill_slide.value
        tip_percentage = self.ids.tip_slide.value
        final_bill = .01*(tip_percentage) * dollar_amount + dollar_amount

        if dollar_amount == 0 and tip_percentage > 0:
            self.ids.final_bill.text = "Please specify a bill amount"
        elif tip_percentage == 0 and dollar_amount > 0:
            self.ids.tip_label.text = ""
            self.ids.final_bill.text = "Please specify a tip percentage"
        elif tip_percentage == 0 and dollar_amount == 0:
            self.ids.bill_label.text = ""
            self.ids.final_bill.text = """Please specify a bill amount and a tip percentage"""
        else:
            self.ids.final_bill.text = "Your Final Bill is $" + str(round(final_bill,2))
        

class Tippy(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Tippy().run()
