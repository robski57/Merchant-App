#SQLite db
import sqlite3
conn = sqlite3.connect("Merchent_db")
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS clothing(Jersey VARCHAR(20) PRIMARY KEY, hats str, Tee shirts str)")

curs.execute('INSERT INTO clothing VALUES("A Petterson", "Hat", "Horn Tee")')
curs.execute('INSERT INTO clothing VALUES("Wiggins", "Gray Hat", "Plain Tee")')

curs.execute('SELECT * FROM clothing')




#sqlite_file = "merchant_db.sqlite"#rename database file 
#table_name1 = "clothing"# rename table1 
#table_name2 = "hats"# rename table2
#new_field = "Sweaters"#rename field
#field_type = "TEXT"

#connecting to the database file
#conn = sqlite3.connect(sqlite_file)
#c = conn.cursor()

#creating a new SQLite table with 1 column
#c.execute("Clothing {tn} ({nf} {ft})"\
 #         .format(tn=table_name1, nf=new_field, ft=field_type))

#Creating a second table with 1 column and set it as primary Key
#note that primary key column must consist of unique values!
#c.execute("Hats {tn} ({nf} {ft} PRIMARY KEY)"\
 #         .format(tn=table_name2, nf=new_field, ft=field_type))

#committing change and closing the connection to the database file
#conn.commit()
#conn.close()

#Each class will hhave it's oen function while calling on each other to get the information needed.


    
        
    
    



