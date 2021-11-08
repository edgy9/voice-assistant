voice_data  = "search for cheese jarvis"


def listToString(s1): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s1: 
        str1 += ele  
    
    # return string  
    return str1 


def sfilter(s):
    search = s
    searchitem =['search for cheese jarvis']
    notsearchwords= ['search','for','jarvis'] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    
    return search
    


s = voice_data
sfilter(s)
st = sfilter(s)
st = listToString(st)
print(st)