import os
import time
from pyautocad import Autocad

class AutoCADHandler:
    def __init__(self):
        self.acad = Autocad(create_if_not_exists=False)

        try:
            _ = list(self.acad.iter_objects(limit=1))
            print(f"✅ Conectado ao AutoCAD - Arquivo: {self.acad.doc.Name}")
        except Exception as e:
            raise RuntimeError("❌ Erro ao conectar com o AutoCAD. Verifique se ele está aberto.") from e

    def listar_objetos(self):
        print("📄 Listando objetos no desenho...")
        for obj in self.acad.iter_objects():
            print(f"🔹 Objeto encontrado: {obj.ObjectName}")

    def desenhar_linha(self, x1, y1, x2, y2):
        p1 = self.acad.Point(x1, y1)
        p2 = self.acad.Point(x2, y2)
        line = self.acad.model.AddLine(p1, p2)
        print(f"📏 Linha desenhada de {p1} para {p2}")

    def capturar_informacoes_do_projeto(self):
        print(f"📂 Nome do arquivo: {self.acad.doc.Name}")

        num_objetos = sum(1 for _ in self.acad.iter_objects())
        print(f"📊 Número total de objetos: {num_objetos}")

        print("🔍 Primeiros objetos do projeto:")
        for i, obj in enumerate(self.acad.iter_objects()):
            print(f"  {i+1}: {obj.ObjectName}")
            if i >= 4:
                break