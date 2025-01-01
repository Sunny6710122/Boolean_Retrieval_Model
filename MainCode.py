import nltk
import string
from nltk.stem import PorterStemmer
ps = PorterStemmer()
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


def ListFetch(termm,Inv_index,filename):#this function will need terms and find you in which documents it is occurred
    listt1 = []
    if(termm in Inv_index):
        for m in filename:
            if(m in Inv_index[termm]):
                listt1.append(m)
    return listt1

def ProximatyIntersection(list1,term11,term22,Inv_index,k): #ProximatyIntersection function is comparing the combinations of positional index of two terms in one documents 
    m = 0
    term1 = []
    term2 = []
    resultt = []
    flag11 = False
    k1 = int(k)
    while m < len(list1):
        term1 = Inv_index[term11][list1[m]]
        term2 = Inv_index[term22][list1[m]]
        
        t1 = 0
        t2 = 0
        while t1<len(term1):
            while t2<len(term2):
                if(term1[t1]>term2[t2]):
                    if(term1[t1]-term2[t2]<=k1):
                        resultt.append(list1[m])
                        flag11 = True
                        break
                if(term1[t1]<term2[t2]):
                    if(term2[t2]-term1[t1]<=k1):
                        resultt.append(list1[m])
                        flag11 = True
                        break
                t2 = t2+1
            if(flag11 == True):
                flag11 = False
                break
            t1 = t1+1
        m = m +1
    return resultt

def Intersection(list1,list2): # sinmple intersection between two list
    l1 = 0
    l2 = 0
    list4 = []
    while l1 < len(list1) and l2 < len(list2):
        if(l1 == len(list1) or l2==len(list2)):
            break
        if(list1[l1]<list2[l2]):
            l1 = l1 + 1
        if(l1 == len(list1) or l2==len(list2)):
            break
        if(list1[l1]>list2[l2]):
            l2 = l2 + 1
        if(l1 == len(list1) or l2==len(list2)):
            break
        if(list1[l1]==list2[l2]):
            list4.append(list1[l1])
            l1 = l1 + 1
            l2 = l2 + 1
        if(l1 >= len(list1) or l2>=len(list2)):
            break
    return list4


def subtraction(list1,list2): # this function will perform as NOT operstion Do . 
    ll1 = 0
    ll2 = 0
    list3 = []
    while(ll2 < len(list2)):
        if(list1[ll1]==list2[ll2]):
            ll1 = ll1 + 1
            ll2 = ll2 + 1
        if(ll1 == len(list1) or ll2==len(list2)):
            break
        if(not(list1[ll1]==list2[ll2])):
            list3.append(list2[ll2])
            ll2 = ll2 + 1
    return list3


def Union(list11,list22): # union two list and as OR operation do
    l1 = 0
    l2 = 0
    list4 = []
    while l1 < len(list11) and l2 < len(list22):# will run until one samllest list length
        if(l1 == len(list11) or l2==len(list22)):
            break
        if(list11[l1]<list22[l2]):
            list4.append(list11[l1])
            l1 = l1 + 1
        if(l1 == len(list11) or l2==len(list22)):
            break
        if(list11[l1]>list22[l2]):
            list4.append(list22[l2])
            l2 = l2 + 1
        if(l1 == len(list11) or l2==len(list22)):
            break
        if(list11[l1]==list22[l2]):
            list4.append(list11[l1])
            l1 = l1 + 1
            l2 = l2 + 1
        if(l1 == len(list11) or l2==len(list22)):
            break
    # remaining elements in any list will appended by these two conditions in both list
    if(not(l1==len(list11))):
        while(l1<len(list11)):
            list4.append(list11[l1])
            l1 = l1 + 1
    if(not(l2==len(list22))):
        while(l2<len(list22)):
            list4.append(list22[l2])
            l2 = l2 + 1
    return list4

#fetching the stop words in Stopwords list 
f1 = open("Stopword-List.txt","r")
Stopword = f1.read()
# print(Stopword)
Stopwords = []
stop = ""
for k in range(len(Stopword)):
    if(Stopword[k]==" "):
        continue
    if(Stopword[k]=="\n"):
        Stopwords.append(stop)
        stop = ""
        continue
    stop += Stopword[k]

R_document1 = []
Inverted_Index = {
}




filenames = [1,2,3,7,8,9,11,12,13,14,15,16,17,18,21,22,23,24,25,26]


for k in filenames:
    f = open("{}.txt".format(k), "r")  #as k will be increasing the all docunments will be read one by one
    document1 = f.read()
    strr = ""
    curr = [k]
    curr1 = k
    count = 1
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag6 = False

    i = -1
    while i < len(document1):#iterating through single character
        i = i+1
        if(i==len(document1)):# if counter is equal to len of douments then break and read next docunment
            break
        if(document1[i]=='('):# if ( will occure then flag3 will true and 
            flag3 = True
            continue
        if(document1[i]==')' and flag4==True):#when closed then flag4 will be true and the word's will be appended into inverted index
            if(document1[i+1]==" " or document1[i+1]=="." or document1[i+1]==","):
                i = i+1
                continue
        if(document1[i]=='-' or (document1[i-1]=='-' and document1[i]=='\n')):# this condition will concanite the - words 
            continue
        if(document1[i]=='\n'): # when next line occur then append words by checking condition
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = False
            flag5 = False
            flag6 = False
            if(strr.lower() in Stopwords):
                strr = ""
                count = count + 1
                continue
            if(len(strr)<=1):
                str = ""
                count = count + 1
                continue
            if(ps.stem(strr.lower()) in Inverted_Index):
                if(k not in Inverted_Index[ps.stem(strr.lower())]):
                    Inverted_Index[ps.stem(strr.lower())][k] = [count]
                else:
                    Inverted_Index[ps.stem(strr.lower())][k].append(count)
                count = count + 1
                strr = ""
                continue
            Inverted_Index[ps.stem(strr.lower())] = {k:[count]}
            count = count + 1
            strr = ""
            continue
        if(document1[i]==" " or document1[i]=="." or document1[i]==","):# when space occur then append words by checking condition
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = False
            flag5 = False
            flag6 = False
            if(strr.lower() in Stopwords):
                strr = ""
                count = count + 1
                continue
            if(len(strr)==1 or strr==""):
                strr = ""
                count = count + 1
                continue
            if(ps.stem(strr.lower()) in Inverted_Index):
                if(k not in Inverted_Index[ps.stem(strr.lower())]):
                    Inverted_Index[ps.stem(strr.lower())][k] = [count]
                else:
                    Inverted_Index[ps.stem(strr.lower())][k].append(count)
                count = count + 1
                strr = ""
                continue
            Inverted_Index[ps.stem(strr.lower())] = {k:[count]}
            count = count + 1
            strr = ""
            continue
        if(not((document1[i]>="A" and document1[i]<="Z") or (document1[i]>="a" and document1[i]<="z"))): #if its an other character so skip
            if(flag2==True):  # it will check now the other character are on the both sides of words then ignore it 
                while document1[i]!=" ":
                    i = i+1
                    if(i==len(document1)):
                        break
                strr = ""
                flag1 = False
                flag2 = False
                # i = i+1
                continue
            flag1 = True  # it will true when an other character will be occured
            if(flag5==True):
                flag6 = True
            continue
        if(((document1[i]>="A" and document1[i]<="Z") or (document1[i]>="a" and document1[i]<="z")) and flag1==True):
            flag2 = True  # it will true when and a-z character will be occured after any other character
        if(((document1[i]>="A" and document1[i]<="Z") or (document1[i]>="a" and document1[i]<="z"))):
            if(flag3==True):
                flag4 = True # for brackets
            flag5 = True
            if(flag6==True):  
                while document1[i]!=" ":
                    i = i+1
                    if(i==len(document1)):
                        break
                strr = ""
                flag5 = False
                flag6 = False
                # i = i+1
                continue

        strr+=document1[i]
# Processing = []

def Proximity_Queryy(str1):  
    terms = []
    resulttt = []
    Qitemss = []
    # str1 = input("'X Y /k': ")
    terms = str1.split(" /") 
    Qitemss = terms[0].split()
    interseclist = []
    d = 0
    terms1 = Qitemss[0]
    while d < len(Qitemss):  # will iterate two terms 
        e = 0
        listt1 = []
        if(ps.stem(Qitemss[d].lower()) in Inverted_Index):  #checking the terms are in inverted index 
            while e < len(filenames):
                if(filenames[e] in Inverted_Index[ps.stem(Qitemss[d].lower())]):
                    listt1.append(filenames[e])
                e = e+1
            interseclist.append(listt1)  #if occured then get list of documents in which it occure
        d = d+1
    intersect = Intersection(interseclist[0],interseclist[1]) # intersect both list
    resulttt = ProximatyIntersection(intersect,ps.stem(Qitemss[0].lower()),ps.stem(Qitemss[1].lower()),Inverted_Index,terms[1]) # send intersect list for find the distance and comparing it is in range
    # print(resulttt)

    return resulttt




def Simple_queryy(str1):
    Qitems = []
    Qitems = str1.split()

    Processing = []
    QitemsFlag = []
    QitemsFlag1 = []
    Operations = []
    list1 = []
    list2 = []

    QTermsList = []
    l = 0
    for a in Qitems:
        QitemsFlag.append(False)
        QitemsFlag1.append(False)
        if(not(a=="AND" or a=="OR" or a=="NOT")):
            Processing.append(ps.stem(a.lower()))
            continue
        Operations.append(a)
    if(len(Operations)==0 and len(Processing)==0):
        return ['Write something']
    b = 0
    countt = 0
    counttt = 0
    while b < len(Qitems):
        if(Qitems[b]=="AND" and QitemsFlag1[b]==False):
            if(Qitems[b+1]=="NOT"):
                QitemsFlag1[b+1]==True
            QitemsFlag1[b]==True
            counttt = counttt + 2
        elif(Qitems[b]=="OR" and QitemsFlag1[b]==False):
            if(Qitems[b+1]=="NOT"):
                QitemsFlag1[b+1]==True
            QitemsFlag1[b]==True
            counttt = counttt + 2
        elif(Qitems[b]=="NOT" and QitemsFlag1[b]==False):
            counttt = counttt + 1
            QitemsFlag1[b]==True
        b = b + 1
    rang = 1
    result = []
    QitemCount = 0
    j = 0
    while QitemCount < len(Qitems): #iterate the all terms of input query
        if(Qitems[QitemCount]=="AND" and QitemsFlag[QitemCount]==False):  #if AND occur then perform AND operation through intersection
            if(countt==0):
                rang = 2
            else:
                rang = 1
            result = []
            for j in range(rang):
                listt = []
                if(l==len(Processing)):
                    break
                if(Processing[l] in Inverted_Index):
                        for m in filenames:
                            if(m in Inverted_Index[Processing[l]]):
                                listt.append(m)
                QTermsList.append(listt)
                l = l+1
            if(Qitems[QitemCount+1]=="NOT"):  # if Not Occur after direct AND then perform first NOT operation
                list33 = QTermsList[countt+1]
                result = subtraction(list33,filenames)
                QTermsList[countt+1] = subtraction(list33,filenames)
                QitemsFlag[QitemCount+1] = True
            if(countt==counttt-1):
                break
            result = []
            result = Intersection(QTermsList[countt],QTermsList[countt+1])
            QTermsList.append(result)
            QitemsFlag[QitemCount] = True
            countt = countt + 2

        elif(Qitems[QitemCount]=="NOT" and QitemsFlag[QitemCount]==False):  # perform NOT through SUbtraction 
            result = []
            for j in range(1):
                if(l==len(Processing)):
                    break
                listt = []
                if(Processing[l] in Inverted_Index):
                        for m in filenames:
                            if(m in Inverted_Index[Processing[l]]):
                                listt.append(m)
                QTermsList.append(listt)
                l = l+1
            result = subtraction(QTermsList[countt],filenames)
            countt = countt + 1
            QTermsList.append(result)
            QitemsFlag[j] = True

        elif(Qitems[QitemCount]=="OR" and QitemsFlag[QitemCount]==False):  #perform OR operation through UNOIn function
            result = []
            if(countt==0):
                rang = 2
            else:
                rang = 1
            for j in range(rang):
                if(l==len(Processing)):
                    break
                listt = []
                if(Processing[l] in Inverted_Index):
                        for m in filenames:
                            if(m in Inverted_Index[Processing[l]]):
                                listt.append(m)
                QTermsList.append(listt)
                l = l+1
            if(Qitems[QitemCount+1]=="NOT"):# if Not Occur after direct OR then perform first NOT operation
                result = subtraction(QTermsList[countt+1],filenames)
                QTermsList[countt+1] = result
                QitemsFlag[QitemCount+1] = True
            result = []
            if(countt==counttt-1):
                break
            list11 = QTermsList[countt]
            list22 = QTermsList[countt+1]
            result = Union(list11,list22)
            countt = countt + 2
            QTermsList.append(result)
            QitemsFlag[QitemCount] = True
            # continue
        else:
            QitemsFlag[QitemCount] = True
            # continue
        QitemCount = QitemCount + 1
    
    if(len(Operations)==0):
        if(not(len(Processing)==0)):
            return ListFetch(Qitems[0],Inverted_Index,filenames)
        
    return QTermsList[len(QTermsList)-1]


    # print(QTermsList[len(QTermsList)-1])

# checkQ = input("1 For Simple Query AND any letter For Proximty Query: ")
# if(not(checkQ=="1")):
    
# else:

# from your_script_file_name import Simple_queryy, Proximity_Queryy

def perform_simple_query():
    query = simple_query_entry.get()
    results = Simple_queryy(query)
    display_results(results)

def perform_proximity_query():
    query = proximity_query_entry.get()
    results = Proximity_Queryy(query)
    display_results(results)

def display_results(results):
    result_text.delete(1.0, tk.END)
    if results:
        for result in results:
            result_text.insert(tk.END, f"{result}\n")
    else:
        result_text.insert(tk.END, "No results found.")

# Create main window
root = tk.Tk()
root.title("Information Retrieval System")

# Create input fields and buttons
simple_query_label = tk.Label(root, text="Simple Query:")
simple_query_label.grid(row=0, column=0, padx=5, pady=5)

simple_query_entry = tk.Entry(root, width=50)
simple_query_entry.grid(row=0, column=1, padx=5, pady=5)

simple_query_button = tk.Button(root, text="Search", command=perform_simple_query)
simple_query_button.grid(row=0, column=2, padx=5, pady=5)

proximity_query_label = tk.Label(root, text="Proximity Query:")
proximity_query_label.grid(row=1, column=0, padx=5, pady=5)

proximity_query_entry = tk.Entry(root, width=50)
proximity_query_entry.grid(row=1, column=1, padx=5, pady=5)

proximity_query_button = tk.Button(root, text="Search", command=perform_proximity_query)
proximity_query_button.grid(row=1, column=2, padx=5, pady=5)

# Create text area to display results
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.grid(row=2, columnspan=3, padx=5, pady=5)

# Run the main event loop
root.mainloop()
