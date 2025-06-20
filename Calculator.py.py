from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button  # FIXED: Button must be imported


class MainApp(App):
    def build(self):
        self.icon = "Calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")

        # FIXED: corrected 'black' and removed 'foreground_color' (use 'foreground' instead)
        self.solution = TextInput(
            background_color="black", foreground_color=(1, 1, 1, 1),  # RGBA for white
            multiline=False, halign="right", font_size=55, readonly=True
        )

        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:  # FIXED: changed from 'lable' to 'label'
                button = Button(
                    text=label, font_size=30, background_color=(0.5, 0.5, 0.5, 1),  # Gray RGBA
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30, background_color=(0.5, 0.5, 0.5, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"


if __name__ == "__main__":
    app = MainApp()
    app.run()
