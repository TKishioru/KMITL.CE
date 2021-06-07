tree = []
i = 0
j = 0

num = input("Enter Input : ").split(',')
for i in range(len(num)):
   #A
   if len(num[i].split()) == 2:
      x = num[i].split()
      h = int(x[1])
      tree.append(h)
   #B
   else:
      n = 0
      highmax = 0
      l = len(tree) - 1
      for j in range(l,-1,-1):
         if tree[j] > highmax:
            highmax = tree[j]
            n+=1
      print(n)