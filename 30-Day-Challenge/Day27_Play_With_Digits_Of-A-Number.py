def main():
    n = int(input())
    even,odd = 0,0
    while n > 0 :
        rem = n%10
        if rem%2 == 0:
            even += rem
        else:
            odd += rem
        n = int(n/10)
    print(int(abs(even-odd)))
    
main()

