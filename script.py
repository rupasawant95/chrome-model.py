#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: vinayak

"""

import sys

part=sys.argv[1]

if part=='a':
    import pandas as pd
    import numpy as np

    Train = pd.read_csv(sys.argv[2],header = None)
    Test = pd.read_csv(sys.argv[3], header = None)

    one = {}
    two = {}
    three = {}
    four = {}
    five = {}
    total={}

    Train.columns = ['rating', 'review']
    Test.columns = ['rating', 'review']

    len_train = len(Train.rating)
    len_test = len(Test.rating)

    X_Train = list(Train.review)
    Y_Train = list(Train.rating)

    X_Test = list(Test.review)

    def adddict(d , s):
        if s in d:
            d[s] = d[s]+1
        else:
            d[s] = 1
            
    prob = [0 for _ in range(5)]
            
    for i in range(0,len_train):
        a = int(Y_Train[i])
        prob[a-1] += 1
        if type(X_Train[i]) is str:
            b = X_Train[i].split()
            for s in b:
                adddict(total , s)
                if a == 1:
                    adddict(one , s)
                elif a == 2:
                    adddict(two , s)
                elif a == 3:
                    adddict(three , s)
                elif a == 4:
                    adddict(four , s)
                elif a == 5:
                    adddict(five , s)

    for i in range(0,5):
        prob[i] /= len_train
        
                    
    haha = []

            
    for i in range(0 , len_test):
        if type(X_Test[i]) is str:
            b = X_Test[i].split()
            
            p1 = np.log(prob[0])
            for s in b:
                if s in one:
                    p1 += np.log(one[s]/total[s])
                    
            p2 = np.log(prob[1])
            for s in b:
                if s in two:
                    p2 += np.log(two[s]/total[s])               
                
            p3 = np.log(prob[2])
            for s in b:
                if s in three:
                    p3 += np.log(three[s]/total[s])
                
            p4 = np.log(prob[3])
            for s in b:
                if s in four:
                    p4 += np.log(four[s]/total[s])
                    
            p5 = np.log(prob[4])
            for s in b:
                if s in five:
                    p5 += np.log(five[s]/total[s])
            
            ans = [p1,p2,p3,p4,p5]
            
            haha += [ans.index(max(ans))+1]

    with open(sys.argv[4], 'w') as f:
        for item in haha:
            f.write("%s\n" % item)

if part=='b':
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    @author: vinayak
    """
    import pandas as pd
    import numpy as np
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    from nltk.stem import PorterStemmer, WordNetLemmatizer
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

            
    def clean(string):
        string = string.replace("0", "")
        string = string.replace("1", "")
        string = string.replace("2", "")
        string = string.replace("3", "")
        string = string.replace("4", "")
        string = string.replace("5", "")
        string = string.replace("6", "")
        string = string.replace("7", "")
        string = string.replace("8", "")
        string = string.replace("9", "")
        string = string.replace("&", " ")
        string = string.replace("#", " ")
        string = string.replace("'", " ")
        string = string.replace(",", " ")
        string = string.replace("(", " ")
        string = string.replace(")", " ")
        string = string.replace("-", " ")
        string = string.replace("/", " ")
        string = string.replace(":", " ")
        string = string.replace(";", " ")
        string = string.replace("*", " ")
        string = string.replace("$", " ")
        string = string.replace("%", " ")
        string = string.replace(".", " ")
        string = string.replace('"', " ")
        string = string.replace('-', " ")
        string = string.replace('_', " ")
        string = string.replace('[', " ")
        string = string.replace(']', " ")
        string = string.replace('?', " ")
        string = string.replace('+', " ")
        string = string.replace('=', " ")
        string = string.replace('{', " ")
        string = string.replace('}', " ")      
        string = string.replace('  ', " ") 
        string = string.replace('   ', " ") 
        string = string.replace('   ', " ")
        return string


    Train = pd.read_csv(sys.argv[2],header = None)
    Test = pd.read_csv(sys.argv[3], header = None)

    one = {}
    two = {}
    three = {}
    four = {}
    five = {}
    total={}

    Train.columns = ['rating', 'review']
    Test.columns = ['rating', 'review']

    len_train = len(Train.rating)
    len_test = len(Test.rating)

    X_Train = list(Train.review)
    Y_Train = list(Train.rating)

    X_Test = list(Test.review)

    def adddict(d , s):
        if s in d:
            d[s] = d[s]+1
        else:
            d[s] = 1
            
    prob = [0 for _ in range(5)]
            
    for i in range(0,len_train):
        a = int(Y_Train[i])
        prob[a-1] += 1
        print(i)
        if type(X_Train[i]) is str:
            b = clean(X_Train[i])
            b = stemmer.stem(b)
            b = b.split()
            b = [item for item in b if item not in stop_words]
            for s in b:
                adddict(total , s)
                if a == 1:
                    adddict(one , s)
                elif a == 2:
                    adddict(two , s)
                elif a == 3:
                    adddict(three , s)
                elif a == 4:
                    adddict(four , s)
                elif a == 5:
                    adddict(five , s)

    for i in range(0,5):
        prob[i] /= len_train
        
                    
    haha = []

            
    for i in range(0 , len_test):
        if type(X_Test[i]) is str:
            b = X_Test[i].split()
            
            p1 = np.log(prob[0])
            for s in b:
                if s in one:
                    p1 += np.log(one[s]/total[s])
                    
            p2 = np.log(prob[1])
            for s in b:
                if s in two:
                    p2 += np.log(two[s]/total[s])               
                
            p3 = np.log(prob[2])
            for s in b:
                if s in three:
                    p3 += np.log(three[s]/total[s])
                
            p4 = np.log(prob[3])
            for s in b:
                if s in four:
                    p4 += np.log(four[s]/total[s])
                    
            p5 = np.log(prob[4])
            for s in b:
                if s in five:
                    p5 += np.log(five[s]/total[s])
            
            ans = [p1,p2,p3,p4,p5]
            
            haha += [ans.index(max(ans))+1]

    with open(sys.argv[4], 'w') as f:
        for item in haha:
            f.write("%s\n" % item)

if part=='c':
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    @author: vinayak
    """

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    @author: vinayak
    """
    import pandas as pd
    import numpy as np
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    from nltk.stem import PorterStemmer, WordNetLemmatizer
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

            
    def clean(string):
        string = string.replace("0", "")
        string = string.replace("1", "")
        string = string.replace("2", "")
        string = string.replace("3", "")
        string = string.replace("4", "")
        string = string.replace("5", "")
        string = string.replace("6", "")
        string = string.replace("7", "")
        string = string.replace("8", "")
        string = string.replace("9", "")
        string = string.replace("&", " ")
        string = string.replace("#", " ")
        string = string.replace("'", " ")
        string = string.replace(",", " ")
        string = string.replace("(", " ")
        string = string.replace(")", " ")
        string = string.replace("-", " ")
        string = string.replace("/", " ")
        string = string.replace(":", " ")
        string = string.replace(";", " ")
        string = string.replace("*", " ")
        string = string.replace("$", " ")
        string = string.replace("%", " ")
        string = string.replace(".", " ")
        string = string.replace('"', " ")
        string = string.replace('-', " ")
        string = string.replace('_', " ")
        string = string.replace('[', " ")
        string = string.replace(']', " ")
        string = string.replace('?', " ")
        string = string.replace('+', " ")
        string = string.replace('=', " ")
        string = string.replace('{', " ")
        string = string.replace('}', " ")      
        string = string.replace('  ', " ") 
        string = string.replace('   ', " ") 
        string = string.replace('   ', " ")
        return string


    Train = pd.read_csv(sys.argv[2],header = None)
    Test = pd.read_csv(sys.argv[3], header = None)

    one = {}
    two = {}
    three = {}
    four = {}
    five = {}
    total={}

    Train.columns = ['rating', 'review']
    Test.columns = ['rating', 'review']

    len_train = len(Train.rating)
    len_test = len(Test.rating)

    X_Train = list(Train.review)
    Y_Train = list(Train.rating)

    X_Test = list(Test.review)

    def adddict(d , s):
        if s in d:
            d[s] = d[s]+1
        else:
            d[s] = 1
            
    prob = [0 for _ in range(5)]
            
    for i in range(0,len_train):
        a = int(Y_Train[i])
        prob[a-1] += 1
        print(i)
        if type(X_Train[i]) is str:
            b = clean(X_Train[i])
            b = lemmatiser.lemmatize(b)
            b = stemmer.stem(b)
            b = list(nltk.bigrams(b.split()))
            b = [item for item in b if item not in stop_words]
            for s in b:
                adddict(total , s)
                if a == 1:
                    adddict(one , s)
                elif a == 2:
                    adddict(two , s)
                elif a == 3:
                    adddict(three , s)
                elif a == 4:
                    adddict(four , s)
                elif a == 5:
                    adddict(five , s)

    for i in range(0,5):
        prob[i] /= len_train
        
                    
    haha = []

            
    for i in range(0 , len_test):
        if type(X_Test[i]) is str:
            b = X_Test[i].split()
            
            p1 = np.log(prob[0])
            for s in b:
                if s in one:
                    p1 += np.log(one[s]/total[s])
                    
            p2 = np.log(prob[1])
            for s in b:
                if s in two:
                    p2 += np.log(two[s]/total[s])               
                
            p3 = np.log(prob[2])
            for s in b:
                if s in three:
                    p3 += np.log(three[s]/total[s])
                
            p4 = np.log(prob[3])
            for s in b:
                if s in four:
                    p4 += np.log(four[s]/total[s])
                    
            p5 = np.log(prob[4])
            for s in b:
                if s in five:
                    p5 += np.log(five[s]/total[s])
            
            ans = [p1,p2,p3,p4,p5]
            
            haha += [ans.index(max(ans))+1]

    with open(sys.argv[4], 'w') as f:
        for item in haha:
            f.write("%s\n" % item)





