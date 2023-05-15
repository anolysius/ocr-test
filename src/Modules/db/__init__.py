# Database connection
import psycopg2

class db:
    def __init__(self):
        pass;

# conn = psycopg2.connect("dbname=qr_test host=localhost user=postgres password=123456 port=5432")
    # cur = conn.cursor()
    # cur.execute("select * from information_schema.columns")
    # cur.execute("SET search_path TO aricosystem")
    # cur.execute("select * from donor")
    # test = tuple('hello')
    # result = cur.fetchone()
    # testString = '-'.join(map(str, result))
    # for record in result:
    #     print(type(record))
    #     print(record[0])
    #     print(record[1])
    # print(cur)
    # print(conn)