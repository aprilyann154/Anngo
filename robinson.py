def phu(x):
    if x[0]=='-':
        return x[1:]
    else:
        return '-' + x

def res(a,b):
    check =False    #Tao bien check, kiem tra xem a voi b la phu cua nhau khong
    ans=list(set(a+b))   #Dung set de loai bo phan tu giong nhau va dung list de convert lai kieu List
    for i in ans[:]:     #Ktra trong tap ans
        if phu(i) in ans :  #Neu a va -a cung ton tai trong ans
            ans.remove(i)    #Thi loai bo chung
            ans.remove(phu(i))
            check=True  #Neu trong ans chua ca a va -a thi gan check=True

    return sorted(ans), check            

def robinson(TAP):
    TAP=TAP.split(",")   #Cat tap thanh cac mang
    so=1              #Bien luu stt cua dong
    my_dict={}          #Tao 1 tu dien my_dict de luu cac dong
    for menh_de in TAP:  #Chia nho tung phan tu de luu cac quan he
        my_dict[so]=sorted(menh_de.split("v"))    #Cat bieu thuc va luu duoi dang List sap xep
        so+=1

    for key, val in my_dict.items():     #In ra man hinh cac dong khoi tao
        print("{:>3}.  {}".format(key, val))

    da_duyet=set()      #Tao tap da duyet de luu caccap da kiem tra
    for i in list(my_dict.keys()):         #Chon tuan tu cac cap dong chua trong my_dict
        for j in list(my_dict.keys())[i:]:   #Chon duyet tu dong thu....
            if (i,j) not in da_duyet:     #Neu 2 dong chua duyet
                tam, check=res(my_dict[i], my_dict[j])       #Thi tam= recuse(a,b)
                da_duyet.update({(i,j),(i,so),(j,so)})    #Cap nhat danh sach da_duyet
                if not check:         #Neu a va b khong co menh de phu cua nhau
                    continue           # Ta bo qua vong lap
                if not tam:            #Neu dong nay la rong (=={})
                    print("{:>3}.Res({:>2},{:>3})={}".format(so, i,j,tam))   #In ra man hinh
                    print("=> Vay bai toan duoc chung minh")
                    return True              #Thi ta ve True, dung vong lap
                if tam not in my_dict.values():   #Neu tam khong la 1 trong cac dong da co
                    print("{:>3}.Res({:>2},{:>3})={}".format(so,i,j,tam)) #In ra man hinh
                    my_dict[so]=tam        #Them vao my_dict
                    so+=1      
    #print(da_duyet)
    return False

TAP="-av-bvc,-bv-cvd,a,b,-e"
TAP1="-av-bvc,-gvd,-cvd,a,b,-d"
print(robinson(TAP))