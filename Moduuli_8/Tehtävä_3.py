import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="syksy2024",
    database="flight_game",
    autocommit=True,
    collation='utf8mb4_general_ci'
)


ICAO_koodi1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
ICAO_koodi2 = input("Anna toisen lentokentän ICAO-koodi: ")

kursori = yhteys.cursor()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

kursori.execute(sql, (ICAO_koodi1,))
maa1 = kursori.fetchone()

kursori.execute(sql, (ICAO_koodi2,))
maa2 = kursori.fetchone()


koordinaatti1 = (maa1[0], maa1[1])
koordinaatti2 = (maa2[0], maa2[1])

etaisyys = geodesic(koordinaatti1, koordinaatti2).kilometers


print(f"Lentokenttien {ICAO_koodi1} ja {ICAO_koodi2} välinen etäisyys on {etaisyys} km.")



