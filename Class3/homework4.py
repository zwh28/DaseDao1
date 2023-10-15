class Listnode(object): #定义节点类
    def __init__(self,data=0,next=None):
        self.data = data
        self.next=next

class List(object):   #链表类
    def __init__(self):
        self.head=None
    def create(self,data):  #构建链表
        self.head=Listnode(data[0])
        current=self.head
        for i in data[1:]:
            p=Listnode(i)
            current.next=p
            current=p
        return self.head
    def tarvel(self):#遍历输出
        if self.head:
            p = self.head
            while p:
                print(p.data, end=' ')  # 依次输出数据
                p = p.next
            print('')
        else:
            return

    def select(self, value): #查找
        if self.head:
            count = 1
            p = self.head
            while p:
                if p.data == value:
                    print(f'在第{count}个节点')
                    break
                else:
                    p = p.next
                    count += 1
            if p == None:
                print('不存在')
        else:
            return None
    def remove(self, value):  #删除
        if self.head:
            p = self.head
            while p:
                if p.next.data == value:  # 获取到要删除节点的上一个节点
                    p.next = p.next.next  # 把下一个获取到的节点指向下下个节点
                    print('删除成功')
                    break
                else:
                    p = p.next
            if p == None:
                print('删除失败')
        else:
            return None

    def insert(self, value, n): #插入
        q = Listnode(value)  # 创建一个节点
        if n == 0:  # 判断是否插入作为第一个节点
            q.next = self.head
            self.head = q  # 新节点作为头结点
        else:
            p = self.head
            count = 1
            while count < n:
                p = p.next
                count += 1
            q.next = p.next
            p.next = q
            print('插入成功')

    def update(self, value, n):  #修改
            if self.head:
                p = self.head
                count = 1
                while count < n:
                    p = p.next
                    count += 1
                p.data = value
                print('修改成功')
            else:
                return None
li=List()
li.create([x for x in range(10)])
li.tarvel()
li.remove(5)
li.select(6)
li.insert(19,5)
li.update(100,1)
li.tarvel()

