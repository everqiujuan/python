
import collections

# 队列：先进先出,后进后出

# 双向队列

# 创建队列
queue = collections.deque()
# print(queue)  # deque([])

# 入队列
# append() : 从队列的右边加入元素
# appendleft() : 从列表的左边加入元素
queue.append('A')
print(queue)  # deque(['A'])

queue.append('B')
print(queue)  # deque(['A', 'B'])

queue.append('C')
print(queue)  # deque(['A', 'B', 'C'])

# queue.appendleft('Q')
# print(queue)  # deque(['Q', 'A', 'B', 'C'])


# 出队列
# pop() : 在队列的右边弹出元素
# popleft() : 在队列的左边弹出元素
queue.popleft()
print(queue)  # deque(['B', 'C'])

queue.popleft()
print(queue)  # deque(['C'])

queue.popleft()
print(queue)  # deque([])

# queue.pop()
