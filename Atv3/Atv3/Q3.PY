class Nodulo:    
  def __init__(self,data):    
    self.data = data    
    self.next = None   
     
class listaenca:    
  def __init__(self):    
        self.head = Nodulo(None)   
        self.tail = Nodulo(None)   
        self.head.next = self.tail   
        self.tail.next = self.head    
        
 
  def add(self,data):    
    newNode = Nodulo(data)    
       
    if self.head.data is None:    
        
      self.head = newNode   
      self.tail = newNode    
      newNode.next = self.head    
    else:
        self.tail.next = newNode     
        self.tail = newNode    
        self.tail.next = self.head 
     
  
  def display(self):    
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
    lista = listaenca()
    cont = 0
    # Lista de entrada
    lst = [1 , 3, 4, 2, 3, 2, 3, 2]
    # Valor de x
    num = 2
    for i in lst:
        lista.add(i)
        if num < i:
            cont += 1
        else:
            pass
    print("A lista possui", cont, "nó(s) de valor maior que:",num )
main()  
