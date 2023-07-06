class LinkedList:
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self, array=[]):
        self.head = None
        if not array:
            return
        for i in array:
            self.append(i)

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def append(self, val):
        """
        Добавляет элемент в конец списка
        """
        if self.is_empty():
            self.head = self.Node(val)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = self.Node(val)
    
    def pop(self):
        """
        Удаляет 1-й элемент из списка и возвращает его
        """
        if self.is_empty():
            return None
        a = self.head.val
        self.head = self.head.next
        return a
    
    def value(self):
        """
        Возвращает значение первого узла. Если список пуст, возвращает значение выше предельного
        """
        if self.is_empty():
            return 10000
        return self.head.val
    
    def __str__(self):
        if self.is_empty():
            return '[]'
        s = '['
        node = self.head
        s += str(node.val)
        while node.next:
            node = node.next
            s += ', ' + str(node.val)
        s += ']'
        return s


    


class Solution:
    def mergeTwoLists(self, list1: LinkedList | None, list2: LinkedList | None) -> LinkedList | None:
        list3 = LinkedList()
        

        while 1:
            if list1.is_empty() and list2.is_empty():
                break
            a, b = list1.value(), list2.value()
            if a < b:
                list3.append(a)
                list1.pop()
            else:
                list3.append(b)
                list2.pop()

            
        
        return list3
    


        
if __name__ == "__main__":
    l1 = LinkedList([1, 1, 2, 4, 7])
    l2 = LinkedList([1, 3, 5])
    solution = Solution()
    print(solution.mergeTwoLists(l1, l2))