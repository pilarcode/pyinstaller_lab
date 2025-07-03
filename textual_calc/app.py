
from textual.app import App
from textual.widgets import Header, Footer, Button, Static

class TestApp(App):
    TITLE = "Textual Test App"
    
    def on_load(self):
        self.log("On the on_load method!")

    def compose(self):
        self.log("On the compose method!")
        yield Header()
        yield Button("Click Me!", id="btn")
        yield Static("This is a test Textual app")
        yield Footer()
    
    def on_button_pressed(self, event):
        self.log("On the on_button_pressed method!")
        self.query_one(Static).update("Button was clicked!")

def main():
    """Run the Textual app."""
    app = TestApp()
    app.run()
if __name__ == "__main__":
    main()
