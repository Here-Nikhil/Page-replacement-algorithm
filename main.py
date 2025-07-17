import sys
from PyQt5.QtWidgets import QApplication
from gui import PageReplacementSimulator

def main():
    """Entry point for the Page Replacement Simulator application."""
    app = QApplication(sys.argv)
    window = PageReplacementSimulator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()