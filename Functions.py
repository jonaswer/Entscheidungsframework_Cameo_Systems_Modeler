# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:23:49 2021

@author: jonas.werheid
"""

from sklearn import preprocessing
import numpy as np
import random

def transferModelParametersToJoiningTechnologies(models, joiningTechnologiesDict):
    
    for key, value in models.items():
        joiningTechnologyOfModel = key.split("%")[0]
        parameterOfModel = key.split("%")[1]
        valueOfModel = value 
        
        if joiningTechnologyOfModel in joiningTechnologiesDict.keys():
            joiningTechnologiesDict[joiningTechnologyOfModel].setModelParameter(parameterOfModel, valueOfModel)
    
        else:
            continue
    
    return


def getPossibleJoiningTechnologies(joiningTechnologiesList, joiningTechnologiesDict, projectPreferences):

    count = 0
    connection_type_punctual_linear_field_ = projectPreferences.getDataFrame()['value'].tolist()[0]
    for i in range(len(connection_type_punctual_linear_field_)):
        if (connection_type_punctual_linear_field_[i] == 1):
            count += 1
            joining_zone_variant = i         
    if (count>1):
        print("ERROR: Es kann nur eine Fuegevariante angegeben werden ### Functions.py line38")
        exit()
    if (count==0):
        print("ERROR: Es muss eine Fuegevariante angegeben werden ### Functions.py line41")
        exit()
    
    count2 = 0
    mixed_compounds_with_thermoplastics_or_pure_metal_compound_ = projectPreferences.getDataFrame()['value'].tolist()[1]
    for j in range(len(mixed_compounds_with_thermoplastics_or_pure_metal_compound_)):
        if (mixed_compounds_with_thermoplastics_or_pure_metal_compound_[j] == 1): 
            count2 += 1
            compound_combination_variant = j         
    if (count2>1):
        print("ERROR: Die Verbindung kann nicht mit UND ohne Kunststoff sein, schließen Sie eine Variante aus ### Functions.py line51")
        exit()
    if (count2==0):
        print("ERROR: Ist die Verbindung mit oder ohne Kunststoff? ### Functions.py line54")
        exit()
        
    remove_list = []
   
    for i in range(len(joiningTechnologiesList)):
        if (joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()['value'].tolist()[0][joining_zone_variant] == 1):
            continue
        else:

            joiningTechnologiesDict.pop(str(joiningTechnologiesList[i]))
            remove_list.append(str(joiningTechnologiesList[i]))
    for i in range(len(remove_list):    
        joiningTechnologiesList.remove(remove_list[i])
    
    remove_list = []

    for i in range(len(joiningTechnologiesList)):     

        if (joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()['value'].tolist()[1][compound_combination_variant] == 1):
            continue
        else:
           joiningTechnologiesDict.pop(str(joiningTechnologiesList[i])) 
           remove_list.append(str(joiningTechnologiesList[i]))
    for i in range(len(remove_list)):
        joiningTechnologiesList.remove(remove_list[i])
      
        
    remove_list = []
           
    for i in range(len(joiningTechnologiesList)): 

        if (projectPreferences.getDataFrame()['value'].tolist()[2] == "1"):
            continue

        if  (projectPreferences.getDataFrame()['value'].tolist()[2] == "0"):
            if (joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()['value'].tolist()[2] == "0"):
                continue
            else:
                joiningTechnologiesDict.pop(str(joiningTechnologiesList[i]))
                remove_list.append(str(joiningTechnologiesList[i]))
    
    for i in range(len(remove_list)):
        joiningTechnologiesList.remove(remove_list[i])
        
    remove_list = []
    
    for i in range(len(joiningTechnologiesList)):
                
        if  (projectPreferences.getDataFrame()['value'].tolist()[3] == "0"):
            continue
        if  (projectPreferences.getDataFrame()['value'].tolist()[3] == "1"):
            if (joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()['value'].tolist()[3] == "1"):
                continue
            else:
                joiningTechnologiesDict.pop(str(joiningTechnologiesList[i]))
                remove_list.append(str(joiningTechnologiesList[i]))       
            
    for i in range(len(remove_list)):
        joiningTechnologiesList.remove(remove_list[i])
    
    return joiningTechnologiesDict


def deleteBooleansInDataFrames(joiningTechnologiesDict, projectPreferences):
    
    joiningTechnologiesList = list(joiningTechnologiesDict.keys())
    
    for i in range(len(joiningTechnologiesList)):
        
        joiningTechnologiesDict[joiningTechnologiesList[i]].dropBooleans()
        
    projectPreferences.dropBooleans()
    
    return


def scaleParametersValues(joiningTechnologiesDict, projectPreferences):    
    
    joiningTechnologiesList = list(joiningTechnologiesDict.keys())
    
    projectPreferencesDataFrame = projectPreferences.getDataFrame()
    projectPreferencesDataFrame = projectPreferencesDataFrame[projectPreferencesDataFrame.datatype == 'parameters']
    boundaries = projectPreferencesDataFrame['value'].tolist()
    
    for i in range (len(joiningTechnologiesList)):

        listOfValues = []
        
        dataFrame = joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()
        dataFrame = dataFrame[dataFrame.datatype == 'parameters']
        values = dataFrame['value'].tolist()
         
        for y in range(len(values)):
            
            mean = values[y][0]
            standard_deviation = values[y][1]
            distribution = np.random.normal(mean, standard_deviation, 2000)
    
            c = 0 
            for k in range(len(distribution)):
                       if distribution[k] >= boundaries[y]:
                           c += 1
            ratio = c / len(distribution)
            listOfValues.append(ratio)

        joiningTechnologiesDict[joiningTechnologiesList[i]].scaleParameters(listOfValues)                                        

    return


def scaleCertainParameters(joiningTechnologiesDict):
    
    joiningTechnologiesList = list(joiningTechnologiesDict.keys())
    
    for i in range (len(joiningTechnologiesList)):
         
        joiningTechnologiesDict[joiningTechnologiesList[i]].scaleCertainParameters()
    
    return


def rateJoiningTechnologies(joiningTechnologiesDict, projectPreferences, selectInformation):
    
    joiningTechnologiesRating = {}
    joiningTechnologiesInformation = {}
      
    joiningTechnologiesList = list(joiningTechnologiesDict.keys())
    joiningTechnologiesNames = list(joiningTechnologiesDict.keys())
    
    for i in range (len(joiningTechnologiesList)):

          joiningTechnologyDataFrame = joiningTechnologiesDict[joiningTechnologiesList[i]].getDataFrame()
          joiningTechnologyValues = joiningTechnologyDataFrame['value'].values.tolist()
          projectPreferencesDataFrame = projectPreferences.getDataFrame()
          projectPreferencesValues = projectPreferencesDataFrame['value'].values.tolist()
          
          rating = 0
          
          for y in range (len(projectPreferencesValues)):
              
                       
              if (len(projectPreferencesValues) != len(joiningTechnologyValues)):
                  print("Projektpraeferenzen fehlen oder Datenbankproblem  ### Functions.py Line197")
                  exit()
              else:
              
                  if y <= 2:    
                      rating = rating + joiningTechnologyValues[y]
                      if (joiningTechnologyValues[y] <= 0.66) and (joiningTechnologyValues[y] > 0.10) and (selectInformation == "ja"):
                          information = projectPreferencesDataFrame['parameter'].values.tolist()[y] + " erfuellt unter Beruecksichtigung der Unsicherheitsabschaetzung nur zu einer Wahrscheinlichkeit von " + str(joiningTechnologyValues[y]*100) + "% die Anforderungen des Projektes."
                          
                          if str(joiningTechnologiesNames[i]) in joiningTechnologiesInformation.keys():
                              joiningTechnologiesInformation[joiningTechnologiesNames[i]].append(information)
                          else:
                              joiningTechnologiesInformation[joiningTechnologiesNames[i]] = [information]

                        
                      if (joiningTechnologyValues[y] <= 0.10) and (selectInformation == "ja"):
                          information = projectPreferencesDataFrame['parameter'].values.tolist()[y] + " erfuellt unter Beruecksichtigung der Unsicherheitsabschaetzung die Anforderungen nicht."
    
                          if str(joiningTechnologiesNames[i]) in joiningTechnologiesInformation.keys():
                              joiningTechnologiesInformation[joiningTechnologiesNames[i]].append(information)
                          else:
                              joiningTechnologiesInformation[joiningTechnologiesNames[i]] = [information]
                        
                        
                  else:
                      if (joiningTechnologyValues[y] >= projectPreferencesValues[y]):
                          rating = rating + 1
                      else:
                          rating = rating + (joiningTechnologyValues[y] / projectPreferencesValues[y])
                    
                      if (projectPreferencesValues[y]>joiningTechnologyValues[y]) and  (selectInformation == "ja"):

                          information = projectPreferencesDataFrame['parameter'].values.tolist()[y] + " wird nach Fuzzy Abschaetzung wahrscheinlich nicht erfuellt"
            
                          if str(joiningTechnologiesNames[i]) in joiningTechnologiesInformation.keys():
                                  joiningTechnologiesInformation[joiningTechnologiesNames[i]].append(information)
                          else:
                              joiningTechnologiesInformation[joiningTechnologiesNames[i]] = [information]
    
    
          joiningTechnologiesRating[joiningTechnologiesNames[i]] = rating
          
    for key, value in joiningTechnologiesRating.items():
        value = ( value / 9 ) * 100 
        joiningTechnologiesRating[key] = value

    return joiningTechnologiesRating, joiningTechnologiesInformation
        
    
