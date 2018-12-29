import sqlite3

conn = sqlite3.connect("db_spider.sqlite")
cur = conn.cursor()

cur.execute('''
            SELECT  COUNT(FROM_ID) AS INBOUND,
                    OLD_RANK,
                    NEW_RANK,
                    ID,
                    URL
            FROM    PAGES
            JOIN    LINKS
                ON  PAGES.ID = LINKS.TO_ID
            WHERE   HTML IS NOT NULL
            GROUP BY ID
            ORDER BY INBOUND DESC
            ''')

count = 0
for row in cur:
    if count < 50:
        print(row)
    count = count + 1
print(count, "rows.")
cur.close()
