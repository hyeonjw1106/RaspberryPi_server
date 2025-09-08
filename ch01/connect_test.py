import pymysql

#1. 연결하기
conn = pymysql.connect(host='localhost', user='hyeonjw', password='aa090700!!00', db='shopping_db_bemssang')
#2. 커서
cur = conn.cursor()
#3. 쿼리 작성
cur.execute('select avg(age) from Customer where address="경기"')
#4. 결과값 조회
result = cur.fetchone()
print(int(result[0]))
#5. 종료(연결해제)
cur.close()
conn.close()
