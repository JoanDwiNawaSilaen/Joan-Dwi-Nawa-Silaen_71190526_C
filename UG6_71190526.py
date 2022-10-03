class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

    def insertHead(self, no_rekening):
        no_rekening = None(no_rekening)
        no_rekening._simpan = self.no_rekening
        self.no_rekening = no_rekening
        self._size += 1
        print("Data masuk di head")

    def delete(self, no_rekening):
        now = self.no_rekening
        before = NodeTabungan(None, now)
        temu = False
        for i in range(0, self.no_rekening):
            if self.no_rekening is None:
                temu = True
                self.next = None
                self._size -= 1
                break
            else:
                now = now.


