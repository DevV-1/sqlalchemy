###########queries (raw sql)

import sqlite3
from pathlib import Path

def read_sql_fun(sql_path : Path) -> str:
        return Path(sql_path).read_text()  #reading sql file as string

def main() :
    number_of_top_customers = int(input('How many top customers do you want?'))

    con = sqlite3.connect('database/db2.db')
    cur = con.cursor()
    # raw_sql = ''' 
    #                 SELECT 
    #                     c.ssn, c.fname,
    #                     SUM (i.iid) AS total
    #                 From Invoice i
    #                 LEFT JOIN Customer c on i.customer = c.ssn
    #                 GROUP BY c.ssn, c.fname
    #                 ORDER BY total DESC
    #                 LIMIT : limit;
    #                 '''
    # or    
    raw_sql = read_sql_fun('sql/sql2.sql')

    # for row in cur.execute(raw_sql, (number_of_top_customers,)):
    #     print(row)
    # or
    placeholder = {
        'limit' : number_of_top_customers
    }
    for row in cur.execute(raw_sql, placeholder):
        print(row)
    
if __name__=='__main__':
    main()
