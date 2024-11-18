class Noh:
    def __init__(self, identificador, custo_de_tempo, lista_de_recursos):
        self.identificador = identificador
        self.custo_de_tempo = custo_de_tempo
        self.lista_de_recursos = lista_de_recursos
        self.predecessores = []
        self.sucessores = []

    def add_sucessor(self, suc):
        self.sucessores.append(suc)
        suc.add_predecessor(self)

    def add_predecessor(self, pred):
        self.predecessores.append(pred)

    def get_id(self):
        return self.identificador

    def get_custo_de_tempo(self):
        return self.custo_de_tempo

    def get_lista_de_recursos(self):
        return self.lista_de_recursos

    def get_sucessores(self):
        return self.sucessores

    def get_predecessores(self):
        return self.predecessores
    
    def __repr__(self):
        # lista_s = []
        # lista_pre = []
        # for item in self.sucessores:
        #     lista_s.append(item.identificador)
        # for item in self.predecessores:
        #     lista_pre.append(item.identificador)
        # return f"No({self.identificador:6} | {lista_s} | {lista_pre})"
        return f"No({self.identificador})"
