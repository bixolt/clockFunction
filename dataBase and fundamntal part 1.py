import re

# Function to create static data and code
def createStaticsAndCode(data=None, patternDefaultDatas=None):
    if data is None:
        data = [[[[['staticData']]]], [[['Code']]]]
    if patternDefaultDatas is None:
        patternDefaultDatas = {
            'staticData': {'dataName': {'dataNamePrecisely': {'typeCode': []}}},
            'codeData': {'realCode': {'typeCode': {}}},
            'fundamentalData': {'fundamentalType': {'codeType': []}}
        }

    # Processing static data
    for subDataClient, dataNamePattern in zip(data[0], patternDefaultDatas['staticData'].keys()):
        for subDataClient2, dataNamePrecisely in zip(subDataClient, patternDefaultDatas['staticData'][dataNamePattern].keys()):
            for subDataClient3, typeCode in zip(subDataClient2, patternDefaultDatas['staticData'][dataNamePattern][dataNamePrecisely].keys()):
                for staticData in subDataClient3:
                    if not isinstance(patternDefaultDatas['staticData'][dataNamePattern][dataNamePrecisely][typeCode], list):
                        patternDefaultDatas['staticData'][dataNamePattern][dataNamePrecisely][typeCode] = []
                    patternDefaultDatas['staticData'][dataNamePattern][dataNamePrecisely][typeCode].append(staticData)
    
    # Processing code data
    for typeCode in patternDefaultDatas['staticData']['dataName']['dataNamePrecisely']['typeCode']:
        for patternId in patternDefaultDatas['staticData']['dataName']['dataNamePrecisely']['typeCode']:
            for subHighLevelData in data[1]:
                for subData in subHighLevelData:
                    for code in subData:
                        match = re.match(patternId, code[1:])
                        if match:
                            if typeCode not in patternDefaultDatas['codeData']['realCode']:
                                patternDefaultDatas['codeData']['realCode'][typeCode] = {}
                            patternDefaultDatas['codeData']['realCode'][typeCode][match.group()] = code
                            patternDefaultDatas['codeData']['idData'][typeCode]['id'] = match.group()
    
    return patternDefaultDatas
pattern_default_datas_filled = createStaticsAndCode()
# Function to add additional form data to the existing form
def additionFormFunction(form, additionalForm):
    for typeOf, subData in additionalForm.items():
        if typeOf not in form:
            form[typeOf] = {}
        insertInternalData(subData, form[typeOf])

# Helper function to recursively insert internal data into current data
def insertInternalData(subData, current_data):
    if isinstance(subData, str):
        if subData not in current_data:
            current_data[subData] = {}
    elif isinstance(subData, list):
        for item in subData:
            if isinstance(item, str) and item not in current_data:
                current_data[item] = {}
            elif isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, list):
                        if key not in current_data:
                            current_data[key] = []
                        current_data[key].extend(value)
    elif isinstance(subData, dict):
        for subInternalName, value in subData.items():
            if isinstance(value, dict):
                if subInternalName not in current_data:
                    current_data[subInternalName] = {}
                insertInternalData(value, current_data[subInternalName])
            elif isinstance(value, list):
                if subInternalName not in current_data:
                    current_data[subInternalName] = []
                current_data[subInternalName].extend(value)
            elif isinstance(value, str):
                if subInternalName not in current_data:
                    current_data[subInternalName] = {}
                current_data[subInternalName] = value

# Define example form structure
form = {'status': {}, 'response': {'error': {'request': {}, 'running': {}}}, 'requests': {'precisely': {}}, 'name': {}}
additionalForm = {
    'error': ['request', 'running'],
    'requests': [
        'name', {'mark': ['block', 'text']},
        {'details': [{'block': [{'dynamic-name': ['argument', 'tag']}]}]}
    ],
    'internal-request': ['private-request-details']
}

# Apply the additional form function to populate the form
additionFormFunction(form, additionalForm)

# Print the updated form to verify correctness
import pprint
pprint.pprint(form)

    #In order to make to do this procces that will make all the sub data in the from and after to insert the fundamental data like id block where we need 
    #we can in this case to do recursive when this statment happen isinstance(form[typeOf],dict) and create a list that will contain all the "key" we check and return any dict
    #and after we will just call to the function that create the empty data in spesific place like this :
    #But the problem with just put this function that we may more things in the same condition that mean may in this proccess form[key[i]]={} we delete thing in 
    #the second we need to put second loop in order to get the value of and the key .
    #In shortly we need to find way to call the function that turn on again the searching on the element issue and contain all of the keys that we have from this and 
    #sparete the keys we need to active for every organ it self and to care about and so to put in . work with additionalForm and the form in the same time and in the runing 
    #i.e to care about one thing in the additionalForm function and to add or do something in the Form in the same time that we decide for other fucntion or things .
    #if we insert all the data in createSpesific we can catch it . 

#fundamentalData that we want to change or not and insert to any place in form 
#We actually will insert this type of fundamntal data to the form according to the fundamntal data in the fundamntal place at the data place in static data we insert .
#We have tow different type "fundamntal-data" one is like the data we insert according the ordinary things that we insert in the "static-data" and second is fundamntal data
#we insert according to things that in the place that exist for fundamntal-data in static data . But all the sources from static-data. 

#The "fundmantalThing" is actually very important because of it do tow thing 1: create the funmantal data with the material we give and the function that suit 
#2 : also because of the function that choise according the fundamntalThing we know where exact to insert the fundamntal data to the form 
import itertools

def create_indexed_list(text, organ_list):
    organRangeInText = []
    current_index = 0 
    for organ in organ_list:
        start_index = text.find(organ, current_index)
        end_index = start_index + len(organ) - 1
        organRangeInText.append((start_index, end_index))  # Append as tuple
        current_index = end_index + 1  # Update current index
    return organRangeInText  

def push(text, index, data):
    return text[:index] + data + text[index:]  # Return the modified text

def delete_range(text, deleteRange):
    start_index, end_index = deleteRange
    return text[:start_index] + text[end_index + 1:]  # Return the modified text

def addFormFundamental():
    for fundamentalType in pattern_default_datas_filled['fundamentalData'].keys():
        for codeType, modifyFundamentalData in pattern_default_datas_filled[fundamentalType].items():
            paths = createPathsForFormAndForModifyData(fundamentalType, codeType)
            create_and_insert_fundamental_data(modifyFundamentalData, paths, fundamentalType, codeType)

def evaluate_condition(condition_str, data):
    """
    Evaluate the condition string on the value.
    
    Args:
    - condition_str (str): The condition string to evaluate.
    - data (any): The data against which the condition is evaluated.
    
    Returns:
    - bool: True if the condition evaluates to True, False otherwise.
    """
    try:
        return eval(condition_str, {'data': data})
    except Exception as e:
        print(f"Error evaluating condition: {e}")
        return False


def find_paths_by_condition(data, condition_str, path_prefix=[]):
    """
    Recursively find paths in the data that match the condition.
    
    Args:
    - data (dict or list): The data to search within.
    - condition_str (str): The condition string to evaluate.
    - path_prefix (list): The prefix path to start searching from (default []). 
    
    Returns:
    - list: A list of paths (lists) in the data that match the condition.
    """
    matching_paths = []

    if isinstance(data, dict):
        disassembly_data = data.items()
    elif isinstance(data, list):
        disassembly_data = enumerate(data)
    else:
        return matching_paths

    for key, value in disassembly_data:
        new_path_prefix = path_prefix + [key]
        if evaluate_condition(condition_str, value):
            matching_paths.append(new_path_prefix)
        matching_paths.extend(find_paths_by_condition(value, condition_str, new_path_prefix))

    return matching_paths


def create_and_insert_fundamental_data(modify_fundamental_data, paths, fundamental_type, code_type):
    """
    Create and insert fundamental data into designated places according to conditions and paths.

    Args:
    - modify_fundamental_data (any): Data used to modify fundamental data.
    - paths (dict): Paths dictionary specifying where to insert data.
    - fundamental_type (str): The type of fundamental data.
    - code_type (str): The type of code for which to modify fundamental data.
    """
    type_using_paths = {'insertPlace': ['form'], 'auxiliaryContentForModifyData': ['staticData']}
    conditions_to_modify_fundamental_data = {
        'codeType': {
            'fundamentalType': {
                'form/or other insertPlace': {
                    'function1': [
                        modify_fundamental_data,
                        f"paths['staticData'][1], paths['staticData'][2] ~ data !== 2 and value == 1^^ 'more condition and data for the same argument",
                        'otherArgument'
                    ],
                    'function2': ['argument'],
                    'function3': ['all!staticData^^moreRequest for data in this argument', modify_fundamental_data]
                }
            },
            'codeType2': {
                'fundamentalType2': {
                    'function': 'codeType$fundamentalType$insertPlace$function'
                }
            }
        }
    }

    # Insert data into specified places
    for insert_place in type_using_paths['insertPlace']:
        for function, arguments_list in conditions_to_modify_fundamental_data[code_type][fundamental_type].items():
            if isinstance(arguments_list, list):
                for arguments in arguments_list:
                    if isinstance(arguments, list):
                        arguments_place = ()
                        for argument in arguments:
                            arguments_place += (argument,)
                        function_str = f"{function}{arguments_place}"
                        data = eval(function_str)
                        for path in paths[insert_place]:
                            insert_data(form, path, data)

    # Define internal command function to retrieve all data
    def all_command(data_for_function_command):
        paths_data = paths[data_for_function_command]
        data = get_nested_data(pattern_default_datas_filled[data_for_function_command], paths_data)
        return data

    # Internal commands dictionary for special commands
    internal_commands = {'all': all_command('data')}

    # Perform preparation for importing data

    preparation_import_data('function', conditions_to_modify_fundamental_data, code_type, fundamental_type,
                            paths_type=None, run_number=0, paths_insert_copied_data=[])

    # Modify data according to conditions and paths
    for function, arguments_index in zip(conditions_to_modify_fundamental_data[code_type][fundamental_type].keys(),
                                         range(len(conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index]))):
        if isinstance(conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index], str):
            request_for_data_in_argument_places = conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index].split('^^')
            organ_range_in_text = create_indexed_list(
                conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index], request_for_data_in_argument_places)
            index_roof = 0
            for request_for_data_in_argument_place in request_for_data_in_argument_places:
                skip_outer_loop = False
                for internal_command in internal_commands.keys():
                    internal_command_length = len(internal_command)
                    request_for_data_in_argument_place_search_internal_command = request_for_data_in_argument_place[0:internal_command_length - 1]
                    if request_for_data_in_argument_place_search_internal_command == internal_command and request_for_data_in_argument_place[internal_command_length] == '!':
                        data_for_function_command = internal_command[len(internal_command):]
                        data = internal_commands[internal_command](data_for_function_command)
                        organ_range = organ_range_in_text[index_roof]
                        for organ_range_index in range(*organ_range):
                            del conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][organ_range_index]
                        conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index].insert(organ_range[0], data)
                        skip_outer_loop = True
                if skip_outer_loop:
                    index_roof += 1
                    continue
                separate_between_data_and_condition = re.findall(r'\s+\~\s+', request_for_data_in_argument_place)
                datas = separate_between_data_and_condition[0].split(',')
                for index_data, data in enumerate(datas):
                    space_split = re.findall(r'\s+', data)
                    if len(space_split) > 1:
                        datas[index_data] = space_split[0]
                if len(separate_between_data_and_condition) > 1:
                    range_data_index = create_indexed_list(
                        conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][
                        organ_range[0]:organ_range[1]], datas)
                    for index_data in range(len(datas)):
                        condition = separate_between_data_and_condition[1]
                        paths_data = find_paths_by_condition(condition, eval(datas[index_data]))
                        if paths_data:
                            for path_data in paths_data:
                                with_deletes = delete_range(
                                    conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][
                                    organ_range[0]:organ_range[1]], range_data_index[index_data])
                                conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][
                                    organ_range[0]:organ_range[1]] = with_deletes
                                data_for_argument = get_nested_data(eval(data), path_data)
                                conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index].insert(
                                    range_data_index[index_data][0], data_for_argument)
                        else:
                            data_for_argument = 'no suitable data'
                            del conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][
                                organ_range[0]:organ_range[1]]
                            conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index].insert(
                                organ_range[0], data_for_argument)
                elif separate_between_data_and_condition[0]:
                    for data in datas:
                        data_for_argument = eval(data)
                        del conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index][organ_range[0]:organ_range[1]]
                        conditions_to_modify_fundamental_data[code_type][fundamental_type][function][arguments_index].insert(
                            organ_range[0], data_for_argument)
                index_roof += 1


  #We will read the str arguments of function "modify" tit and insert as condition,data to function that give path for this data and after insert the data to spesific
  #argument to function . 

   #Function planing:
     #Put the wanted datas from the "fundamntalData" in correct function according the "fundamntalType", modify and more the "fundamntalData" according to data in
     #paths['staticData'] and insert the wnated things to form accroding path['form']. 
  
     #(that ok we choise the function that we active on the data just according the "fundamntalType" 
     #because the "fundamntalData" that in the "patternDefaultDatasFilled" we insert how much data we want in one "fundamntalType" and we
     #can create how much we want "fundamntalType"
     #and create request for happining for every one of them (turn-on function) . as well as we create condition(paths) according the "typeCode" (see how path conditions build
     # in 'createPathsForFormAndForModifyData' in 'fundamntalTypesPathsInterface' )  ).
"""for fundamntalTypePaths,pathsBig in paths.items():
     for pathsType in pathsBig.key():
        for path in pathsBig[pathsType]:"""

    #So item equel to 'all' in this tree i.e in this case should be -> 
    # staticData['data1']['data2'][staticData['data1']['data2'].key()]['data4']
#The porpuse to return it in this case in 'fundamntalTypesPathsSystemForm' : 
# ['path1']['path2']['pathA']['path4'],
#   ['path1']['path2']['pathB']['path4'],
#    ['path1']['path2']['pathC']['path4']
#if staticData['path1']['path2'].key()==['pathA','pathB','pathC']       
# We will read the str arguments of function "modify" tit and insert as condition,data to function that give path for this data and after insert the data to spesific
# argument to function.

# Function planning:
# Put the wanted data from the "fundamentalData" in correct function according to the "fundamentalType", modify and add more "fundamentalData" according to data in
# paths['staticData'] and insert the wanted things to form according to path['form'].
# 
# (It's okay to choose the function that we activate on the data just according to the "fundamentalType"
# because the "fundamentalData" that is in the "patternDefaultDatasFilled" allows us to insert as much data as we want in one "fundamentalType" and we
# can create as many "fundamentalType" as we want and create conditions (paths) according to the "typeCode" (see how path conditions are built
# in 'createPathsForFormAndForModifyData' in 'fundamentalTypesPathsInterface')).
def createPathsForFormAndForModifyData(fundamentalType, codeType):
    """
    Create paths for form and modify data based on specified fundamental type and code type.

    Args:
    - fundamentalType (str): The type of fundamental data.
    - codeType (str): The type of code for which paths are being created.
    """
    fundamentalTypesPathsInterface = {
        'typeCode': {
            'fundamentalType': [
                [['pathForm1', 'all', 'pathForm3', 'pathForm4'], ['otherFormPath']],
                [['otherStaticDataPath'], [['pathModifyStaticData1', 'pathModifyStaticData2', 'all', 'pathModifyStaticData4']]],
                ['other']
            ],
            'fundamentalType2': [['fundamentalType-typeCode'], ['fundamentalType3', ['fundamentalType-typeCode']]]
        },
        'typeCode2': {
            'fundamentalType2': [['fundamentalType-typeCode']],
            'fundamentalType3': [['fundamentalType$typeCode$staticData$3'], ['fundamentalType$typeCode$form'],
                                 ["otherPaths 'typeUsingPaths' look in function 'createAndInsertFundamentalData'"]]
        }
    }
    # The "$" indicates in "pathDrought" which data we want to place in this place according to the conditions of the function that care about it and the data in this specific dictionary.
    pathsType = ['form', 'staticData']
    preparation_import_data(fundamentalType, codeType, fundamentalTypesPathsInterface, pathsType)

    pathsTypeAndPathsForFormUsing = {}
    for specificPathsToFundamentalTypes in fundamentalTypesPathsInterface[codeType][fundamentalType]:
        for pathIndex in range(len(specificPathsToFundamentalTypes[fundamentalType])):
            fundamentalPathsInterface = []
            for itemIndex in range(len(specificPathsToFundamentalTypes[fundamentalType][pathIndex])):
                if specificPathsToFundamentalTypes[fundamentalType][pathIndex][itemIndex] != 'all':
                    fundamentalPathsInterface.append([specificPathsToFundamentalTypes[fundamentalType][pathIndex][itemIndex]])
                else:
                    partPath = specificPathsToFundamentalTypes[fundamentalType][pathIndex][:itemIndex]
                    dynamic_keys = get_nested_keys(pattern_default_datas_filled, partPath)
                    fundamentalPathsInterface.append(list(dynamic_keys))

            paths1 = [[]]
            for pathInterface in fundamentalPathsInterface:
                newPaths1 = []
                for item in pathInterface:
                    if paths1[0]:
                        for currentPath in paths1:
                            newPaths1.append(currentPath + [item])
                    else:
                        newPaths1.append([item])
                paths1 = newPaths1

            print(f"paths1 after processing {specificPathsToFundamentalTypes[fundamentalType][pathIndex]}: {paths1}")
            pathsTypeAndPathsForFormUsing[pathsType[pathIndex]] = paths1


    return pathsTypeAndPathsForFormUsing
def get_nested_keys(data, path):
    """
    Traverse the data structure following the keys in the path
    and return the keys of the last node.

    Args:
    - data (dict or list): The nested data structure to traverse.
    - path (list): List of keys to traverse the data structure.

    Returns:
    - keys of the last node in the path.
    """
    for key in path:
        data = data[key]
    return data.keys()

def get_nested_data(data, path):
    """
    Traverse the data structure following the keys in the path
    and return the value of the last node.

    Args:
    - data (dict or list): The nested data structure to traverse.
    - path (list): List of keys to traverse the data structure.

    Returns:
    - value of the last node in the path.
    """
    for key in path:
        data = data[key]
    return data

def insert_data(area, path, data):
    """
    Traverse the data structure following the keys in the paths (excluding the last key)
    and insert the data at the final destination.

    Args:
    - area (dict or list): The nested data structure where data will be inserted.
    - path (list): List of keys to traverse the data structure, excluding the last key.
    - data: The data to insert at the final destination.
    """
    for key in path[:-1]:
        area = area[key]
    area[path[-1]] = data

def insertFundamentalDataForm(form, data, fundamentalPathsSystem):
    """
    Insert fundamental data into the form structure based on the paths in fundamentalPathsSystem.

    Args:
    - form (dict): The form structure where data will be inserted.
    - data: The data to insert into the form structure.
    - fundamentalPathsSystem (dict): Dictionary containing paths to insert data into the form structure.
    """
    for paths in fundamentalPathsSystem['form']:
        for path in paths:
            current = form
            for item in path[:-1]:
                if item not in current:
                    current[item] = {}
                current = current[item]
            current[path[-1]] = data


def preparation_import_data(systemType, system, codeType, fundamntalType, pathsType=None, runNumber=0, pathsInsertCopiedData=[]):
    """
    Prepare paths for form or static data based on the given interface and insert them into the system.

    Args:
    - systemType (str): Type of the system.
    - system (dict): The system data structure.
    - codeType (str): Type of the code.
    - fundamntalType (str): Type of the fundamental data.
    - pathsType (list, optional): List of paths types. Default is None.
    - runNumber (int, optional): Run number. Default is 0.
    - pathsInsertCopiedData (list, optional): List of paths to insert copied data. Default is an empty list.
    """
    wantedPaths = system[codeType][fundamntalType]
    for wantedPathIndex in range(len(wantedPaths)):
        if not isinstance(wantedPaths[wantedPathIndex], str):
            if '$' in wantedPaths[wantedPathIndex]:  # Check if the path contains a '$' indicating dynamic path
                if wantedPaths[wantedPathIndex].count('$') == runNumber:
                    commandPath = wantedPaths[wantedPathIndex].split('$')
                    if systemType == 'paths':
                        if len(commandPath) >= 3:
                            commandPath[2] = pathsType[commandPath.index(commandPath[2])]
                        if len(commandPath) >= 4:
                            commandPath[3] = int(commandPath[3])
                    # Handle additional conditions and modify paths accordingly
                    insert_data_according_fundamntal_paths(commandPath, system, codeType, fundamntalType, pathsInsertCopiedData)
                else:
                    print(f"Path '{wantedPaths[wantedPathIndex]}' is not valid for run number {runNumber}.")
            else:
                print(f"Expected a dynamic path with '$' for index {wantedPathIndex}. Found: {wantedPaths[wantedPathIndex]}")
        else:
            if isinstance(wantedPaths[wantedPathIndex], list):
                pathsInsertCopiedData.append(wantedPathIndex)
                preparation_import_data(systemType, system, codeType, fundamntalType, pathsType, runNumber, pathsInsertCopiedData)

def insert_data_according_fundamntal_paths(commandPath, system, codeType, fundamntalType, pathsInsertCopiedData):
    """
    Get the data according to the command path and insert it into the appropriate location.

    Args:
    - commandPath (list): List representing the command path.
    - system (dict): The system data structure.
    - codeType (str): Type of the code.
    - fundamntalType (str): Type of the fundamental data.
    - pathsInsertCopiedData (list): List of paths to insert copied data.
    """
    data = get_nested_data(system, commandPath)
    pathForPaste = [codeType, fundamntalType] + pathsInsertCopiedData
    insert_data(system, pathForPaste, data)

def insert_fundamental_data_to_form():
    """
    Insert fundamental data into the form structure based on predefined patterns and codes.
    """
    for codeType in pattern_default_datas_filled['codeData'].keys():
        for idCode in pattern_default_datas_filled['codeData'][codeType]:
            code = pattern_default_datas_filled['codeData'][codeType][idCode]
            for markType, generalPatternList in pattern_default_datas_filled['staticData']['request']['requestsGenerally'][codeType].items():
                for generalPattern in generalPatternList:
                    if re.findall(generalPattern, code):
                        generalRequests = re.findall(generalPattern, code)
                        if not form['requests']['generallyRequest'][markType][codeType][idCode]:
                            form['requests']['generallyRequest'][markType][codeType][idCode] = []
                        form['requests']['generallyRequest'][markType][codeType][idCode].append(*generalRequests)

            for generalRequest in generalRequests:
                for patternsStagesRequest in pattern_default_datas_filled['staticData']['request']['preciselyPattern'][markType][codeType]:
                    for patternsStageRequest in patternsStagesRequest:
                        for patternStageRequest in patternsStageRequest:
                            partNumber = True
                            combinedPattern = []
                            pattern = re.compile(patternStageRequest)
                            if partNumber == True:
                                match = re.match(pattern, generalRequest)
                                partNumber = False
                            else:
                                match = re.search(pattern, generalRequest)
                            if match:
                                combinedPattern.append(patternStageRequest)
                                break

                        form['requests']['mark'][markType][codeType][idCode] = combinedPattern