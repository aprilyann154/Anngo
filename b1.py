graph={"I":{"II": 20, "III": 15, "V":80},
       "II":{"I": 40, "V": 10, "VI": 30},
       "III":{"I": 20, "II": 4, "VI": 10},
       "IV":{"I": 36, "II": 18, "II": 15},
       "V":{"III": 90, "IV": 15},
       "VI":{"III": 45, "IV": 4, "V": 10}}

def print_path_and_cost(start, goal, parent, g):
    path=[]
    current=goal
    while current!= start:
        path.append(current)
        current=parent[current]
    path.append(start)
    path.reverse()
    print("Duong di: ", '->'.join(path))
    print("C(p)= ", g[goal])
   
def AT(graph, start, goals):
    MO= [start] #danh sach cac dinh cho duoc duyet
    g={start:0} #Chi phia toi tung dinh
    DONG=[] #Danh sach cac dinh da xet xong
    parent={} #Luu tru cha cua moi dinh

    while MO:
    #Lay dinh n co chi phi g(n) nho nhat tu tap MO
        min_cost=float('inf')
        n=None
        for vertex in MO:
            if vertex in g:
                cost= g[vertex]
            else:
                cost=float('inf')
            if cost< min_cost:
                min_cost= cost
                n= vertex

        if n in goals:
            print_path_and_cost(start, n, parent, g)
            return True

        MO.remove(n) #Xoa dinh n khoi tap MO
        DONG.append(n) #Them dinh n vao tap da xet

        for m in graph.get(n, {}): #duyet qua cac dinh lien ke cua m
            cost=graph[n][m] #chi phi tu n den m
            new_cost=g.get(n, float('inf')) +cost

        #Neu m da co cha va duong di moi ngan hon
            if m in parent and new_cost<g[m]:
                g[m]=new_cost
                parent[m]=n

        #Neu m chua duoc duyet
            elif m not in MO and m not in DONG:
                g[m]=new_cost
                parent[m]=n 
                MO.append(m)

    return False #Khong thay duong di den dinh dich

start="I"
goals=["VI","V"]
AT(graph, start, goals)
