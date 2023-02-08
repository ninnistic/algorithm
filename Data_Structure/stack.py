class Stack:

    # 인스턴스 변수로 리스트 초기화
    def __init__(self):
        self.items = []

    # 빈 배열인지 확인하는 인스턴스 메소드
    def isEmpty(self):
        return self.items == []

    # 리스트의 뒤쪽으로 값을 넣는 push 메소드
    def push(self, item):
        self.items.append(item)

    # 리스트의 뒤에서부터 값을 빼는 pop 메소드
    def pop(self):
        return self.items.pop()

    # 배열의 길이를(크기를) 알아내는 메소드
    def size(self):
        return len(self.items)
