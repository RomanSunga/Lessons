class LinkedList:
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head: Item = None

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
        if self.head:
            self.head = self.head.next

    def remove_last(self):
        current = self.head
        if current and not current.next:
            self.head = None
            return
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
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
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def remove_last_value(self, value):
        current = self.head
        previous = None
        last_occurrence = None
        while current:
            if current.value == value:
                last_occurrence = current
            previous = current
            current = current.next
        if last_occurrence:
            if previous:
                previous.next = last_occurrence.next
            else:
                self.head = last_occurrence.next
   

my_list = LinkedList()
my_list.append_end(2)
my_list.append_end(3)
my_list.append_end(4)
my_list.append_by_index(5, 2)
if my_list.head:
    for value in my_list.get_items():
        print(value)
my_list.remove_first()
my_list.remove_last()
my_list.remove_at(1)
my_list.remove_first_value(3)
my_list.remove_last_value(4)
print(my_list.head.value if my_list.head else "Лист пуст")
if my_list.head:
    for value in my_list.get_items():
        print(my_list)

