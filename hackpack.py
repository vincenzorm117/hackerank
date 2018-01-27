#!/usr/local/bin/python3


####################################################################################
####################################################################################
####################################################################################
####################################################################################

class BitVector:
	def __init__(self, size=1):
		if not isinstance(size, int):
			size = 1
		self.vector = [0] * size

	def __getitem__(self, i):
		if not isinstance(i, int):
			return False
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			return False
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		return ((1 << index & chunk) >> index) == 1

	def __setitem__(self, i, val):
		if not isinstance(i, int):
			return None
		if isinstance(val, bool):
			val = bool(val)
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			self.vector.extend([0] * (1 + (chunkIndex - len(self.vector))))
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		if val:
			chunk |= (1 << index)
		else:
			chunk &= ~(1 << index)
		self.vector[chunkIndex] = chunk

	def print(self):
		for v in self.vector:
			for i in range(64):
				print(((1 << i & v) >> i), end="")
		print()



####################################################################################
####################################################################################
####################################################################################
####################################################################################

class LinkedList:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def insert(self, data):
		self.count += 1
		if self.head is None:
			self.head = self.tail = self.Node(data)
			return
		self.tail.next = self.Node(data)
		self.tail = self.tail.next

	def find(self, data):
		curr = self.head
		while curr is not None and curr.data != data:
			curr = curr.next
		return Node if curr is None else curr

	def remove(self, data):
		def _remove(data):
			self.count -= 1
			if self.tail is None:
				return
			elif self.tail == self.head and self.tail.data == data:
				del self.head
				self.__init__()
				return
			elif self.head.data == data:
				d = self.head
				self.head = self.head.next
				del d
			else:
				prev = self.head
				while prev.next is not None and prev.next.data != data:
					prev = prev.next
				if prev.next is None:
					return
				d = prev.next
				if prev.next == self.tail:
					self.tail = prev
				prev.next = prev.next.next
				del d
		if type(self.head.data) == type(data):
			return _remove(data)
		elif isinstance(data, (tuple, list)):
			for l in data:
				_remove(l)
		else:
			return _remove(data)


	def print(self):
		curr = self.head
		while curr is not None:
			print(curr, end=" ")
			curr = curr.next
		print()

####################################################################################
####################################################################################
####################################################################################
####################################################################################

class DoubleLinkedList:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
			self.prev = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def insert(self, data):
		self.count += 1
		if self.head is None:
			self.head = self.tail = self.Node(data)
			return
		self.tail.next = self.Node(data)
		self.tail.next.prev = self.tail
		self.tail = self.tail.next

	def find(self, data):
		curr = self.head
		while curr is not None and curr.data != data:
			curr = curr.next
		return Node if curr is None else curr

	def remove(self, data):
		def _remove(data):
			self.count -= 1
			if self.tail is None:
				return
			elif self.tail == self.head and self.tail.data == data:
				del self.head
				self.__init__()
				return
			elif self.head.data == data:
				d = self.head
				self.head = self.head.next
				del d
				self.head.prev = None
			elif self.tail.data == data:
				d = self.tail
				self.tail = self.tail.prev
				del d
				self.tail.next = None
			else:
				prev = self.head
				while prev.next is not None and prev.next.data != data:
					prev = prev.next
				if prev.next is None:
					return
				d = prev.next
				prev.next = prev.next.next
				prev.next.prev = prev
				del d
		if type(self.head.data) == type(data):
			return _remove(data)
		elif isinstance(data, (tuple, list)):
			for l in data:
				_remove(l)
		else:
			return _remove(data)


	def print(self):
		curr = self.head
		while curr is not None:
			print(curr, end=" ")
			curr = curr.next
		print()


####################################################################################
####################################################################################
####################################################################################
####################################################################################


class Stack:
	def __init__(self, size = 16):
		if not isinstance(size, int) or size <= 0:
			size = 16
		self.items = [None] * size
		self.size = size
		self.top = 0
		self.count = 0

	def isEmpty(self):
		return self.top == 0

	def isFull(self):
		return self.top == self.size

	def push(self, item):
		if self.isFull():
			self.items = self.items + [None] * self.size
			self.size *= 2
		self.items[self.top] = item
		self.top += 1
		self.count += 1

	def pop(self):
		if self.isEmpty():
			return None
		self.top -= 1
		self.count -= 1
		return self.items[self.top]

	def peek(self):
		if self.isEmpty():
			return None
		return self.items[self.top - 1]


####################################################################################
####################################################################################
####################################################################################
####################################################################################

class Queue:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
			self.prev = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.head = self.tail = None
		self.count = 0

	def isEmpty(self):
		return self.count == 0

	def add(self, item):
		self.count += 1
		if self.head is None:
			self.head = self.tail = self.Node(item)
			return
		self.tail.next = self.Node(item)
		self.tail.next.prev = self.tail
		self.tail = self.tail.next


	def remove(self):
		if self.head is None:
			return None
		self.count -= 1
		d = self.head
		self.head = self.head.next
		item = d.data
		del d
		if self.head is None:
			self.tail = None
		return item

	def peek(self):
		return self.head.data if self.count == 0 else None


####################################################################################
####################################################################################
####################################################################################
####################################################################################


class BinaryTree:
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None

	def insert(self, data, path):
		if self.root is None:
			self.root = self.Node(data)
			return
		curr = self.root
		for isLeft in path:
			if isLeft:
				if curr.left is not None:
					curr = curr.left
				else:
					curr.left = self.Node(data)
					continue
			else:
				if curr.right is not None:
					curr = curr.right
				else:
					curr.right = self.Node(data)
					continue


	def find(self, data):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			if c.data == data:
				return c
			if c.left is not None:
				q.append(c.left)
			if c.right is not None:
				q.append(c.right)

	def empty(self):
		return self.root == None

	def print(self):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			print(c)
			if c.left is not None:
				q.append(c.left)
			if c.right is not None:
				q.append(c.right)
		print()

	def height(self):
		if self.root is None:
			return 0
		q = [(0,self.root)]
		max = 0
		while 0 < len(q):
			c = q.pop(0)
			if max < c[0]:
				max = c[0]
			if c[1].left is not None:
				q.append((c[0]+1, c[1].left))
			if c[1].right is not None:
				q.append((c[0]+1, c[1].right))
		return max+1



####################################################################################
####################################################################################
####################################################################################
####################################################################################



class BST:
	class Node:
		def __init__(self, data):
			self.data = data
			self.children = [None,None]
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None
		self.height = 0

	def insert(self, data):
		if self.root is None:
			self.height = 1
			self.root = self.Node(data)
			return
		curr = self.root
		height = 0
		while curr is not None:
			height += 1
			index = 0 if data <= curr.data else 1
			if curr.children[index] is None:
				curr.children[index] = self.Node(data)
				height += 1
				break
			else:
				curr = curr.children[index]
		self.height = max(self.height, height)

	def find(self, data):
		curr = self.root
		while curr is not None and curr.data != data:
			curr = curr.children[0] if data <= curr.data else curr.children[1]
		return curr

	def pathToNode(self, data):
		if self.root is None or self.height <= 0:
			return []
		path = [None] * self.height
		q = [(self.root, 0)]
		while 0 < len(q):
			c = q.pop()
			path[c[1]] = c[0]
			if c[0].data == data:
				return path[:c[1]+1]
			if c[0].left is not None:
				q.append((c[0].left, c[1]+1))
			if c[0].right is not None:
				q.append((c[0].right, c[1]+1))
		return []

	def empty(self):
		return self.root == None

	def print(self):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			print(c, end=" ")
			if c.children[0] is not None:
				q.append(c.children[0])
			if c.children[1] is not None:
				q.append(c.children[1])
		print()

	def parent(self, node):
		if node is None or self.root is None:
			return None
		if node.data == self.root.data:
			return None
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			if c.children[0] is not None:
				if c.children[0].data == node.data:
					return c
				q.append(c.children[0])
			if c.children[1] is not None:
				if c.children[1].data == node.data:
					return c
				q.append(c.children[1])
		return None

	def remove(self, data):
		def maxSubtreeVal(root):
			subtreeMax = (-2 ** 64, None)
			if root is None:
				return subtreeMax
			c = root
			while True:
				if subtreeMax[0] < c.data:
					subtreeMax = (c.data, c)
				if c.children[1] is None:
					break
				c = c.children[1]
			return subtreeMax


		if self.root is None:
			return None
		delnode = self.find(data)
		parent = self.parent(delnode)
		if delnode is None:
			return None
		subtree = (delnode.children[0] is None, delnode.children[1] is None)

		if subtree[0] and subtree[1]:
			if parent is None:
				self.root = None
			elif parent.children[0] == delnode:
				parent.children[0] = None
			elif parent.children[1] == delnode:
				parent.children[1] = None
			del delnode
		elif subtree[0]:
			if parent is None:
				self.root = delnode.children[1]
			elif parent.children[0] == delnode:
				parent.children[0] = delnode.children[1]
			elif parent.children[1] == delnode:
				parent.children[1] = delnode.children[1]
			del delnode
		elif subtree[1]:
			if parent is None:
				self.root = delnode.children[0]
			elif parent.children[0] == delnode:
				parent.children[0] = delnode.children[0]
			elif parent.children[1] == delnode:
				parent.children[1] = delnode.children[0]
			del delnode
		else:
			self.print()
			newDelNode = maxSubtreeVal(delnode.children[0])
			self.remove(newDelNode[0])
			delnode.data = newDelNode[0]


####################################################################################
####################################################################################
####################################################################################
####################################################################################



class Graph():
	def __init__(self, data=[]):
		if not isinstance(data, list):
			data = []
		self.V = data[:]
		self.count = len(self.V)
		self.E = []
		for i in range(self.count):
			self.E.append([None] * self.count)

	def add(self, data):
		self.V.append(data)
		self.count += 1
		for E in self.E:
			E.append(None)
		self.E.append([None] * self.count)

	def remove(self, index):
		if not isinstance(index, int):
			return None
		if index < 0 or index <= self.count:
			return None
		ret = self.V[index]
		del self.V[index]
		del self.E[index]
		for e in self.E:
			del e[index]
		return ret

	def print(self):
		for e in self.E:
			print(e)

	def edge(self, a, b, val=None):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				return self.E[a][b]
		return None

	def connect(self, a, b, v = True):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				self.E[a][b] = v

	def size(self):
		return len(self.V)

	def empty(self):
		return len(self.V) == 0


####################################################################################
####################################################################################

def top_sort(G):
	if not isinstance(G, Graph) or G.count <= 0:
		return None
	visited = [False] * G.count
	q = []
	for i in range(G.count):
		noOutEdges = True
		for j in range(G.count):
			if G.E[i][j]:
				noOutEdges = False
				break
		if noOutEdges:
			q.append(i)
	order = []
	for n in q:
		order.append(G.V[n])
		p = [n]
		visited[n] = True
		while 0 < len(p):
			c = p.pop(0)
			for i in range(G.count):
				if G.E[i][c] and not visited[i]:
					p.append(i)
					visited[i] = True
					order.append(G.V[i])
	order.reverse()
	return order


####################################################################################
####################################################################################
####################################################################################
####################################################################################
# Sorting functions


def bubbleSort(a):
	if a is not List:
		return None
    L = len(a)
    for i in range(L):
        for j in range(L-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
	return a



####################################################################################
####################################################################################
####################################################################################
####################################################################################
# Nice Functions

####################################################################################
# Combinatorics Functions

def nCk(bag, k):
	L = len(bag)
	if k < 0 or L < k:
		return None
	chosen = []
	q = [([], k, 0)]
	while 0 < len(q):
		c = q.pop()
		if c[1] == 0:
			chosen.append(c[0])
			continue
		for i in range(c[2], L):
			N = c[0][:]
			N.append(bag[i])
			q.append((N, c[1]-1, i+1))
	return chosen


def powerset(bag):
	L = len(bag)
	chosen = []
	for k in range(L+1):
		q = [([], k, 0)]
		while 0 < len(q):
			c = q.pop()
			if c[1] == 0:
				chosen.append(c[0])
				continue
			for i in range(c[2], L):
				N = c[0][:]
				N.append(bag[i])
				q.append((N, c[1]-1, i+1))
	return chosen


def possibilities(bags):
		if not isinstance(bags, list) or len(bags) <= 0:
			return None
		s = [None] * len(bags)
		stack = []
		for n in bags[0]:
			stack.append((n,0))
		while 0 < len(stack):
			c = stack.pop()
			s[c[1]] = c[0]
			nxt = c[1]+1
			if len(s) <= nxt:
				print(s)
			else:
				for c in bags[nxt]:
					stack.append((c,nxt))


def permute(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	stack = [(l,0)]
	sols = []
	while 0 < len(stack):
		c = stack.pop()
		if c[1] == L:
			sol = []
			for i in c[0]:
				sol.append(i)
			sols.append(sol)
		else:
			for i in range(c[1],L):
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
				stack.append((c[0][:], c[1]+1))
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
	return sols


def permute_no_dups(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	stack = [(l,0)]
	sols = set()
	while 0 < len(stack):
		c = stack.pop()
		if c[1] == L:
			sol = []
			for i in c[0]:
				sol.append(i)
			print(sol,tuple(sol))
			sols.add(tuple(sol))
		else:
			for i in range(c[1],L):
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
				stack.append((c[0][:], c[1]+1))
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
	return sols

# Assymptotically faster than permute_no_dups
def permute_no_dups2(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	mp = {}
	for c in l:
		if c not in mp:
			mp[c] = 0
		mp[c] += 1
	res = []
	keys = mp.keys()
	q = [([], L, mp)]
	while 0 < len(q):
		pre, k, mp = q.pop()
		if k == 0:
			res.append(pre)
			continue
		for c in keys:
			count = mp[c]
			if 0 < count:
				mp[c] = count - 1
				q.append((pre + [c], k - 1, mp.copy()))
				mp[c] = count
	return res


def genvals(N, alpha):
	if N <= 0:
		return []
	alpha = vals = [[s] for s in alpha]
	if N <= 1:
		return alpha
	for i in range(N-1):
		n = []
		for l in vals:
			for a in alpha:
				n.append(l + a)
		vals = n
	return n


####################################################################################
# Math functions

def is_prime(N):
	if not isinstance(N, int):
		return None
	if N <= 1:
		return False
	isPrime = [True] * (N+1)
	for i in range(2,N):
		if isPrime[i]:
			for c in range(i*i,N+1,i):
				isPrime[c] = False
	return isPrime[N]

def list_of_primes(N):
	if not isinstance(N, int):
		return None
	if N < 0:
		return []
	isPrime = [True] * (N+1)
	isPrime[0] = False
	if 1 <= N:
		isPrime[1] = False
	for i in range(2,N):
		if isPrime[i]:
			for c in range(i*i,N+1,i):
				isPrime[c] = False
	return isPrime


def log(b,x):
	c = 0
	while b <= x:
		x /= b
		c += 1
	return c


def fibonacci(n):
    # Write your code here.
    fib0, fib1 = 0, 1
    for i in range(n-1):
        if i % 2 == 0:
            fib0 = fib0 + fib1
        else:
            fib1 = fib0 + fib1
    return fib0 if n % 2 == 0 else fib1

def fib(n):
	if not isinstance(n, int) or n < 0:
		return None
	if n == 0 or n == 1:
		return n
	f = [0,1]
	for i in range(n-1):
		f[i%2] = f[0] + f[1]
	return f[n%2]


def print_grid(g):
	n,m = len(g), len(g[0])
	for y in range(n):
		for x in range(m):
			print(g[y][x], end=" ")
		print()


def gcd(a,b):
    while( a != 0 ):
        c = a
        a = b % a
        b = c
    return b



####################################################################################
# Bitwise functions

def hamming_distance(N):
	if not isinstance(N, int):
		return 0
	count = 0
	while 0 < N:
		count += 1
		N = N & (N - 1)
	return count


def power_of_2(N):
	return (N & (N-1)) == 0
