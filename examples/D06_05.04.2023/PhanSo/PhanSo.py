import math

class PhanSo:
    tu_so: int
    mau_so: int
    
    def __init__(self, tu, mau) -> None:
        self.tu_so = tu
        self.mau_so = mau
        
    def __str__(self) -> str:
        return f"{self.tu_so}/{self.mau_so}"
    
    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so /= ucln
        self.mau_so /= ucln
    
    def __add__(self, other):
        tu_so_moi = self.tu_so * other.mau_so + self.mau_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        
        phan_so_moi = PhanSo(tu_so_moi, mau_so_moi)
    
# Demo
ps1 = PhanSo(1, 2)
ps2 = PhanSo(2, 3)
print(ps1, ps2)
ps3 = ps1 + ps2
print(ps3)