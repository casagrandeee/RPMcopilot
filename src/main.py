import sys
import tkinter as tk
from ui import CopilotUI

def main():
    root = tk.Tk()
    app = CopilotUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()