
def isEmpty():  # Bool
    return front == rear


def isFull():  # Bool
    return (rear + 1) % len(q) == front


def enQueue(item):  # Queue에 data 삽입시, rear 포인터 이동
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear + 1) % len(q)
        q[rear] = item


def deQueue():  # Queue에 data 삽입시, front 포인터 이동
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(q)
        return q[front]


for tc in range(1, 11):
    t = int(input())
    data = list(map(int, input().split()))
    q = [None] * 10000
    rear = front = 0
    counts = 1

    for i in range(8):
        enQueue(data[i])

    while q[-1] != 0:

