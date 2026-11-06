class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = max(tilavuus, 0.0)
        self.saldo = max(min(alku_saldo, self.tilavuus), 0.0)

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return

        self.saldo = self.saldo + maara if maara <= self.paljonko_mahtuu() else self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        else:
            if maara > self.saldo:
                if self.saldo == 0.0:
                    return 0
                else:
                    kaikki_mita_voidaan = self.saldo
                    self.saldo = 0.0
                    return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
