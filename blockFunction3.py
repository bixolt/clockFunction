import re
#The idea instead of the copy and paste , if we actually all the time look for take part of block small blick that can turn on everytime in the block with dinamic function 
# we can do it with cratidge (מכסנית) of this pasts without spacail things i.e without arbument or somethings like this just the mini block in default and we can decide
# in every block which argument and where we wanna to paste this spesific mini block with the sepesific function all the time . 
#We check how the client wrotes the request paste step by step .
#So after it we don't need to change the "requestPaste" because we will do the same just instead of to paste from other block ,what not really allow because i we think about
#if we copy from other block we take it with the argument func and that doesn't allow us to work with something clear and append and design which and what we want in the paste
# mini block . 
#So for summery , we will create for the paste-block several things first we atually creat a aprroximately str-list and insert it to spacial place in every block (probebly)
# after we can design and add everything like arguments-function and after the block that we want is prepared we can insert it to our "real" block according the function 
# argument and the name of this mini-block <- this place for mini block will be probebly dictionary and we will insert the mini-block to current place with automaticly 
# but if we want the client can write the name of the block that he want to take this block and paste like this : <--{(B1(optional),blockMiniName),function1(Fargument1="bla1",
# Fargument2="bla2"),function2(...))}-->
#the regular expression will be somthings like -> 
#We also can ceate more understandaable according checking stages and if have any error we can responed about exctly which part need to fix . 
# for example we can say if don't have at least if we don't have a name block and if have so need to three (,) in the <-- -->  
# the regulary of the can be somethings reauestSearcher1=compiler(r'(?=.*,+)') if have a name copiler(r'^(?=.*,{3})/(([A-Z]{1}/d+)/)')
#Or to do somthings like this with the search compile=r'/(()/)
#In order to get into to evrypart of the request any request that we will talk and mark in order to understand every error and create a handler(טיפול) and answer 
#for example of this condition is when we check the "request-paste" we actually in this case "increase the ->"regular-expression" " and every time in other proporation
#for example we got "true" about the beginning question if exist name-block and name-mini-block for example So we will filled it in a form in order to provide correct 
# react of this "checking" but no just it we actually "build" the next pattern with this answer may it error and stop to reseach this request or build somthing like this
#patternPasteAll.match(f'{previousPatternCurrent}patternfunction1')<-for example exist argument or not with patternFunction2 for example and so write result in the form and...
#Let's try to build this system for paste system (notice: this is the way for rescue the things from the request and i'll explain about it abtually when we check things that 
#nessessory for our request we actually can rescue the current material that defined our request and becuase of this we can actually do findall or somthing like this , and 
#retrive the things in one list from there we can anlyze everythings).
#For summery : we tow things to do everytime we actually want to create a respone for any request(we called request to mark thst we need to do function in order to insert it) .
#First test it by increasing the pattern that suit to this request every time and response Data about every test and increasing in form ->"response" for example with name without 
#or error and we response in the code and give to the client (2) tow stage is actually create find all about this request and join the pattern that we found true of this reuqest 
#If we think about, this can be suit to every request just with cheking and rescue different things .
#For first filter
#in order to make regular expression denamic and every time we will insert the previous regular to the next we will put the regular every regular in "str" in variables and evry
#time we will insert the durrent part like : combineNewPattern=re.compile(r'previousPatternCurrentVariable+newPattern1')
#From there we than do the same with match : match=re.match(combineNewPattern,requestPaste) and -> if(match)... 
#We will use in range loop and lists every variable that consider pattern have category and we insert them one then one with range to our compile and so what suit stay in the
#compile as current variable .
#Some example of lists patterns : 
function_patterns = [
    r'\bdef\s+\w+\s*\([^)]*\):',  # Python function definition
    r'\bfunction\s+\w+\s*\([^)]*\)\s*{',  # JavaScript function definition
    r'\bfunc\s+\w+\s*\([^)]*\)\s*{',  # Go function definition
    r'\b[A-Za-z_]\w*\s*\([^)]*\)\s*(?:->\s*[A-Za-z_]\w*)?\s*{',  # Swift function definition
    r'\b[A-Za-z_]\w*\s*\([^)]*\)\s*(?:const\s*->\s*[A-Za-z_]\w*)?',  # C++ function definition
]

# Patterns for validating IDs
id_patterns = [
    r'\bID\d{3,}\b',  # Simple numeric ID starting with 'ID' and followed by at least three digits
    r'\b[A-Za-z]{2,5}\d{2,5}\b',  # Alphanumeric ID with 2-5 letters followed by 2-5 digits
    r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b',  # UUID
]

# Patterns for validating passwords
password_patterns = [
    r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',  # At least 8 characters, one letter, and one number
    r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',  # At least 8 characters, one letter, one number, and one special character
    r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$',  # At least 12 characters, one letter, one number, and one special character
]

# Patterns for validating email addresses
email_patterns = [
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',  # General email format
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$',  # General email format with domain length 2-4
]

# Patterns for validating dates
date_patterns = [
    r'^\d{4}-\d{2}-\d{2}$',  # Date in YYYY-MM-DD format
    r'^\d{2}/\d{2}/\d{4}$',  # Date in MM/DD/YYYY format
    r'^\d{2}-\d{2}-\d{4}$',  # Date in DD-MM-YYYY format
    r'^\d{4}/\d{2}/\d{2}$',  # Date in YYYY/MM/DD format
]

# Patterns for validating URLs
url_patterns = [
    r'^(https?|ftp)://[^\s/$.?#].[^\s]*$',  # General URL pattern
    r'^(https?|ftp)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(/[\w.-]*)*$',  # URL with domain and optional path
    r'^(https?|ftp)://(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(/[\w.-]*)*$',  # URL with optional www
]

# Patterns for validating IP addresses
ip_patterns = [
    r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',  # IPv4
    r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:)$',  # IPv6
]

# Patterns for validating credit card numbers
credit_card_patterns = [
    r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$',  # Simple 16-digit credit card number with optional hyphens
    r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$',  # 16-digit credit card number with spaces
    r'^\d{4}-\d{6}-\d{5}$',  # American Express card format
]

# Patterns for validating Social Security Numbers (SSNs)
ssn_patterns = [
    r'^\d{3}-\d{2}-\d{4}$',  # SSN in the format XXX-XX-XXXX
]

# Patterns for validating file paths
file_path_patterns = [
    r'^[a-zA-Z]:\\[\\S|*\S]?.*$',  # Windows file path
    r'^\/[^\0]*$',  # Unix/Linux file path
]

# Patterns for validating HTML tags
html_tag_patterns = [
    r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>(.*?)</\1>',  # General HTML tag with content
    r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*\/?>',  # Self-closing HTML tag
]
suits=0
patternPasteSpesific=''
responseFormPaste={}
blocks=['{A1 This is str block1 that contain marks function and more...}','{B1 This is str block2 that contain marks function and more...}',
'{C1 This is str block3 that contain marks function and more...}']
#We C1 and more of these are the id-block everytime when we create block our system should create for the client these id-block and rise when abc is over and do like this
#C2 ... 
#The idea of every block , is that every block need to get "personally-data" we actually every time that we discover mark of function and the name of block isn't there
#we actually insert the request and the responed and every things that we see here to the data(dictionary) of the block that write this mark . 
#due to we will can to turn on the function after we check the request and the parts of just to access the data of every block and turn loops and just turn the function 
#according the requerments of the client and about the current block in the spesific place .
#We will know which block is in the aim of the client do the spesific function in this way :
# when we check the spesific function in some kind of block we will direct search any name of function in the request of the function if nothing (most of the time for example
# in requestPaste ). So when we have the spesific name of our function we insert and every result and things in the data , that not really hard because everything will be short
# with loops and because that happen evretytime the in the same way we can fund really shortly whay to do it . According to this knowledge this will bring us the information 
# to active the functions-marks.   
requestsPastesListSpesific=[]
objectOfPaste=''
patternListChackingPaste=[function_patterns,id_patterns]
patternPasteGnerally=re.compile(r'<--/{(?.*)/}-->')
for block in blocks:
  nameBlock=''
  for char in block[1:]:
     if char==" ":
        break
     nameBlock+=char
  requestsPastesListGenerally=re.findall(patternPasteGnerally,block)
  for reqauestPaste in requestsPastesListGenerally:
     patternCombinedPaste='' 
     while(suits>2):
       for i in range(len(patternListChackingPaste[suits])):
           lengthOf=len(patternListChackingPaste[suits][i])
           patternCombinedPaste+=patternListChackingPaste[suits][i]
           compileTest=re.compile(patternCombinedPaste)
           if(suits>1):
               search=re.match(compileTest,reqauestPaste)
           else:
             search=re.search(compileTest,reqauestPaste)
             if(search):
                 responseFormPaste[reqauestPaste]=f"""Response:
                  Match: requestPaste ({reqauestPaste}) in {globals()[patternListChackingPaste[suits]]}"""
                 suits+=1
                 break
             elif(i==lengthOf-1 and not search):
                responseFormPaste[reqauestPaste]=f""" Response:
                RequestFall: reqauestPaste ({reqauestPaste}) in {globals()[patternListChackingPaste[suits]]}"""
                patternCombinedPaste=patternCombinedPaste[:-lengthOf]
                suits+=1
                break 
             else:
                responseFormPaste[reqauestPaste]=f""" Response:
                Invalid: reqauestPaste ({reqauestPaste}) in {globals()[patternListChackingPaste[suits]]}"""
                patternCombinedPaste=patternCombinedPaste[:-lengthOf]
     disassemblyRequestPaste=re.findall(patternCombinedPaste,reqauestPaste)
     requestsPastesListSpesific.append(patternCombinedPaste)
#So now we need to retrieve the things that we was find according to the 