class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

N = 100

root = Node(2)
previous = root
for i in range(3, N, 2):
    node = Node(i)
    previous.next = node
    node.prev = previous
    previous = node
last_node = previous

current = root
limit = int(last_node.value ** 0.5)

while current and current.value <= limit:
    candidate = current.next
    while candidate:
        if candidate.value % current.value == 0:
            if candidate.prev:
                candidate.prev.next = candidate.next
            if candidate.next:
                candidate.next.prev = candidate.prev
            if candidate == last_node:
                last_node = candidate.prev
        candidate = candidate.next
    current = current.next

primes = []
node = root
while node:
    print(node.value, end = ' <-> ')
    node = node.next