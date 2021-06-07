class Queue:
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join(self.queue)
    def push(self, data):
        self.queue.insert(0, data)
    def is_empty(self):
        return self.size() == 0
    def pop(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'
    def size(self):
        return len(self.queue)
    def reverse(self):
        return self.queue.reverse()

def display(red, heat, error, blue, freeze):
    print('NORMAL :')
    print(len(red))
    print(''.join(str(a) for a in reversed(red)) if len(red) != 0 else 'Empty')
    print(f'{heat} Explosive(s) ! ! ! (NORMAL)')
    if error != 0:
        print(f'Failed Interrupted {error} Bomb(s)')
    print('------------MIRROR------------')
    print(': RORRIM')
    print(len(blue))
    blue.reverse()
    print(''.join(str(a) for a in blue) if len(blue) != 0 else 'ytpmE')
    print(f'(RORRIM) ! ! ! (s)evisolpxE {freeze}')


red, blue = input('Enter Input (Normal, Mirror) : ').split()
red = list(red)
blue = list(blue)
blue.reverse()

q, b_blue, freeze = Queue(), [], 0
for i, data in enumerate(blue):
    b_blue.append(data)
    if len(b_blue) > 2:
        if b_blue[-1] == b_blue[-2] == b_blue[-3]:
            q.push(data)
            freeze += 1
            for a in range(3):
                b_blue.pop()
q.reverse()
b_red, heat, error = [], 0, 0
for i, data in enumerate(red):
    b_red.append(data)
    if len(b_red) > 2:
        if b_red[-1] == b_red[-2] == b_red[-3]:
            bq_pop = q.pop()
            if data == bq_pop:
                for a in range(2):
                    b_red.pop()
                error += 1
            elif bq_pop == 'Empty':
                for a in range(3):
                    b_red.pop()
                heat += 1
            else:
                b_red.insert(-1, bq_pop)

display(b_red, heat, error, b_blue, freeze)

