class student:
    def __init__(self):
        self.name = '' * 20
        self.score = 0
        self.next = None


front = student()
rear = student()
front = None
rear = None


def enqueue(name, score):
    global front
    global rear
    new_data = student()
    new_data.name = name
    new_data.score = score
    if rear == None:
        front = new_data
    else:
        rear.next = new_data
    rear=new_data
    new_data.next=None
def dequeue():
    global front
    global rear
    if front==None:
        print('queue empty')
    else:
        print ('firstname %s\t  Grade:%d.....catch' %(front.name,front.score))
        front= front.next
def show():
    global front
    global rear
    ptr = front
    if ptr==None:
        print('empty')
    else:
        while ptr !=None:
            print('name: %s\t Grade: %d' %(ptr.name,ptr.score))
            ptr=ptr.next
select=0
while True:
    select=int(input('1 save 2catch 3sidplay 4exit'))
    if select==4:
        break
    if select==1:
        name=input('name')
        score=int(input('score'))
        enqueue(name,score)
    elif select==2:
        dequeue()
    else:
        show()
