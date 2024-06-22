#For summery of what we did in generaly at the data,apcacialPattern,dinamic and static data,stages of beginning run until the end (aprowimately without perform just big 
# explanation) in reasechh 4 for our app we check all the possible way to inset data in dinamic/static way and understand the different actually figure out from stage 3
#what need to get change and where the subdata should to be  and we arrived to this structure {category:{BigName:{exatlyName:[data]}}} because the category in general
#are the same for every type of data and the function block or every guy that we wanna to get data about is get different every time and because of this we insert the 
#data like this after is to create dinamic data like form we get this data just we run the loops or get every result that we need in the three stage (perform) that combined
#three of things one is the response request... every data that we sum from the loops and read the blocks (in order to get this data we will use in the data itself 
# for example with the pattern to recognize the exactly request that happened with marks at the block and after for example pull out the name of the function that we reaveled)
# Ok so after we have the data from the block and more... in the form we actually in the stage 3 in this stage we will perform this things on the block with the data the form
# and with the block of course in shortly word modify the block and insert back . So now the blocks place according the "mini-block"<-
# default using blocks that we can chenge how we want put function argument and more and after paste in real-block and every real-block should to get this list of mini-function
#and passibility to modify them and in the mark paste we can decide from which of real-block we want to pull out the spesific mini-block and using in arguments and function 
# that we want and this get decide in the paste) <- in very shortly from 2 3 search about mini block and paste. 
# and may more things that we will add , we must to plan the place of blocks , like the data structure in general so actually we have property that the same for block 
#and just we insert idfferent data every time for different block (we have name of the real-block according the A1,B1,C1... and have the name of the mini-block with
#a1,b1,c1...)  we will build this this place exactly the same of every static data and because of this we actually will build this place at the containing-object blocks
#at the function createStatic <- because of this we will change the name of this function to createStaticAndBlocks 
# we will the structuer we will use in order to filled the thing is it : [[[data],[the same category just different block get the data]],[other type of data ]]
#or passible to put something like this direct in the function -> {typeData:{block:[]}}<- notice that the hendler of this building should to be slightly different 
#here we don't have "exactly-block" like every data that have the name of the data like function and the exact like functionName1.
#The resulting of the process is basically block that untill at str and that mean every function that in the system should to turn on just in the block and just in the end
#of the process when we have the now list with new block according the requerments we can modify or eval it what mean also for the next stages of development we will may
# develop system security of every block that we seccess to create (that mean every requerments in the block don't failed) have every mark of security block to user defending
# if the user will turn on eval or something else that can risk the system . 

# let's build what we did already : 
import re
def createStaticsAndBlocks(data=[[[['data']]],[['dataBlock']]],patternDefaultDatas=
    {'patternData':{"property":{"dataName":{'sepesificThings':[]}}},'patternDefaultBlock':{'property':{'blockName':[]}}}):
    for patternDefaultData,subData in zip(patternDefaultDatas,data):
        for property,propertyList in zip(patternDefaultData,subData):
            for dataNames,dataNamesList in zip(property,propertyList):
                if patternDefaultData=='patternDefaultBlock':
                    if not patternDefaultDatas[patternDefaultData][dataNames]:
                        patternDefaultDatas[patternDefaultData][dataNames]=[]
                    patternDefaultDatas[patternDefaultData][dataNames].append(dataNamesList)
                    break
                for sepesificThings,sepesificThingsList in zip(dataNames,dataNamesList):
                    if not patternDefaultDatas[patternDefaultData][property][dataNames][sepesificThings]:
                        patternDefaultDatas[patternDefaultData][property][dataNames][sepesificThings]=[]
                    patternDefaultDatas[patternDefaultData][property][dataNames][sepesificThings].append(sepesificThingsList)
    patternDefaultDatasFilled=patternDefaultDatas
    return patternDefaultDatasFilled
def createForm(patternDefaultDatasFilled):
    form={'status':{},'response':{'error':{'request':{},'runing':{}}},'requests':{'precisely':{}},'name':{}}
    #The meaning of "createForm" is actually create function that analyze the block from this data 'patternDefaultBlock':{'property':{'blockName':['data']}}'
    # i.e for beginning we will do loops about the patternDefaultDatasFilled['blockItself'] and analyze the data from every time according the 'patternData' according what 
    #we said we will fined the marks for any function that we need to turn on due to according the pattern . Notice in this case we will don't read and create and make 
    #thing for the request and for the things that we reaveled in the block ,we just create the intentions check the request or every spacial things in the blocks 
    #and bring to the form in exactly place for exactly thing
    # "dinamic-data" becaus the "user" that use in this app can design and build according the input more precisely according the things that he write in the blocks that
    # he want to change . in shortly this "form" actually say what we want exactly in the real-block and say every thing we want to change in our data .
    #The stages of this function -> first we will discover every general mark like the version 3 with the pattern in the requestsListGenerally in the patternData 
    #for each one of the block that and after this searching we check the request i.e the fixed of the mark that we found after we make the spesific pattern
    #we findall and insert the organs in the list that soport this request for this spesific issue in shortly in this way we insert the data in exactly place for currently block
    #in the form this just adding we also add soport of every checking or process that we do in this function to the form
    #that mean after we write a code for this function 'createForm' we must to make function -> "performForm" in order to perform all the things wanted things according the 
    # details we pick form the "createform" function .  
    additionaForm={'error':['request','runing'],'requests':['name',{'mark':[{'block':[]}]},'details',{'internal-request':['private-request-details']}]}
    def additionFormFunction(form,additionaForm):
        for typeOf,subDatas in additionaForm.items():
            if not form[typeOf] in form:
                  form[typeOf]={}
        def insertInteranlData(subDatas,current_data=form[typeOf]):
            if isinstance(subDatas,list):
              for subData in subDatas:
                 if not(isinstance(subData,dict)):
                    if not current_data[subData] in current_data:
                     current_data[subDatas]={}
                 else:
                     for key,value in zip(subData):
                        if isinstance(value,list):
                            if not key in current_data:
                              current_data[key]={}
                        else:
                            insertInteranlData(current_data[key],subData)
                             
            else:
              print('Insert new type of data in your form failed due to : incorrect placement.')
        insertInteranlData(subDatas)
    additionFormFunction(form,additionaForm)
    #In order to make to do this procces that will make all the sub data in the from and after to insert the fundamental data like id block where we need 
    #we can in this case to do recursive when this statment happen isinstance(form[typeOf],dict) and create a list that will contain all the "key" we check and return any dict
    #and after we will just call to the function that create the empty data in spesific place like this :
    #But the problem with just put this function that we may more things in the same condition that mean may in this proccess form[key[i]]={} we delete thing in 
    #the second we need to put second loop in order to get the value of and the key .
    #In shortly we need to find way to call the function that turn on again the searching on the element issue and contain all of the keys that we have from this and 
    #sparete the keys we need to active for every organ it self and to care about and so to put in . work with additionalForm and the form in the same time and in the runing 
    #i.e to care about one thing in the additionalForm function and to add or do something in the Form in the same time that we decide for other fucntion or things .
    #if we insert all the data in createSpesific we can catch it . 
    dictNamesIssue={}
    def addFormFundamental(form,DataNames):
        dictNames={}
        for issueNames,listNames in DataNames.items():
            for issueName,listName in zip(issueNames,listNames):
                dictNames[listName]={}
            dictNamesIssue[issueName]=dictNames
            dictNames={}
        def insertIdDataForm(form):
            for category in form:
                if isinstance(category,dict):
                  if category=={}:
                      for dictNameIssue,content in dictNamesIssue.items():
                          category[dictNameIssue]=content
                  else:
                      insertIdDataForm(category)
                else:
                    print('Failed to insert the fundamental data , your form incorrect')
        insertIdDataForm(form)
    addFormFundamental(form,patternDefaultDatasFilled['patternData']['names'])
        #The names in patternData is dictonary that contain all the id name of every items for example form,patternDefaultDatasFilled['patternData']['names']['blocks]
        #all the id block A1,B1,C1... and we want to insert all of these to all category in form
    #after we will build this function we will know if we can insert the "neseccary-data" in the data in this function i.e combined things that neseccary for write soport
    # in the form or write this things that consider to neseccary direct in createStaticsAndBlocks or in function that will run befor .  
    #we wnat to check if in the place that we insert this data or at least the data that we want to create spesific in form as empty place or place with just these value 
    #from the names dictionary in the data base
        
    for generalyPatternlist,block in zip(patternDefaultDatasFilled['patternData']['requestsListGenerally']['blocks'],patternDefaultDatasFilled['patternDefaultBlock']['real_block']):
        #So basically the one argument zip is consistunet-list that contain in every list ,every passible generaly pattern for for this spesific mark in block
        # and the the second argument is actually the all the "real-block" that we wrote in one list 
        requestSpesificType=[]
        idBlockPattern=re.compile(r'[A-Z]{1}/d+')
        for generalyPattern in generalyPatternlist:
            if re.findall(generalyPattern,block):
              requestSpesificType.append(re.findall(generalyPattern,block))
        idBlock=re.match(idBlockPattern,block[:-1])
        if idBlock:
          if idBlock.group() in patternDefaultDatasFilled['patternDefaultBlock']['blockNames']:
            if not form['requests']['mark'][idBlock]: 
              form['requests']['block']['mark'][idBlock]=[]
            form['requests'][idBlock].append(requestSpesificType)
            requestSpesificType=[]
          else:
              form['response']['error']['request'].append(f"The requestMarks : {requestSpesificType} failed because the name block doesn't found in your store block")
        else:   
            form['response']['error']['request'].append(f"The requestMarks : {requestSpesificType} failed because the name block doesn't found in the spesific block")
    preciselyPatternList=[]
    for requestMark in form['requests']['block']['mark']:
        for presicelymarkPattern in patternDefaultDatasFilled['patternData']['preciselyPattern']['block']:
            combinedPattern=''
            for presicelyStagePattern in presicelymarkPattern:
                partNumber=True
                combinedPattern=''
                for presicelyPattern in presicelyStagePattern:
                    pattern=re.compile(presicelyPattern)
                    if partNumber==True:
                        match=re.match(pattern,requestMark)
                        partNumber=False
                    else:
                      match=re.search(pattern,requestMark)
                    if match:
                        combinedPattern+=presicelyPattern
                        break
                    elif presicelyPattern==presicelymarkPattern[-1]:
                        form['response']['error']
            preciselyPatternList.append(combinedPattern)
    form['requests']['presicely']['block']=[]
    form['requests']['presicely']['block'].append(preciselyPatternList)
