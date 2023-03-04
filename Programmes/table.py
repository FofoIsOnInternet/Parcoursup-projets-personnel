def longest_word (lst:list,mini)->int:
    """takes a list of words and returns the lengh of the longest word"""
    length = mini  # minimum length of a comlumn
    for word in lst :
        if len(word) > length:
            length = len(word)
    return length

def abssign (value:int):
    if value != 0 :
        return 1
    return 0


class Table :
    def __init__ (self,name:str,headings:list,row_by_page=25):
        self.table_name = name
        self.headers = ["#"] + headings # list of names
        self.data = [] # list of dict
        self.max_row = row_by_page
        self.curent_page = 0
        self.column_black_list = []

    def insert_data (self,data:dict):
        """adds data to the table"""
        keys = list(data.keys())
        for var in self.headers :
            if var not in keys and var != "#":
                data[var]=""
        data["#"] = self.get_table_length()
        self.data.append(data)

    def remove_row (self,row:int):
        """will remove a row of data from the table"""
        if row < self.get_table_length():
            for line in range (row,len(self.data)):
                self.data[line]["#"] -= 1
            self.data = self.data[:row]+self.data[row+1:]
        else :
            raise IndexError ("row " + str(row) + " does not exists in " + self.table_name)

    def add_column (self,colunm_name:str,data=None):
        if data is None :
            data = ["" for x in range(self.get_table_length())]
        while len(data) < self.get_table_length() :
            data.append("")
        self.headers.append(colunm_name)
        for row in range(self.get_table_length()):
            self.data[row][colunm_name] = data[row]
    
    def del_column (self,column_name:str):
        if column_name in self.headers and column_name != "#":
            for i in range (len(self.headers)):
                if self.headers[i] == column_name :
                    del (self.headers[i])
            for row in range (self.get_table_length()) :
                del (self.data[row][column_name])

    def get_table_length (self)->int:
        """returns the length of the table"""
        return len(self.data)
    
    def get_columns_length(self)->dict:
        """returns a dictionay with the lenght of every column"""
        d = {}
        for column in self.headers:
            words = [str(row[column]) for row in self.data] # takes all the data of the column
            d[column] = longest_word(words,len(column))
        return d

    def get_pages (self)->int:
        """returns the amount of pages that can contain rows"""
        return ( self.get_table_length() // self.max_row ) + abssign(self.get_table_length() % self.max_row)

    def get_first_row(self,page)->int:
        """returns the index of the first row of the given page"""
        return self.max_row * page

    def get_last_row(self,page)->int:
        """returns the index of the last row of the given page"""
        if self.max_row * (page + 1) > self.get_table_length() :
            return self.get_table_length ()
        return self.max_row * ( page + 1 )

    def get_value (self,row:int,column:str):
        """returns the value detained by the specified row and column"""
        return self.data[row][column]
    
    def set_value (self,row:int,column:str,value):
        """change the value of the specified row and column"""
        self.data[row][column] = value
    
    def set_max_row_by_page (self,value:int):
        self.max_row = value

    def show_page (self,page:int):
        """returns a string with the given page to be shown"""
        string = self.table_name + " :\n"
        column_length = self.get_columns_length()
        
        # first row of the table
        string+= "┏"
        for column,length in column_length.items():
            if column not in self.column_black_list :
                string+= "━"*length + "┳"
        string = string[:-1] + "┓\n"

        # headers
        string+= "┃"
        for column in column_length.keys():
            if column not in self.column_black_list :
                string+= column + " " * ( column_length[column] - len(column)) + "┃"
        string+= "\n"

        #ending headers
        string+= "┣"
        for column,length in column_length.items():
            if column not in self.column_black_list :
                string+= "━"*length + "╋"
        string = string[:-1] + "┫"

        # insert data
        for index in range(self.get_first_row(page),self.get_last_row(page)) :
            row = self.data[index]
            string += "\n┃"
            for column in column_length.keys():
                if column not in self.column_black_list :
                    data = str(row[column])
                    string += data + " " * ( column_length[column] - len(data) ) + "┃"
        
        #end of the table
        string+= "\n┗"
        for column,length in column_length.items():
            if column not in self.column_black_list :
                string+= "━"*length + "┻"
        string = string[:-1] + "┛\n"
        
        # stats
        string += "row: " + str(self.get_last_row(page)) + "/" + str(self.get_table_length()) + " | page: " + str(page+1) + "/" + str(self.get_pages())

        return string
    
    def forward (self,pages=1):
        """shows the next pages"""
        if self.curent_page + pages < self.get_pages():
            self.curent_page += pages
        print(self)
    
    def backward (self,pages=1):
        """shows the previous pages"""
        if self.curent_page - pages >= 0:
            self.curent_page -= pages
        print(self)
    
    def hide_columns (self,columns:list):
        """will add the given list of columns to the list of column to hide when printing the table"""
        self.column_black_list += columns

    def show_columns (self,columns:list):
        """will remove the given list of columns from the list of columns to hide when printing the table"""
        for col in columns :
            for i in range (len(self.column_black_list)):
                if col == self.column_black_list[i] :
                    del(self.column_black_list[i])

    def __repr__ (self):
        return self.show_page(self.curent_page)

def export_csv (table:Table,delimiter=","):
    string = ""
    for column in table.headers :
        if column != "#" :
            string += column + delimiter
    for row in table.data :
        string += "\n"
        for column in table.headers :
            if column != "#" :
                string += str(row[column]) + delimiter
    with open ( "export_" + table.table_name + ".csv", mode = "w" , encoding="utf-8") as f :
        f.write(string)
        f.close()

def import_csv (file_directory:str,delimiter=",")->Table:
    if file_directory[-4:] == ".csv":
        with open(file_directory,"r",encoding="utf-8") as f: 
            headers = f.readline().split(delimiter)[:-1]
            lines = f.readlines()
            for k in range (len(lines)):
                while lines[k].find(",,") != -1 : # making sure that there's not any empty cell in that row, otherwise the split method of 'smth,,smth' will return [smth,smth] instead of [smth,,smth]
                    empty_cell_index = lines[k].find(",,")
                    lines[k] = lines[k][:empty_cell_index+1] + " " + lines[k][empty_cell_index+1:]
                lines[k] = lines[k].split(delimiter)[:-1]
            f.close
        file_name = file_directory.split("/")[-1]
        file_name = file_name[:file_name.find(".csv")]

        

        table = Table(file_name,headings=headers)
        for i in lines :
            row_data = {}
            for j in range (len(headers)):
                row_data[headers[j]] = i[j]
            table.insert_data(row_data)

        return table
    else :
        raise TypeError ("Given file is not a csv file")
