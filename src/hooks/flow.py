import json
class Flow():
    def __init__(self):
        with open("../config/flow.json") as jsonFile:
                self.__flow = json.load(jsonFile)
                jsonFile.close()

    @property
    def flow(self):
        return self.__flow

    #Função para Recuperar o Estado de um usuario especifico.
    def get_state_by_id(self):
        return self



