class create_node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class linked_list():
    def __init__(self) -> None:
        self.head = None
    def add_at_end(self, data):
        nod = create_node(data)
        a = self.head
        if not a:
            self.head = nod
            return
        while a.next:
            a = a.next
        a.next = nod
    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count +=1
        return count 
    def add_at_beg(self, data):
        ins = create_node(data)
        a = self.head
        if not a:
            self.head =  ins
            return
        else:
            self.head = ins
            ins.next = a
    def get_items(self):
        count = 0
        a = self.head
        while a:
            print(a.data)
            a = a.next
            count += 1
        return
    def insrect_at_pos(self, data, position):
        ins = create_node(data)
        p = position
        a = self.head
        c = 0 
        if position > self.size():
            return "value not found"
        elif position == 1:
            self.add_at_beg(data)
        else:
            while c < position - 2:
                a = a.next
                c += 1
            
            ins.next = a.next
            a.next = ins 
             
            return
        
            
    
    

no = linked_list()
no.add_at_end("Hello world")
no.add_at_end("HEY")
no.add_at_end(10)
no.add_at_beg("i am added at beg")
no.insrect_at_pos("hello", 2)

#print(no.size())
no.get_items()

