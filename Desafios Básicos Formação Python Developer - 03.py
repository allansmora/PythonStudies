n = int(input())
i = 0
print_final = []
while(i < n):
    a,b = input().split()
    
    validador = a[-len(b):]
    
    if(b == validador): {
      print_final.append("encaixa")
    }
    else:{
      print_final.append("nao encaixa")
    }
    i+=1
for j in range(len(print_final)): {
    print(print_final[j])
}