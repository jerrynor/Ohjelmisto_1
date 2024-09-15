import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="syksy2024",
    database="flight_game",
    autocommit=True,
    collation='utf8mb4_general_ci'
)

maakoodi = input("Anna maakoodi: ")

kursori = yhteys.cursor()

sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type"

kursori.execute(sql)

tulos = kursori.fetchall()

for rivi in tulos:
    print(f"Type: {rivi[0]} lkm: {rivi[1]}")

