class LinkedList:
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head: Item = None

    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count

    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return

        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index):
        new_item = LinkedList.Item(value)
        if index == 0:
            new_item.next = self.head
            self.head = new_item
        else:
            current = self.head
            position = 0
        while position < index - 1 and current.next:
            current = current.next
            position += 1
        new_item.next = current.next
        current.next = new_item


    def get_items(self):
        current = self.head
        while current != None:
            yield current.value                
            current = current.next

    def remove_first(self):
        if self.head is not None:
            
            self.head = self.head.next
        else:
            raise ValueError('')
    def remove_last(self):
        current = self.head
        if current == None:
            raise ValueError('')
        elif current.next is None:
            self.head = None
            return
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
    
        if self.head == None:
            raise ValueError('')
        if index == 0:
            self.remove_first()
            return
        current = self.head
        current_index = 0
        while current_index < index - 1 and current.next:
            current = current.next
            current_index += 1
        if current.next is None:
            self.remove_last()
        else:
            current.next = current.next.next

    def remove_first_value(self, value):
        if self.head == None:
            raise ValueError('')
        current = self.head
        previous = None
        tot = 0
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        
        if tot == 0:
            raise ValueError('')

    def remove_last_value(self, rem):
        if self.head is None:
            raise ValueError('')
        current = self.head
        while current.next is not None:
            if current.next.value == rem:
                current.next = current.next.next
                return
            current = current.next

        if self.head.value == rem:
            self.head = self.head.next
            return
        else:
            raise ValueError('')
        

