class node():
    def __init__(self,c):
        self.next = {}
        self.fail = None
        self.end = False
        self.word = c

class ac_auto():
    def __init__(self):
        self.root = node("root")
    def add(self,words):
        curnode = self.root
        for c in words:
            if c in curnode.next.keys():
                curnode = curnode.next[c]
            else:
                curnode.next[c] = node(c)
                curnode = curnode.next[c]
        curnode.end = True
    def fail(self):
        que = []
        que.append(self.root)
        while(len(que) != 0):
            cur = que.pop(0)
            for key,value in cur.next.items():
                p = cur.fail
                while p is not None:
                    if key in p.next.keys():
                        print(p.word)
                        cur.next[key].fail = p.next[key]
                    else:
                        p = p.fail
                if p is None:
                    cur.next[key].fail = self.root
                que.append(cur.next[key])
    def search(self,words):
        cur = self.root
        for c in words:
            while c not in cur.next.keys():
                cur = cur.fail
                if(cur == self.root):
                    break
            if(c not in cur.next.keys()):
                cur = self.root
                continue
            else:
                cur = cur.next[c]
        if cur.end:
            print("ok")
        else:
            print("fail")
