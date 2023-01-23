# 1. 노드를 만든다. 여기에는 값과 다음 노드가 저장된다.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 2. linked-list를 만든다. 여기에는 Header와 나머지 Node를 저장한다.


class LinkedList:
    def __init__(self):
        self.head = None
        self.rest = None

    def append(self, new_value):
        new_node = Node(new_value)
        # 처음 입력되는 값이면, head와 rest에 모두 처음 노드를 넣는다.
        if self.head is None:
            self.head = new_node
            self.rest = new_node
        # 처음 node의 next에 두번째 노드가 들어가고, 그다음 rest를 두번쨰 node로 만든다
        # 3번째에는 두번째 노드의 next에 새번째가 들어가고, rest가 3번째 노드가 된다.
        else:
            self.rest.next = new_node
            self.rest = self.rest.next

    def values(self):
        start = self.head
        list_string = ""
        while start is not None:
            list_string += str(start.value)+' '
            start = start.next

        return list_string


if __name__ == '__main__':
    my_list = LinkedList()
    for i in range(6):
        my_list.append(i)

    print(my_list.values())
