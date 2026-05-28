print("🎊"*58)

def menu():
    while True:
        print("1.Create Member")
        print("2.Create Sports")
        print("3.Create Coach")
        print("4.Create Batches")

        x=int(input("enter your choice : "))
        if x==1:
            createmember()
        elif x==2:
            createsports()
        elif x==3:
            createcoach()
        elif x==4:
            createbatches()
        else:
            print("Invalid choice")

def createmember():
    import mysql.connector as con
    conn = con.connect(host='localhost', user='root', password='pass@123', database='sports_club')
    cur = conn.cursor()
    i=[]
    cur = conn.cursor()
    a=int(input("enter members id :"))
    i.append(a)
    b=input("enter members name :")
    i.append(b)
    c=int(input("enter members age :"))
    i.append(c)
    d=input("enter members date of joining :")
    i.append(d)
    e=int(input("enter members mobile no. :"))
    i.append(e)
    f=input("enter members email :")
    i.append(f)
    g=input("enter members address :")
    i.append(g)
    h=input("enter members type :")
    i.append(h)
    sql="insert into member(memid, memname, age,doj, phone, email, address,memtype) values(%i,%s,%i, %d,%i, %s,%s,%s)"
    r=tuple(i)
    #cur.execute("create table member(memid int primary key, memname varchar(40) not null, age int, doj date, phone varchar(10), email varchar(60) unique, address varchar(100), memtype varchar(20)")
    cur.execute(sql,r)
    conn.commit()
    print("details inserted")


def createsports():
    import mysql.connector as con
    conn = con.connect(host='localhost', user='root', password='pass@123', database='sports_club')
    cur = conn.cursor()
    k=[]
    cur = conn.cursor()
    z=int(input("enter student id:"))
    k.append(z)
    y=input("enter student name:")
    k.append(y)
    x=input("enter student category:")
    k.append(x)
    w=input("enter equipment:")
    k.append(w)
    sql="insert into sports (stuid,stuname,category, equipment) values(%i,%s,%s,%s)"
    v=tuple(k)
    #cur.execute("create table coach(cid int primary key,cname varchar(30) not null,stuid int,experience int,phone varchar(10),email varchar(50),address varchar(100)")
    cur.execute(sql,v)
    conn.commit()
    print("details inserted")


def createcoach():
    import mysql.connector as con
    conn = con.connect(host='localhost', user='root', password='pass@123', database='sports_club')
    cur = conn.cursor()
    m=[]
    cur = conn.cursor()
    n=int(input("enter coach id:"))
    m.append(n)
    o=input("enter coach name:")
    m.append(o)
    p=int(input("enter student id:"))
    m.append(p)
    q=int(input("enter coach experience:"))
    m.append(q)
    s=int(input("enter coach mobile no.:"))
    m.append(s)
    t=input("enter coach email:")
    m.append(t)
    u=input("enter coach address:")
    m.append(u)
    sql="insert into coach (cid,cname,stuid,experience, phone, email,address) values(%i,%s,%s,%i,%i,%s,%s)"
    ab=tuple(m)
    print(ab)
    #cur.execute("create table sports(stuid int primary key,stuname varchar(50) not null,category varchar(100),equipment varchar(100)")
    cur.execute(sql,ab)
    conn.commit()
    print("details inserted")

def createbatches():
    import mysql.connector as con
    conn = con.connect(host='localhost', user='root', password='pass@123', database='sports_club')
    cur = conn.cursor()
    bc=[]
    cur = conn.cursor()
    cd=int(input("enter batch id:"))
    bc.append(cd)
    de=input("enter batch name:")
    bc.append(de)
    ef=eval(input("enter duration of batch:"))
    bc.append(ef)
    fg=eval (input("enter timings:"))
    bc.append(fg)
    gh=int(input("enter coach id:"))
    bc.append(gh)
    hi=int(input("enter fees:"))
    bc.append(hi)
    sql="insert into batches(bid,bname,days, btime,cid, fees) values(%i,%s,%d,%d,%i,%i)"
    ii=tuple(bc)
    #cur.execute("create table batches(bid int primary key, bname varchar(30),days varchar(10),btime varchar(20),cid int,fees int")
    cur.execute(sql,ii)
    conn.commit()
    print("details inserted")
menu()
