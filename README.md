# JBlajic_PZW_project

## O projektu

**Food scout** je web aplikacija za razmjenu i pregledavanje jela (food blog) izrađena u Pythonu koristeći Flask framework i MongoDB bazu podataka. Aplikacija omogućuje korisnicima da objavljuju, uređuju i brišu vlastite recepte/jela, pregledavaju jela drugih korisnika, te označavaju omiljena jela (pin/unpin). Također, korisnici mogu uređivati svoj profil, a administratori imaju dodatne mogućnosti upravljanja korisnicima.

## Ključne funkcionalnosti

- Registracija i prijava korisnika
- Potvrda email adrese nakon registracije
- Objavljivanje, uređivanje i brisanje jela
- Pregled svih objavljenih jela
- Pin/Unpin (označavanje omiljenih) jela
- Pregled vlastitih objava i omiljenih jela
- Uređivanje korisničkog profila
- Administratorsko sučelje za upravljanje korisnicima

## Kako koristiti aplikaciju

1. **Registracija i prijava**
   - Registrirajte se s email adresom i nazivom restorana.
   - Potvrdite email putem linka koji ćete dobiti na email adresu.
   - Prijavite se s registriranim podacima.

2. **Objavljivanje i pregled jela**
   - Nakon prijave možete objavljivati nova jela, uređivati i brisati vlastite objave.
   - Sva jela su vidljiva na početnoj stranici.

3. **Pin/Unpin jela**
   - Klikom na gumb "Pin" ili "Unpin" možete označiti ili ukloniti jelo iz svojih omiljenih.
   - Sva označena jela možete pregledati na stranici "Pinned dishes".

4. **Upravljanje profilom**
   - U profilu možete mijenjati podatke i postaviti profilnu sliku.

5. **Administracija**
   - Administrator može pregledavati i uređivati sve korisnike.

## Tehnologije

- Python, Flask, Flask-Login, Flask-Bootstrap, Flask-Mail, Flask-Principal
- MongoDB (PyMongo, GridFS)
- Bootstrap 5

