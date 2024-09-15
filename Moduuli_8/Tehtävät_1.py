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

icao_koodi = input("Anna lentokentän ICAO-koodi: ")

kursori = yhteys.cursor()

sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_koodi}'"

kursori.execute(sql)

tulos = kursori.fetchone()

print(f"Lentokentän nimi: {tulos[0]}, Sijaintikunta: {tulos[1]}")

