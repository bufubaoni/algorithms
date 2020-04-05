import time
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = {}
        self.freq_key = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.data.get(key, -1)

        if val != -1:
            self.freq_key[key] = (self.freq_key[key][0]+1, time.time())
        return val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        ori = self.data.get(key, -1)
        if self.capacity == 0:
            return 
        if ori == -1:
            #没有达到容量
            if len(self.data) < self.capacity:
                if key not in self.freq_key:
                    self.freq_key[key] = (1, time.time())
                else:
                    self.freq_key[key] = (self.freq_key[key][0]+1, time.time())
            else:
                #达到容量 淘汰最少访问
                k = self.min_freq_key()
                self.data.pop(k)
                self.freq_key.pop(k)
                self.freq_key[key] = (1, time.time())
        else:
            self.freq_key[key] = (self.freq_key[key][0]+1, time.time())
        self.data[key] = value


    
    def min_freq_key(self):
        fr = sorted([(k, v) for k,v in self.freq_key.items()], key=lambda x : (x[1][0], x[1][1]))
        return fr[0][0]
# 不做非常复杂的时间和空间优化， 记录访问次数和最后一次访问的时间戳即可