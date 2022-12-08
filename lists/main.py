def main():
    mode="none"
    list = []


    def dele(content):
        if (content in list):
            list.remove(content)
        else:
            print("This is not in the list")

        
    def add(content):
        if (content not in list):
            list.append(content)
        else:
            print("This is already in the list")      
        
        
    while True:
        mode=input("do you want to add/delete/end? ")

        if mode=="add":          
            add(input())
            
        elif mode=="delete":
            dele(input())

        elif mode=="end":
            break
        else:
            print("invalid input")
        print(list)
        
  
main()