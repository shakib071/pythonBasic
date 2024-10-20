class Engine:
    def __init__(self) -> None:
        pass 
    def  start(self):
        return "engine start"
    
class Driver:
    def __init__(self) -> None:
        pass

#car has a engine
#eta inheritance er ulta
class Car:
    def __init__(self) -> None:
        self.engine=Engine()
        self.driver=Driver()

    def start(self):
        self.engine.start()


