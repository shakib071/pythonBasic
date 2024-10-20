class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no


class Star_Cinema(Hall):
    hall_list=[]

    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)


h1=Star_Cinema(1,2,3)
h2=Star_Cinema(2,3,4)

for hall in Star_Cinema.hall_list:
    print(hall.hall_no,hall.rows,hall.cols)


