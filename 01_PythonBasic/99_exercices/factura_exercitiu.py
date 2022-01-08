class Client:
    def __init__(self, nume, cif, reg_com, adresa):
        self.nume = nume
        self.cif = cif
        self.reg_com = reg_com
        self.adresa =adresa

class Furnizor(Client):
    def __init__(self, nume, cif, reg_com, adresa, tel, email, cont, banca, tva, plata_tva):
        super().__init__(nume, cif, reg_com, adresa)
        self.tel = tel
        self.email = email
        self.cont = cont
        self.banca = banca
        self.tva = tva
        self.plata_tva = plata_tva

class Produs:
    def __init__(self, nume_prod, um, cant, pret):
        self.nume_prod = nume_prod
        self.um = um
        self.cant = cant
        self.pret = pret
        self.valoare = cant * pret
        # todo: fix val_tva

#class delegat


class Factura:
    def __init__(self, client, furnizor, produse, delegat):
        self.client = client
        self.furnizor = furnizor
        self.produse = produse
        self.delegat = delegat
    def afisare(self):
        print(f"{self.furnizor.nume: <30}")
        print(f"{'CIF: '+ self.furnizor.cif: <30}")
        print(f"{''}")



furnizor = Furnizor('Ionut', 'RO50432123', 'J05/9130/0345', 'Luceafarului 1b, Huedin', '0742293928', 'klaudiapoka@gmail.com', 'RO47BTRL00501236565656XX', 'Transilvania', 19, True)
client = Client('Andrei', 'RO12345678', 'J35/2001/2002', 'Bd. Republicii nr.2')
produs = Produs('ciocolata_milka', 'buc', 100, 50)
produs2 = Produs('suc', 'buc', 2, 10)
produs3 = Produs('seminte', 'buc', 1, 3)

produse = [produs, produs2, produs3]

factura = Factura(client, furnizor, produse, None)
factura.afisare()





