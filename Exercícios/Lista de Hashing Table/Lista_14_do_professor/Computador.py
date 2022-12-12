class Computador():
  def __init__(self,ip:str, hardware:str):
    self.ip = ip
    self.hardware = hardware

  def __str__(self)->str:
    if self.ip is None:
      return None
    if self.ip and self.hardware != None:
      return f'{self.ip}, {self.hardware}'

  def __eq__(self, outro):
    return self.ip == outro.ip

  def __hash__(self)->int:
    return hash(self.ip)
    
    # Incrementei um método que mostre o ip  e o valor do ip

if __name__ == '__main__':
    c1 = Computador('192.168.0.1','intel i7 8GB RAM 1TB HD')
    c2 = Computador('192.168.0.2','intel i5 4GB RAM 500MB SSD')
    if c1 == c2:
        print('c1 é igual a c2') # pela chamada implícita ao método __eq__

    print(c1.__hash__())
    print(c2.__hash__())
    print(hash(c1))
