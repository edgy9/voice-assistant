import webbrowser

def filtersearch(s):
    search = s
    searchitem =[s]
    notsearchwords= ['search','for','Jarvis','look','up','jarvis','jervis','Jervis'] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    
    return search

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    print(str1)
    return str1 


def search(voice_data):
    #search = record_audio('What do you want to search for?')
    s = voice_data
    filtersearch(s)
    st = filtersearch(s)
    st = listToString(st)
    #print(st)
    url = 'https://google.com/search?q=' + st
    webbrowser.get().open(url)
    return('here is what i found for ' + st)

