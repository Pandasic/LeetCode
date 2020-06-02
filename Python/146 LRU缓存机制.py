"""
146. LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ??? 超时了？？？

class LRUCache_timetick:
    def __init__(self, capacity: int):
        self.datas = {}
        #操作计数 用于管理时间
        self.tick = 0
        self.maxSize = capacity

    def get(self, key: int) -> int:
        self.tick += 1
        if key not in self.datas:
            return -1
        else:
            self.datas[key][1] = self.tick
            return self.datas[key][0]

    def put(self, key: int, value: int) -> None:
        self.tick += 1
        if key in self.datas:
            self.datas[key][1] = self.tick
            self.datas[key][0] = value
        else:
            if len(self.datas) >= self.maxSize:
                datalist = list(self.datas.items())
                self.datas.pop(min(datalist,key= lambda x:x[1][1])[0])
            self.datas[key] = [value,self.tick]

class LRUCache:
    def __init__(self, capacity: int):
        self.datas = {}
        #用于维护时间的队列
        self.actionQueue = []
        
        self.maxSize = capacity

    def get(self, key: int) -> int:
        if key not in self.datas:
            return -1
        else:
            self.actionQueue.remove(key)
            self.actionQueue.append(key)
            return self.datas[key]

    def put(self, key: int, value: int) -> None:
        if key in self.datas:
            self.actionQueue.remove(key)
            self.actionQueue.append(key)
            self.datas[key] = value
        else:
            if len(self.datas) >= self.maxSize:
                oldkey = self.actionQueue.pop(0)
                self.datas.pop(oldkey)
            self.actionQueue.append(key)
            self.datas[key] = value

LUR = LRUCache(2)
print(LUR.put(1,1))
print(LUR.put(2,2))
print(LUR.get(1))
print(LUR.put(3,3))
print(LUR.get(2))
print(LUR.put(4,4))
print(LUR.get(1))
print(LUR.get(3))
print(LUR.get(4))
