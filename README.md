# Yleiskuvaus tehtävästä

Tehtävän ideana on demonstroida Dockerin käyttöä yksinkertaisessa ympäristössä. Tehtävän tarkoituksena on luoda kaksi konttia käyttäen Dockeria ja saada tiedonsiirto toimimaan niiden välillä luodun verkon avulla.

## Ympäristön rakenne

### Docker Container

Docker Containerit eli kontit ovat tehtävässä **server** ja **client**.
Niiden toiminnot ja asetukset määritellään Dockerfile-tiedostoissa. Server-kontti toimii yksinkertaisena HTTP-palvelimena, kun taas client-kontti lähettää pyyntöjä serverille ja vastaanottaa vastauksia. Molemmat kontit liitetään samaan Docker-verkkoon, jotta ne voivat kommunikoida keskenään.

### Docker Volumes

Docker volyymit säilyttävät konttien dataa. Tässä tehtävässä:
- **servervol**: Tallentaa server-kontin luoman tiedoston ja tarkistussumman.
- **clientvol**: Tallentaa server-kontilta haetun tiedoston.

### Verkon luominen

Tehtävässä luodaan verkko, 'app-network', johon server- ja client-kontit liitetään. Verkko määritellään Docker Compose -tiedostossa.

### Docker Compose

Docker-compose.yml -tiedostossa määritellään Docker -ympäristömme rakenne. 
Tässä tehtävässä compose -tiedostoon on määritelty seuraavaa:
- **Version**. Docker Compose -tiedoston versio.
- **Services (kontit)**. Tehtävässä on käytössä kaksi eri konttia (server ja client). Konteille on määritelty mm. build, volumes, networks, ports ja commands.
- **Volume**. Määritellään volyymit, jotka liitetään client- ja server-kontteihin.
- **Networks**. Määritellään verkko, joka luodaan ja johon kontit kiinnitetään.

## Konttien rakentaminen / ajaminen

Kontit voidaan rakentaa ajamalla luonti scriptit :
```bash
./server/serversetup.sh
./client/clientsetup.sh
```
Kontit voidaan myös rakentaa komennolla:
```bash
docker-compose up --build
```
Konttien pitäisi ajaa tarvittavat sovellukset käynnistyessään automaattisesti, mutta tässä nyt vielä prosessi manuaalisesti toteutettuna:
 1. Luodaan volyymit:
```bash
docker volume create servervol
docker volume create clientvol
```
 2. Luodaan verkko:
```bash
docker network create app-network
```
 3. Rakennetaan ja käynnistetään server-kontti server-hakemistossa:
```bash
docker build -t server ./server
docker run -d --name server --network app-network -v servervol:/serverdata -p 5000:5000 server
```
 4. Rakennetaan ja käynnistetään client-kontti client-hakemistossa:
```bash
docker build -t client ./client
docker run -d --name client --network app-network -v clientvol:/clientdata client python client.py --server-url http://server:5000
```

## Tiedoston siirron todentaminen

1. Aloitetaan tarkistamalla kaikki kontit:
```bash
docker ps -a
```

2. Tarkistetaan client-kontin lokit:
```bash
docker logs <client-kontin ID>
```

Jos kaikki on onnistunut, meidän pitäisi nähdä: "File transfer successful and checksum verified."

3. Tarkistetaan siirretyn tiedoston sisältö:

Tämän voi tehdä kahdella eri tavalla:
 **Tapa 1.** Siirrytään client-konttiin ja tarkistetaan, että tiedosto löytyy sieltä:
```bash
docker exec -it <client-kontin ID> /bin/bash

ls /clientdata
cat /clientdata/random.txt
```

 Tai **Tapa 2.** Kopioidaan siirretty tiedosto omalle koneelle client-kontista:
 ```bash
 docker cp <client-kontin ID>:/clientdata/random.txt ./random.txt
 cat ./random.txt
 ```

### Yhteenveto

Tässä tehtävässä opittiin luomaan ja konfiguroimaan Docker-kontteja, sekä niille tärkeitä volyymeja ja verkkoja. Lisäksi opittiin käyttämään Docker Composea monikonttisen ympäristön hallinnassa. Lopuksi varmistettiin, että tiedonsiirto konttien välillä toimii.
