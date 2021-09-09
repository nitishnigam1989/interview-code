def fetch(data,v):
    for key,value in data.items():
        if v==key:
         print (str(key)+' is -> '+str(value))
        elif isinstance(value,dict):
            fetch(value,v)
        elif isinstance(value,str):
            print(value)
        elif isinstance(value, list):
            for val in value:
                if isinstance(val, str):
                    pass
                elif isinstance(val, list):
                    pass
                else:
                    fetch(val,v)




if __name__ == "__main__":
    user_input1={"a":{"b":{"c":"d"}}}
    user_input2={"x":{"y":{"z":"a"}}}
    fetch(user_input1,"a")
    fetch(user_input2,"z")