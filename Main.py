# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:57:43 2021

@author: jonas.werheid
"""

import sys
import os 
import json
import numpy as np 
import pandas as pd
import Classes
import Functions

if __name__ == '__main__':
        
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(__location__ + "\\database_joining.json") as f:
        data = json.load(f)
        
    '''Matlab datapipeline'''
    
    costs = float(str((sys.argv[1])))    
    maximum_allowable_tension = float(str((sys.argv[2])))
    production_cycle_time = float(str((sys.argv[3])))

    automatability = str((sys.argv[4]))
    automatability = automatability.replace('_', ' ')
    
    environmental_conditions = str((sys.argv[5]))
    environmental_conditions = environmental_conditions.replace('_', ' ')
    
    dynamic_tension = str((sys.argv[6]))    
    dynamic_tension = dynamic_tension.replace('_', ' ')
    
    occupational_safety = str((sys.argv[7]))    
    occupational_safety = occupational_safety.replace('_', ' ')
    
    weight = str((sys.argv[8]))
    weight = weight.replace('_', ' ')
    
    temperature_resistance = str((sys.argv[9]))
    temperature_resistance = temperature_resistance.replace('_', ' ')
    
    post_processing_necessary = str((sys.argv[12]))
    processing_with_one_sided_access_to_the_joint = str((sys.argv[13]))
    connection_type_punctual_linear_field = [str((sys.argv[14])), str((sys.argv[15])), str((sys.argv[16]))]
    mixed_compounds_with_thermoplastics_or_pure_metal_compound = [str((sys.argv[10])), str((sys.argv[11]))]
    removable_connection = str((sys.argv[54]))

    selectInformation =  str((sys.argv[17]))
    
    models = { 
             "joiningTechnology5_tailor_joints%costs" : [float(str((sys.argv[18]))),float(str((sys.argv[19])))],
             "joiningTechnology5_tailor_joints%production_cycle_time" : [float(str((sys.argv[20]))),float(str((sys.argv[21])))],
             "joiningTechnology5_tailor_joints%maximum_allowable_tension" : [float(str((sys.argv[22]))),float(str((sys.argv[23])))],
             "joiningTechnology3_glue%costs" : [float(str((sys.argv[24]))),float(str((sys.argv[25])))],
             "joiningTechnology3_glue%production_cycle_time" : [float(str((sys.argv[26]))),float(str((sys.argv[27])))],
             "joiningTechnology3_glue%maximum_allowable_tension" : [float(str((sys.argv[28]))),float(str((sys.argv[29])))],
             "joiningTechnology2_soldering%costs" : [float(str((sys.argv[30]))),float(str((sys.argv[31])))],
             "joiningTechnology2_soldering%production_cycle_time" : [float(str((sys.argv[32]))),float(str((sys.argv[33])))],
             "joiningTechnology2_soldering%maximum_allowable_tension" : [float(str((sys.argv[34]))),float(str((sys.argv[35])))],
             "joiningTechnology6_rivet%costs" : [float(str((sys.argv[36]))),float(str((sys.argv[37])))],
             "joiningTechnology6_rivet%production_cycle_time" : [float(str((sys.argv[38]))),float(str((sys.argv[39])))],
             "joiningTechnology6_rivet%maximum_allowable_tension" : [float(str((sys.argv[40]))),float(str((sys.argv[41])))],
             "joiningTechnology4_screw%costs" : [float(str((sys.argv[42]))),float(str((sys.argv[43])))],
             "joiningTechnology4_screw%production_cycle_time" : [float(str((sys.argv[44]))),float(str((sys.argv[45])))],
             "joiningTechnology4_screw%maximum_allowable_tension" : [float(str((sys.argv[46]))),float(str((sys.argv[47])))],
             "joiningTechnology1_welding%costs" : [float(str((sys.argv[48]))),float(str((sys.argv[49])))],
             "joiningTechnology1_welding%production_cycle_time" : [float(str((sys.argv[50]))),float(str((sys.argv[51])))],
             "joiningTechnology1_welding%maximum_allowable_tension" : [float(str((sys.argv[52]))),float(str((sys.argv[53])))]   
             }   

    '''test parameters'''
    
#    production_cycle_time = 2
#    costs = 5555
#    maximum_allowable_tension = 40
#    automatability = 'normal'
#    environmental_conditions = 'wichtig'
#    dynamic_tension = 'wichtig'
#    occupational_safety = 'normal'
#    weight = 'weniger wichtig'
#    temperature_resistance = 'normal'
#    #mixed_compounds_with_thermoplastics = 'ja' 
#    #pure_metal_compound = 'nein'
#    connection_type_punctual_linear_field = ['nein','ja','nein']
#    mixed_compounds_with_thermoplastics_or_pure_metal_compound = ['nein','ja']
#    post_processing_necessary = 'nein'
#    processing_with_one_sided_access_to_the_joint = 'nein'
#    removable_connection = 'ja'
# 
#    selectInformation = "ja"
#    
#    if (selectInformation != "ja"):
#        print("Setze selectInformation auf 'ja' für weitere Informationen zu den Fügetechnologien")
# 
#    models = { 
#             "joiningTechnology5_tailor_joints%costs" : [8,1.1],
#             "joiningTechnology5_tailor_joints%production_cycle_time" : [1,3.2],
#             "joiningTechnology5_tailor_joints%maximum_allowable_tension" : [43,2.3],
#             "joiningTechnology3_glue%costs" : [12,4.3],
#             "joiningTechnology3_glue%production_cycle_time" : [77,4.5],
#             "joiningTechnology3_glue%maximum_allowable_tension" : [39,2.2],
#             "joiningTechnology2_soldering%costs" : [12,2.2],
#             "joiningTechnology2_soldering%production_cycle_time" : [4,3.2],
#             "joiningTechnology2_soldering%maximum_allowable_tension" : [54,1.2],
#             "joiningTechnology6_rivet%costs" : [21,2.3],
#             "joiningTechnology6_rivet%production_cycle_time" : [12,3.2],
#             "joiningTechnology6_rivet%maximum_allowable_tension" : [10,3.2],
#             "joiningTechnology4_screw%costs" : [12,1.4],
#             "joiningTechnology4_screw%production_cycle_time" : [14,1.2],
#             "joiningTechnology4_screw%maximum_allowable_tension" : [43,3.2],
#             "joiningTechnology1_welding%costs" : [12,2.4],
#             "joiningTechnology1_welding%production_cycle_time" : [4,1.2],
#             "joiningTechnology1_welding%maximum_allowable_tension" : [54,2.2]   
#             }

    cameoData = {"connection_type_punctual_linear_field" : connection_type_punctual_linear_field, "mixed_compounds_with_thermoplastics_or_pure_metal_compound" : mixed_compounds_with_thermoplastics_or_pure_metal_compound, "post_processing_necessary" : post_processing_necessary, "processing_with_one_sided_access_to_the_joint" : processing_with_one_sided_access_to_the_joint, "removable_connection" : removable_connection, "production_cycle_time" : production_cycle_time, "costs" : costs, "maximum_allowable_tension" : maximum_allowable_tension, "occupational_safety" : occupational_safety, "automatability" : automatability, "dynamic_tension" : dynamic_tension, "environmental_conditions" : environmental_conditions, "weight" : weight, "temperature_resistance" : temperature_resistance}
    
    '''initialize data from Json'''
    
    joiningTechnologiesList = list(data["joiningTechnologies"].keys())
    joiningTechnologiesDict = {}
    
    for i in range (1, len(joiningTechnologiesList)+1):
        name = joiningTechnologiesList[i-1].split("_")[1]
        name = Classes.JoiningTechnology(joiningTechnologiesList[i-1], data)
        joiningTechnologiesDict[joiningTechnologiesList[i-1]] = name
    
    '''initialize data from models'''
    
    #Functions.transferModelParametersToJoiningTechnologies(models, joiningTechnologiesDict)
    #print(joiningTechnologiesDict['joiningTechnology3_glue'].getDataFrame())
    
    '''initialize data from cameo'''
    
    projectPreferences = Classes.ProjectPreferences(cameoData, data)
   
    '''Decision algorithm'''
    #print(joiningTechnologiesDict['joiningTechnology3_glue'].getDataFrame()) 
    #print(projectPreferences.getDataFrame())
    #print(joiningTechnologiesDict['joiningTechnology5_tailor_joints'].getDataFrame())

    
    joiningTechnologiesDict = Functions.getPossibleJoiningTechnologies(joiningTechnologiesList, joiningTechnologiesDict, projectPreferences)

    Functions.deleteBooleansInDataFrames(joiningTechnologiesDict, projectPreferences)
    
    Functions.transferModelParametersToJoiningTechnologies(models, joiningTechnologiesDict)
    
    Functions.scaleParametersValues(joiningTechnologiesDict, projectPreferences)
    
    Functions.scaleCertainParameters(joiningTechnologiesDict)
    
    joiningTechnologiesRating, joiningTechnologiesInformation = Functions.rateJoiningTechnologies(joiningTechnologiesDict, projectPreferences, selectInformation)
    
    '''Solutions'''
    
    MaxDictVal = max( joiningTechnologiesRating, key= joiningTechnologiesRating.get)
    if joiningTechnologiesInformation:
        print("Informationen ueber fehlende Erfuellung von Anforderungen:") 
        print(joiningTechnologiesInformation)
        
    print("------------------------------------------------------------------------------------------------")  
    print("Informationen ueber Schaetzung der Gesamterfuellung aller moeglichen Fuegetechnologien [in %]")
    print(joiningTechnologiesRating)
    print("------------------------------------------------------------------------------------------------")
    print(MaxDictVal + " ist unter den Projektpraeferenzen und Unsicherheitsabschaetzungen")
    print("die optimale Fuegetechnologie fuer den gegebenden Use-Case und erfüllt die Anforderugen zu " + str(joiningTechnologiesRating[MaxDictVal]) + "%")
    