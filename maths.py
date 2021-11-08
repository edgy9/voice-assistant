def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    print(str1)
    return str1 

def filtermaths(s):
    search = s
    searchitem =[s]
    notsearchwords= ['what','is','Jarvis',"what's"'jarvis','jervis','Jervis',"'s"] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    #print(search)
    return search

def multiply(voice_data):
    s = voice_data
    st = filtermaths(s)
    st = listToString(st)
    #print(st)
    if "hat's" in st:
        st.split()
        v, arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 * arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')
    else:
        st.split()
        arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 * arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')

def divide(voice_data):
    s = voice_data
    st = filtermaths(s)
    st = listToString(st)
    #print(st)
    if "hat's" in st:
        st.split()
        v, arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 / arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')
    else:
        st.split()
        arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 / arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')


def addition(voice_data):
    s = voice_data
    st = filtermaths(s)
    st = listToString(st)
    #print(st)
    if "hat's" in st:
        st.split()
        v, arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 + arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')
    else:
        st.split()
        arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 + arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')

def subtraction(voice_data):
    s = voice_data
    st = filtermaths(s)
    st = listToString(st)
    #print(st)
    if "hat's" in st:
        st.split()
        v, arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 - arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')
    else:
        st.split()
        arg1, op, arg2 = st.split()
        if arg1.isnumeric() and arg2.isnumeric():
            arg1 = float(arg1)
            arg2 = float(arg2)
            answer = arg1 - arg2
            answer = str(answer)
            if '.0' in answer:
                answer = answer[:-2]
                print(answer)
                return(answer)
            else:
                print(answer)
                return(answer)
        else:
            print('invalid number')
            return('invalid number')
