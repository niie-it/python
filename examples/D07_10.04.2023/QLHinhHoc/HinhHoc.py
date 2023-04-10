from math import pow, pi

class HinhHoc:
    dien_tich: float = 0
    chu_vi: float = 0
    
    def __str__(self) -> str:
        return "Hình học"
    
    def tinh_dien_tich_chu_vi(self):
        pass
    
class HinhChuNhat(HinhHoc):
    dai: float = 0
    rong: float = 0
    
    def __init__(self, d, r) -> None:
        self.dai = d
        self.rong = r
        
    def tinh_dien_tich_chu_vi(self):
        self.dien_tich = self.dai * self.rong
        self.chu_vi = (self.dai + self.rong)*2
        
    def __str__(self) -> str:
        return f"HCN {self.dai}x{self.rong} có S = {self.dien_tich}, P = {self.chu_vi}"

class HinhTron(HinhHoc):
    ban_kinh: float = 0
    
    def __init__(self, r) -> None:
        self.ban_kinh = r
        
    def tinh_dien_tich_chu_vi(self):
        self.dien_tich = pow(self.ban_kinh, 2) * pi
        self.chu_vi = 2 * self.ban_kinh * pi
        
    def __str__(self) -> str:
        return f"Tròn {self.ban_kinh} có S = {self.dien_tich}, P = {self.chu_vi}"