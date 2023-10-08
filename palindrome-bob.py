
import socket, time, requests
server = '45.76.177.238'
port = 5000

def send(mydata):
    s.send(mydata +b'\n\r')
    data = s.recv(1024)
    #print(data)
    data=data.decode('ascii')
    return (data)


def change(test_str):
    count=0
    res_first = test_str[0:len(test_str)//2] 
    res_second = test_str[len(test_str)//2 if len(test_str)%2 == 0
                                else ((len(test_str)//2)+1):] 
    # print((res_first))
    # print((res_second))
    for i in range(0,len(res_first)):
        if(res_first[i]==res_second[len(res_second)-i-1]):
            pass
        else:
            count=count+1
    return count


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f'trying to connect to {server}')
    s.connect((server,port))
    data = s.recv(1024)
    #print(data)
    f=0
    for i in range(0,1005):
        print('1st appear',data)
        data=(str(data).split(":")[1])
        
        if (f==0):
            data=str(data)[:-3]
            f=1
        data=data.replace(" ","")
        data=data.strip()
        print('going to count:',data)
        count=change(data)
        print(count)
    
        bfunc=bytes(str(count), 'utf-8')
        funcval= send(bfunc)
        print('Return from server',funcval)
        data= funcval
    


    
    # count=change(data)
    # funcval= (send(b'0'))

#print(change(s))
# s = "EQEFZfCpaEARLHLpjtRrJeqDUtcExIeEHQfggsJULjPVemYWwdWzYuMufZsUGOupOdeLZxVZwgwCafuCDLXcLliCNfGrkSaAwUtrVLhTqsrTEmPHjkJzzhmDkmusVKEdSYzDxTMkAlcEsevVzeICqoxCFvWpR"
# print(ob.solve(s))
# s="gRqznYfJDGwJDMiUhTGwjnepdzMYCEXyqOKzYCErTrDMRanZHfXsJAuKpMcRfCmjNsdopzDdrPtAahcdtTZlBzENjeMhLpqlyZSJCQKGnyGxhLTUfoRqcoPxzrfQcgNSdoHqJOESLyZucreIkBTmQDDrKlcaVwnapRQBJSxgAZsyHdtKEPLSGFYeENHGoEdtyM"
# print(minSwap(s))