from  math import log2
class Sol:
     def count_prime(self,n):
         count=1
         if n==2:return 1
         if n==3:return 2
         for i in range(4,n+1):
             for j in range(2,int(log2(i))+2):
                 if i%j==0 :
                     count += 1

                     break
         num=n-count
         return num
if __name__ == '__main__':
    p1=Sol()
    print(p1.count_prime(13))
