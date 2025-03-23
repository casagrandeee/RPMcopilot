import tkinter as tk
from tkinter import ttk, messagebox
from core.suggestions_engine import SuggestionEngine

from src.autocad_handler import AutoCADHandler


class CopilotUI:
    def __init__(self, root):
        self.root = root
        self.root.title('RPMcopilot')
        self.root.geometry('600x400')

        self.acad_handler = AutoCADHandler()
        self.suggestion_engine = SuggestionEngine()

        self.tabs = ttk.Notebook(self.root)
        self.tab_monitor = ttk.Frame(self.tabs)
        self.tab_chat = ttk.Frame(self.tabs)
        self.tab_config = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_monitor, text="Monitor")
        self.tabs.add(self.tab_chat, text="Chat")
        self.tabs.add(self.tab_config, text="Configurações")
        self.tabs.pack(expand=1, fill="both")

        self.create_monitor_tab()
        self.create_chat_tab()
        self.create_config_tab()

    def create_monitor_tab(self):
        self.log_box = tk.Text(self.tab_monitor, height=15, width=70)
        self.log_box.pack(pady=10)

        self.btn_start = ttk.Button(self.tab_monitor, text="Iniciar Monitoramento", command=self.start_monitor)
        self.btn_start.pack(pady=5)

    def create_chat_tab(self):
        self.chat_log = tk.Text(self.tab_chat, height=15, width=70)
        self.chat_log.pack(pady=10)

        self.chat_entry = tk.Entry(self.tab_chat, width=50)
        self.chat_entry.pack(side=tk.LEFT, padx=5)

        self.btn_send = ttk.Button(self.tab_chat, text="Enviar", command=self.send_chat_message)
        self.btn_send.pack(side=tk.RIGHT, padx=5)

    def create_config_tab(self):
        self.label_config = tk.Label(self.tab_config, text="Configurações")
        self.label_config.pack(pady=10)

    def log(self, message):
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, message + '\n')
        self.log_box.see(tk.END)
        self.log_box.config(state=tk.DISABLED)

    def start_monitor(self):
        self.log('Monitoramento iniciado')

        try:
            self.acad_handler.listar_objetos()
            self.log(f"Conectado ao AutoCAD - Arquivo: {self.acad_handler.acad.doc.Name}")

            self.log("Informações do projeto:")
            self.acad_handler.capturar_informacoes_do_projeto()

            objetos = list(self.acad_handler.acad.iter_objects())
            sugestoes = self.suggestion_engine.gerar_sugestoes_basicas(objetos)

            if sugestoes:
                self.log("💡 Sugestões do Copilot:")
                for sugestao in sugestoes:
                    self.log(f"-{sugestao}")
            else:
                self.log("🤖 Copilot não encontrou sugestões no momento")

        except Exception as e:
            self.log(f"Erro: {str(e)}")
            messagebox.showerror("Erro", f"Não foi possível conectar ao AutoCAD.\n\n{e}")

    def send_chat_message(self):
        message = self.chat_entry.get()
        if message.strip():
            self.chat_log.insert(tk.END, f"Você: {message}\n")
            self.chat_entry.delete(0, tk.END)
            self.chat_log.insert(tk.END, "Copilot: Ainda estou aprendendo a conversar\n")
            self.chat_log.see(tk.END)
            self.chat_log.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    app = CopilotUI(root)
    root.mainloop()