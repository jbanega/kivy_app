from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (320, 460)

# Designated .kv file
Builder.load_file("calculator.kv")


class MyLayout(Widget):
    def clear(self):
        # Clear input box
        self.ids.calc_input.text = "0"
    
    # Create a button number pressing function
    def button_press(self, button):
        # Create a variable that contains was in the text box already
        prior = self.ids.calc_input.text

        # Test for error first
        if "Error" in prior:
            self.ids.calc_input.text = ""

        # Determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text += f"{button}"
    
    # Create math function
    def math_sign(self, sign):
        # Adding a plus sign to the text box
        self.ids.calc_input.text += f"{sign}"

    # Create a decimal fucntion
    def dot(self):
        # Create a variable that contains was in the text box already
        prior = self.ids.calc_input.text
        # Split out text box
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            self.ids.calc_input.text += f"."
        elif "." in prior:
            pass
        else:
            # Adding a decimal to the end of text box
            self.ids.calc_input.text += f"."

    # Create a function to remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove last item in the text box
        prior = prior[:-1]
        # Output back to the text box
        self.ids.calc_input.text = prior
        # Display zero when there is nothing to remove
        if self.ids.calc_input.text == "":
            self.ids.calc_input.text = "0"

    # Create function to make text box positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Search if there is negative sign in the text box
        if "-" not in prior:
            prior = f"-{prior}"
        else:
            prior = f"{prior.replace('-', '')}"
        # Output back to the text box
        self.ids.calc_input.text = prior

    # Create function to display result
    def equal(self):
        # Create a variable that contains was in the text box already
        prior = self.ids.calc_input.text

        # Error handling
        try:
            # Evaluate the math from the text box
            result = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(result)
        except:
            self.ids.calc_input.text = str("Error")


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()