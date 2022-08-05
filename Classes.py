# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:08:10 2021

@author: jonas.werheid
"""

import pandas as pd
import random
import numpy as np
from itertools import repeat

'''#####################################################################################################################################'''    
'''Every joining technology has a own instance of the class JoiningTechnology'''

class JoiningTechnology:
    
    
    def __init__(self, name, data):
        
        self.name = name
        self.data = data
        
        self.setDataFrame()
        self.transformFuzzy()
        self.setData()
    
        
    def setDataFrame(self):
        
        #Method to create dataframe from the given data
        
        joiningTechnologies = self.data["joiningTechnologies"]
        dfObj = pd.DataFrame(columns=['datatype', 'parameter', 'value'])

        for i, category in enumerate (joiningTechnologies[self.name].keys()):
        
            if i != 0:
                categorydict = joiningTechnologies[self.name][category]
                df = pd.DataFrame(list(categorydict.items()),columns = ['parameter','value']) 
                datatype = [category for i in range(df.shape[0])]
                df['datatype'] = datatype
                dfObj = dfObj.append([df], sort=False)
                
        self.dataFrame=dfObj
            
        return
    
    
    
    def transformFuzzy(self):
        
        #Method for transforming fuzzy words into a parametric values
        
        values = self.dataFrame['value'].tolist()
        
        for i in range(len(values)):
            if values[i] == "Very High" or values[i] == "Very high" or values[i] == "very high":
                values[i] = 1
            if values[i] == "High" or values[i] == "high":
                values[i] = 0.75
            if values[i] == "Normal" or values[i] == "normal":
                values[i] = 0.5
            if values[i] == "Low" or values[i] == "low":
                values[i] = 0.25
            if values[i] == "Very Low" or values[i] == "Very low" or values[i] == "very low":
                values[i] = 0
                
        self.dataFrame['value'] = values
            
        return
    
    
    def setData(self):
        
        #Method to create an Object of each parameter of each dataframe
        
        self.dataDict = {}
        
        for i,j in self.dataFrame.iterrows():
            #parameter = j.tolist()
            parameter = Parameter(j.tolist())
            self.dataDict[j.tolist()[1]] =  parameter
            
        return
        
    def dropBooleans(self):
        
        self.dataFrame = self.dataFrame[self.dataFrame.datatype != 'booleans']
        
        return
    
    
    def setModelParameter(self, parameterOfModel, valueOfModel):
       
        self.dataFrame['value'].iloc[self.dataFrame.index[self.dataFrame.parameter == parameterOfModel][0]] = valueOfModel        
        
        return
        
    
    def scaleParameters(self, values):
        
        self.dataFrame['value'].iloc[0] = values[0]
        self.dataFrame['value'].iloc[1] = values[1]
        self.dataFrame['value'].iloc[2] = values[2]
    
        return
    

    ''' Some Parameters are better if their values are smaller, to compare the Dataframes we need to subtract 1 minus these certain parameters '''
    def scaleCertainParameters(self): 
        
        production_cycle_time = self.dataFrame.iloc[0, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[0, self.dataFrame.columns.get_loc('value')] = 1 - production_cycle_time
        costs = self.dataFrame.iloc[1, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[1, self.dataFrame.columns.get_loc('value')] = 1 - costs
        weight = self.dataFrame.iloc[7, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[7, self.dataFrame.columns.get_loc('value')] = 1 - weight
         
        return
        
    
    def getDataFrame(self):
    
        return self.dataFrame
    
    
    def getDataDict(self):
        
        return self.dataDict
  
    
    
'''#####################################################################################################################################'''
'''The project preferences are structured in this class'''



class ProjectPreferences:   
    
    
    def __init__(self, cameoData, data):
    
        self.cameoData = cameoData
        self.data = data
        self.transformBooleans()
        self.transformFuzzy()
        self.getDataTypeOfParameters()
        self.setDataFrame()
         
    
    def transformBooleans(self):
             
        #Method for transforming booleans to integer
        
        values = list(self.cameoData.values())
        for i in range(len(values)):
            if values[i] == "ja" or values[i] == "Ja" or values[i] == "yes":
                key = list(self.cameoData)[i]
                self.cameoData[key] = "1"
            if values[i] == "nein" or values[i] == "Nein" or values[i] == "No":
                key = list(self.cameoData)[i]
                self.cameoData[key] = "0"
            if (type(values[i]) == list):
                for j in range(len(values[i])):
                    if values[i][j] == "ja" or values[i][j] == "Ja" or values[i][j] == "yes":
                        values[i][j] = 1
                    if values[i][j] == "nein" or values[i][j] == "Nein" or values[i][j] == "No":
                        values[i][j] = 0
            else:
                continue
    
        return
    

    def transformFuzzy(self):
        
        #Method for transforming fuzzy words into a parametric values
        
        values = list(self.cameoData.values())
        for i in range(len(values)):
            if values[i] == "Sehr Wichtig" or values[i] == "Sehr wichtig" or values[i] == "sehr wichtig":
                key = list(self.cameoData)[i]
                self.cameoData[key] = 1
            if values[i] == "Wichtig" or values[i] == "wichtig":
                key = list(self.cameoData)[i]
                self.cameoData[key] = 0.75
            if values[i] == "Normal" or values[i] == "normal":
                key = list(self.cameoData)[i]
                self.cameoData[key] = 0.5
            if values[i] == "Weniger Wichtig" or values[i] == "Weniger wichtig" or values[i] == "weniger wichtig":
                key = list(self.cameoData)[i]
                self.cameoData[key] = 0.25
            if values[i] == "Nicht Wichtig" or values[i] == "nicht wichtig":
                key = list(self.cameoData)[i]
                self.cameoData[key] = 0
            else:
                continue
            
        return
        
    
    def getDataTypeOfParameters(self):
        
        #Method to connect given data from cameo with the datatype structure of json (not well written/new one?)
        
        datatypesOfParameters = {}
         
        joiningTechnologies = self.data["joiningTechnologies"]
    
        joiningTechnologies = self.data["joiningTechnologies"][random.choice(list(self.data["joiningTechnologies"]))]
        booleans = list(joiningTechnologies['booleans'].keys())
        booleanss = list(repeat("booleans", len(booleans)))
        fuzzy_set = list(joiningTechnologies['fuzzy set'].keys())
        fuzzy_sett = list(repeat("fuzzy set", len(fuzzy_set)))
        parameters = list(joiningTechnologies['parameters'].keys())
        parameterss = list(repeat("parameters", len(parameters)))
        for i in range (len(booleans)):
            datatypesOfParameters[booleans[i]] = booleanss[i]
        for i in range (len(fuzzy_set)):
            datatypesOfParameters[fuzzy_set[i]] = fuzzy_sett[i]       
        for i in range (len(parameters)):
            datatypesOfParameters[parameters[i]] = parameterss[i]
            
        df2 = pd.DataFrame(list(datatypesOfParameters.items()),columns = ['parameter','datatype'])
        
        self.df2 = df2
        
        return df2
    
    
    def setDataFrame(self):
                     
        self.df = pd.DataFrame(list(self.cameoData.items()),columns = ['parameter','value'])    
        
        self.dataFrame = pd.merge(self.df, self.df2, on='parameter', how='inner')
        self.dataFrame = self.dataFrame[['datatype', 'parameter', 'value']]     
            
        return        
    
    
    def dropBooleans(self):
        
        self.dataFrame = self.dataFrame[self.dataFrame.datatype != 'booleans']
        
        return
    

    def scaleParameters(self, values):
        
        countParameters = self.dataFrame[self.dataFrame.datatype == 'parameters']
        countParameters = len(countParameters['value'].tolist())
        
        self.dataFrame['value'] = self.dataFrame['value'].replace(self.dataFrame['value'].tolist()[:countParameters],values)
    
        return
    
    
    ''' Some Parameters are better if their values are smaller, to compare the Dataframes we need to subtract 1 minus these certain parameters '''
    def scaleCertainParameters(self): ##Hardcode ##Ändern nach nächster Besprechung 
        
        production_cycle_time = self.dataFrame.iloc[0, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[0, self.dataFrame.columns.get_loc('value')] = 1 - production_cycle_time
        costs = self.dataFrame.iloc[1, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[1, self.dataFrame.columns.get_loc('value')] = 1 - costs
        weight = self.dataFrame.iloc[7, self.dataFrame.columns.get_loc('value')]
        self.dataFrame.iloc[7, self.dataFrame.columns.get_loc('value')] = 1 - weight
        
        return
        
    
    def getDataFrame(self):
        
        return self.dataFrame
   

    
'''#####################################################################################################################################'''
'''Every row of any initilized Dataframe has an own Object of the Class Parameter'''    
   


class Parameter:
    
    
    def __init__(self, columns):
        
        self.name = columns[1]
        self.datatype = columns[0]
        self.parameter = columns[2]
        
        
    def setDistribution(self):
        
        if self.datatype!='parameters':
            return "This datatype do not have a distribution"
        
        else:
            return
    
    
    def getBoolStatement(self):
        
        if self.datatype!='booleans':
            return "This datatype is not an boolean"

        else:
            return self.parameter