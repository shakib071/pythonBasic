class Star_Cinema:
    hall_list=[]

    def entry_hall(self,object):
        if isinstance(object,Hall):
            self.hall_list.append(object)

class Hall:
    pass
