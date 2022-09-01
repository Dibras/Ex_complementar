class N:    
  def __init__(self,data):    
    self.data = data    
    self.next = None   
     
class L:    
  def __init__(self):    
        self.head = N(None)   
        self.tail = N(None)   
        self.head.next = self.tail   
        self.tail.next = self.head    
        
 
  def add(self,data):    
    newNode = N(data)    
       
    if self.head.data is None:    
        
      self.head = newNode   
      self.tail = newNode    
      newNode.next = self.head    
    else:
        self.tail.next = newNode     
        self.tail = newNode    
        self.tail.next = self.head 
     
  
  def mostrar(self):    
    current = self.head;    
    if self.head is None:    
        print("List is empty")   
        return 
    else:    
        cont = 0
        while(current.next != self.head):
            current = current.next
            cont += 1    
        print("A lista contem",cont+1,"elementos")
 
def main():
    lista = L()
    
    # Lista de entrada
    s = [1 , 3, 4, 2, 3, 2, 3, 2]
    # Valor de x
    x = 2
    for i in s:
        lista.add(i)
    # Tamanho da lista
    lista.mostrar()
main()  
