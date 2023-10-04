domain = input("Введите адрес сайта: ") 

while True:
    last_dot_index = domain.rfind('.')  
    if last_dot_index == -1:  
        break
    subdomain = domain[last_dot_index + 1:]  
    print(subdomain) 
    domain = domain[:last_dot_index]  

print(domain)  