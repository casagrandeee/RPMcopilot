class SuggestionEngine:
    def __init__(self):
        self.sugestoes = []

    def gerar_sugestoes_basicas(self, objetos):

        self.sugestoes.clear()

        tipos = {}
        for obj in objetos:
            nome = obj.ObjectName
            tipos[nome] = tipos.get(nome, 0) + 1

        for tipo, quantidade in tipos.items():
            if quantidade >= 3:
                self.sugestoes.append(
                    f"🔹 Você usuou muitos objetos do tipo {tipo}. Deseja criar um atalho?"
                )
            elif quantidade == 1:
                self.sugestoes.append(
                    f"🔹 Objeto '{tipo}' aparece isoladamente. Deseja padronizar?"
                )

        return self.sugestoes