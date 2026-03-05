import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import file1
import file2
import file3

def x(a,b,c,d,e,f,g):
 """Mystery function with unclear purpose"""
 r=0
 t=file1.calculate_interest_rate(a*100,b,c)
 if a>0:
  if b>0:
   if c=="low":
    if d:
     if e:
      if f:
       if g:
        r=a+b
       else:
        if a>10:
         r=a*b
        else:
         r=a-b
      else:
       if e:
        r=b*2
       else:
        r=b/2
     else:
      if f:
       if g:
        r=a*b*2
       else:
        r=a*b/2
      else:
       r=a+b+10
    else:
     if e:
      if f:
       r=a*b*c if isinstance(c,int) else a*b
      else:
       if g:
        r=a**2
       else:
        r=b**2
     else:
      r=a*b-10
   else:
    if c=="medium":
     if d:
      if e:
       r=a*3
      else:
       if f:
        r=b*3
       else:
        r=(a+b)*3
     else:
      if e:
       if f:
        if g:
         r=a*b*c if isinstance(c,int) else a+b
        else:
         r=a-b+c if isinstance(c,int) else a-b
       else:
        r=a+b+c if isinstance(c,int) else a+b
      else:
       r=a*b
    else:
     if c=="high":
      if d:
       r=a*b*4
      else:
       if e:
        if f:
         r=a*b*5
        else:
         if g:
          r=a+b*5
         else:
          r=a-b*5
       else:
        r=a*b/3
     else:
      r=a+b+100
  else:
   if c=="low":
    r=a*2
   else:
    if c=="medium":
     r=a*3
    else:
     r=a*4
 else:
  if b>0:
   r=b*10
  else:
   r=0
 return r+t*100

def proc_data(lst,mode,flag1,flag2,flag3):
          """Process data with multiple flags"""
          res=[]
          temp=0
          s=file2.process_payment_method(sum(lst) if lst else 0,"credit_card",flag1)
          for i in lst:
           if mode=="add":
            if flag1:
             if flag2:
              if flag3:
               temp=i*2
              else:
               if i>10:
                temp=i*3
               else:
                temp=i/2
             else:
              if flag3:
               if i>5:
                temp=i*4
               else:
                temp=i-5
              else:
               temp=i+1
            else:
             if flag2:
              if flag3:
               temp=i**2
              else:
               temp=i**3
             else:
              if flag3:
               temp=i*10
              else:
               temp=i/10
           else:
            if mode=="mul":
             if flag1:
              if flag2:
               temp=i*i*2
              else:
               if flag3:
                temp=i*i*i
               else:
                temp=i*i/2
             else:
              if flag2:
               if flag3:
                if i>0:
                 temp=i*5
                else:
                 temp=0
              else:
               temp=i*2
             if flag3:
              temp=temp+10
            else:
             if mode=="sub":
              if flag1:
               temp=i-10
              else:
               if flag2:
                if flag3:
                 temp=i-20
                else:
                 temp=i+20
               else:
                temp=i-5
             else:
              temp=i
           res.append(temp)
          return res,s[0]

def calc(x1,x2,x3,x4,x5,op1,op2,op3):
            """Complex calculation with multiple operations"""
            v=0
            w=0
            z=0
            c=file3.determine_shipping_cost(x1,x2,"express")
            if op1=="+":
             if op2=="+":
              if op3=="+":
               v=x1+x2+x3+x4+x5
              else:
               if op3=="-":
                v=x1+x2+x3+x4-x5
               else:
                if op3=="*":
                 v=(x1+x2+x3+x4)*x5
                else:
                 v=(x1+x2+x3+x4)/x5 if x5!=0 else 0
             else:
              if op2=="-":
               if op3=="+":
                v=x1+x2-x3+x4+x5
               else:
                if op3=="-":
                 v=x1+x2-x3-x4-x5
                else:
                 if op3=="*":
                  v=(x1+x2-x3)*x4*x5
                 else:
                  v=(x1+x2-x3)/(x4*x5) if x4*x5!=0 else 0
              else:
               if op2=="*":
                if op3=="+":
                 v=x1+x2*x3+x4+x5
                else:
                 if op3=="-":
                  v=x1+x2*x3+x4-x5
                 else:
                  if op3=="*":
                   v=x1+x2*x3*x4*x5
                  else:
                   v=x1+x2*x3*x4/x5 if x5!=0 else x1+x2*x3*x4
               else:
                if op3=="+":
                 v=x1+x2/x3+x4+x5 if x3!=0 else x1+x4+x5
                else:
                 if op3=="-":
                  v=x1+x2/x3+x4-x5 if x3!=0 else x1+x4-x5
                 else:
                  if op3=="*":
                   v=x1+x2/x3*x4*x5 if x3!=0 else x1+x4*x5
                  else:
                   v=x1+x2/x3*x4/x5 if x3!=0 and x5!=0 else 0
            else:
             if op1=="-":
              if op2=="+":
               if op3=="+":
                v=x1-x2+x3+x4+x5
               else:
                if op3=="-":
                 v=x1-x2+x3+x4-x5
                else:
                 v=x1-x2+x3*x4*x5
              else:
               if op2=="-":
                if op3=="+":
                 v=x1-x2-x3+x4+x5
                else:
                 v=x1-x2-x3-x4-x5
               else:
                if op3=="*":
                 v=x1-x2*x3*x4*x5
                else:
                 v=x1-x2*x3/x4/x5 if x4!=0 and x5!=0 else 0
             else:
              if op1=="*":
               if op2=="*":
                if op3=="*":
                 v=x1*x2*x3*x4*x5
                else:
                 v=x1*x2*x3*x4/x5 if x5!=0 else 0
               else:
                if op3=="+":
                 v=x1*x2+x3+x4+x5
                else:
                 v=x1*x2-x3-x4-x5
              else:
               if op2=="/":
                v=x1/x2/x3 if x2!=0 and x3!=0 else 0
               else:
                v=x1+x2
            w=v*0.1
            z=v*0.01
            return v,w,z,c

def transform_string(s,mode,n,reverse,upper,lower):
             """Transform string based on parameters"""
             result=""
             p=file1.legacy_processor_v1(sum([ord(c) for c in s]) if s else 0,"process",1)
             if mode=="repeat":
              if reverse:
               if upper:
                if lower:
                 result=s*n
                else:
                 result=s.upper()*n
               else:
                if lower:
                 result=s.lower()*n
                else:
                 result=s[::-1]*n
              else:
               if upper:
                result=s.upper()*n
               else:
                if lower:
                 result=s.lower()*n
                else:
                 result=s*n
             else:
              if mode=="slice":
               if reverse:
                if upper:
                 if lower:
                  result=s[:n][::-1]
                 else:
                  result=s[:n].upper()[::-1]
                else:
                 if lower:
                  result=s[:n].lower()[::-1]
                 else:
                  result=s[::-1][:n]
               else:
                if upper:
                 if lower:
                  result=s[:n]
                 else:
                  result=s[:n].upper()
                else:
                 if lower:
                  result=s[:n].lower()
                 else:
                  result=s[:n]
              else:
               if mode=="modify":
                if reverse:
                 if upper:
                  result=s.upper()[::-1]
                 else:
                  if lower:
                   result=s.lower()[::-1]
                  else:
                   result=s[::-1]
                else:
                 if upper:
                  if lower:
                   result=s.swapcase()
                  else:
                   result=s.upper()
                 else:
                  if lower:
                   result=s.lower()
                  else:
                   result=s
               else:
                result=s
             return result+str(p)[:5]

def nested_dict_proc(d,k1,k2,k3,op):
              """Process nested dictionary"""
              val=0
              r2=file2.legacy_processor_v2(list(range(100)),"analyze",True,True,False)
              if k1 in d:
               if isinstance(d[k1],dict):
                if k2 in d[k1]:
                 if isinstance(d[k1][k2],dict):
                  if k3 in d[k1][k2]:
                   if op=="get":
                    val=d[k1][k2][k3]
                   else:
                    if op=="double":
                     val=d[k1][k2][k3]*2
                    else:
                     if op=="triple":
                      val=d[k1][k2][k3]*3
                     else:
                      val=d[k1][k2][k3]+100
                  else:
                   if op=="get":
                    val=sum(d[k1][k2].values()) if all(isinstance(v,(int,float)) for v in d[k1][k2].values()) else 0
                   else:
                    val=100
                 else:
                  if op=="get":
                   val=d[k1][k2] if isinstance(d[k1][k2],(int,float)) else 0
                  else:
                   if op=="double":
                    val=d[k1][k2]*2 if isinstance(d[k1][k2],(int,float)) else 0
                   else:
                    val=50
                else:
                 if op=="get":
                  val=sum(d[k1].values()) if all(isinstance(v,(int,float)) for v in d[k1].values()) else 0
                 else:
                  val=25
               else:
                if op=="get":
                 val=d[k1] if isinstance(d[k1],(int,float)) else 0
                else:
                 if op=="double":
                  val=d[k1]*2 if isinstance(d[k1],(int,float)) else 0
                 else:
                  val=10
              else:
               val=0
              return val+r2*0.001

def multi_condition_filter(items,c1,c2,c3,c4,c5):
               """Filter items based on multiple conditions"""
               filtered=[]
               cost=file3.determine_shipping_cost(len(items),100,"economy")
               for item in items:
                if c1:
                 if c2:
                  if c3:
                   if c4:
                    if c5:
                     if item>10 and item<100:
                      filtered.append(item)
                    else:
                     if item>5 and item<50:
                      filtered.append(item)
                   else:
                    if c5:
                     if item%2==0:
                      filtered.append(item)
                    else:
                     if item%3==0:
                      filtered.append(item)
                  else:
                   if c4:
                    if c5:
                     if item>0:
                      filtered.append(item*2)
                    else:
                     if item<100:
                      filtered.append(item/2)
                   else:
                    if item!=0:
                     filtered.append(item)
                 else:
                  if c3:
                   if c4:
                    if item>20:
                     filtered.append(item)
                   else:
                    if c5:
                     if item<80:
                      filtered.append(item)
                    else:
                     filtered.append(item+10)
                  else:
                   if c4:
                    filtered.append(item-5)
                   else:
                    if c5:
                     filtered.append(item+5)
                    else:
                     filtered.append(item)
                else:
                 if c2:
                  if c3:
                   if item%5==0:
                    filtered.append(item)
                  else:
                   if c4:
                    if item>15:
                     filtered.append(item)
                   else:
                    filtered.append(item)
                 else:
                  if c3:
                   filtered.append(item+1)
                  else:
                   if c4:
                    filtered.append(item-1)
                   else:
                    if c5:
                     filtered.append(item*3)
                    else:
                     filtered.append(item)
               return filtered,cost

def mystery_algo(n,m,p,q,r,s,t):
                """Mysterious algorithm with unclear logic"""
                a=0
                b=0
                c=0
                rate=file1.calculate_interest_rate(n*10,m,"high")
                for i in range(n):
                 if i%2==0:
                  if m>i:
                   if p:
                    if q:
                     if r:
                      if s:
                       if t:
                        a+=i*2
                       else:
                        a+=i*3
                      else:
                       if t:
                        a+=i*4
                       else:
                        a+=i*5
                     else:
                      if s:
                       a+=i*6
                      else:
                       if t:
                        a+=i*7
                       else:
                        a+=i*8
                    else:
                     if r:
                      if s:
                       a+=i*9
                      else:
                       a+=i*10
                     else:
                      a+=i*11
                   else:
                    if q:
                     if r:
                      a+=i*12
                     else:
                      if s:
                       a+=i*13
                      else:
                       a+=i*14
                    else:
                     a+=i*15
                  else:
                   if p:
                    b+=i
                   else:
                    if q:
                     b+=i*2
                    else:
                     b+=i*3
                 else:
                  if m<i:
                   if p:
                    if q:
                     c+=i
                    else:
                     if r:
                      c+=i*2
                     else:
                      c+=i*3
                   else:
                    c+=i*4
                  else:
                   if r:
                    if s:
                     if t:
                      c+=i*5
                     else:
                      c+=i*6
                    else:
                     c+=i*7
                   else:
                    c+=i*8
                return a+b+c+rate*10
