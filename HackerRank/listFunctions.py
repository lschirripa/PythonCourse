listFunctions.py

def delegate(order):

    nombreDeOrden = order.split()[0]

    if(len(order.split())>1):
        par1 = int(order.split()[1])
    
    if(len(order.split())>2):
        par2 = int(order.split()[2])

    if nombreDeOrden == 'insert':
        userList.insert(par1,par2)
    elif nombreDeOrden == 'append':
        userList.append(par1)
    elif nombreDeOrden == 'remove':
        userList.remove(par1)
    elif nombreDeOrden == 'print':
        print(userList)
    elif nombreDeOrden == 'sort':
        userList.sort()
    elif nombreDeOrden == 'pop':
        userList.remove(userList[-1])
    elif nombreDeOrden == 'reverse':
        userList.reverse()

    #print(userList)


if __name__ == '__main__':
    N = int(input())

    userList = []

    orders = []

    for _ in range(N):
        orders.append(input())

    #print(f"ORDERS: {orders}")

    for order in orders:
        delegate(order)