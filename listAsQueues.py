# Using list as queues
# While using list as stack is efficient since append() and pop() method just adds and removes at end
# using llist as queue is inefficient since for append() and pop() at the beginning of the list
# needs us to shift each element one up

# To implement a queue, use collections.deque which was designed to have fast appends and pops
# from both ends. For example:

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)
print(queue.popleft(), " - was the First to arrive and has left first")  # Eric - The first to arrive now leaves
print(queue.popleft()," - was the Second to arrive and has left next")  # John - the second to arrive now leaves
print(queue , " are now remaining in the party")

