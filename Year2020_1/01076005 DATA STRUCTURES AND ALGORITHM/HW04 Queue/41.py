class Queue():
  def __init__(self,list =None):
    if list==None:
      self.items = []
    else: self.items = list
      
  def enQueue(self,i):
    self.items.append(i)
    
  def deQueue(self):
    if self.items!= []: return self.items.pop(0)
    
  def isEmpty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)

def showList(list):
    e =''
    if list!=[]:
        for i in range(len(list)):
            if i == len(list)-1: e = e+str(list[i])
            else: e = e+str(list[i])+', '
        return e
    else: return 'Empty'
  
  
inpQ = input('Enter Input : ').split(',')
q = Queue()
deQueue_data = []
for i in inpQ:
  if len(i)>1: 
    q.enQueue(i[-1])
    print(showList(q.items))
  else:
    if not q.isEmpty():
        last_dequeque = q.deQueue()
        deQueue_data.append(last_dequeque)
        e = str(last_dequeque)+' <-'
        print(e,showList(q.items))
    else: print('Empty')
print(showList(deQueue_data),':',showList(q.items))
    