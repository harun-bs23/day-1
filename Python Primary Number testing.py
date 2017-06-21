import math

maxN = 10000007;

flag=[];

index={};
index2={};

def sieve():

    flag.append(0);
    flag.append(0);

    for i in range(2,maxN):
        flag.append(1);

    limit = int(math.sqrt(maxN))+1;

    i=2;
    idx=1;

    while(i<limit):

        if(flag[i]==1):
            index[i]=idx;
            index2[idx]=i;
            idx=idx+1;
            Limit = maxN;
            j=i*i;

            while(j<Limit):
                flag[j]=0;
                j=j+i;
        i=i+1;


sieve();

for i in range(1,25):
    print(index2[i]);

while(1):

    m=input();
    n=int(input());

    if(m[0]=='c'):
        if(flag[n]==1):
            print(n,"is prime");
        else:
            print("FALSE RESULT");

    elif(m[0]=='p'):
        print("index of prime ",n," is ", index[n]);

    elif(m[0]=='f'):
        idx=1;
        L=[];
        while(index2[idx]<n):
            L.append(index2[idx]);
            idx=idx+1;
        idx=0;
        print("tuples are (");
        while(idx<len(L)):
            print(L[idx]);
            idx=idx+1;
            if(idx<len(L)):
                print(',');
        print(')');

    else:
        break;
