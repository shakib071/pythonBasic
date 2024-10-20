

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no

    def entry_show(self,show_id,movie_name,time):

        temp_obj=(show_id,movie_name,time)
        self.show_list.append(temp_obj)
    
    def allocate_seats(self):
        seats=[['free' for _ in range(self.cols) for _ in range(self.rows)]] #2D list]
        self.seats={self.hall_no: seats}

    def book_seats(self,show_id,list):

        for show in self.show_list:
            if show[0]==show_id:
                for row,col in list:
                    if 0<=row<self.rows and 0<=col<self.cols:
                        if self.seats[self.hall_no][row][col]=='free':
                            self.seats[self.hall_no][row][col]='Booked'
                            print(f'Your Chosen Seat ({row}, {col}) booked succesfully')
                        else:
                            print(f'Your Chosen Seat ({row}, {col}) Already booked ')
                    
                    else:
                        print(f'your chosen seat does not exist')
                return
        print(f'The Show_id {show_id} was not exist')

            



class Star_Cinema(Hall):
    hall_list=[]

    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)


# h1=Star_Cinema(1,2,3)
# h2=Star_Cinema(2,3,4)

# for hall in Star_Cinema.hall_list:
#     print(hall.hall_no,hall.rows,hall.cols)

hal1=Hall(10,10,1)

hal1.entry_show('s1',"Alur chop","12:12 PM")
hal1.allocate_seats()
hal1.book_seats('s1',[(1,1),(0,0)])


