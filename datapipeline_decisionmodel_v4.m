function feedbackOfDecisionAlgorithm = datapipeline_decisionmodel_v4(costs, max_allowable_tension, production_cycle_time, automatability, enviromental_conditions, dynamic_tension, occupational_sefety, weight, temperature_resistance, mixed_compounds_with_thermoplastics, pure_metal_compound, post_processing_necessary, processing_with_one_sided_access_to_the_joint, connection_type_punctual, connection_type_linear, connection_type_field, select_Information, costs_TailoredJoints, cycle_TailoredJoints, stress_TailoredJoints, costs_AdhensiveBonding, cycle_AdhensiveBonding, stress_AdhensiveBonding, costs_Soldering, cycle_Soldering, stress_Soldering, costs_Rivet, cycle_Rivet, stress_Rivet, costs_Screws, cycle_Screws, stress_Screws, costs_Welding, cycle_Welding, stress_Welding, removable_connection)

commandStr =['pushd "C:\ProgramData\Anaconda3\Scripts" & activate.bat Jonas & pushd "\\mse-files6.ime.rwth-aachen.de\MSE-Transfer01$\julius.berges\HiWi TailoredJoints\8 Systemmodell\Entscheidungsmodell" & python Main.py ',num2str(costs),' ',num2str(max_allowable_tension),' ',num2str(production_cycle_time),' ',automatability,' ',enviromental_conditions,' ',dynamic_tension,' ',occupational_sefety,' ',weight,' ',temperature_resistance,' ',mixed_compounds_with_thermoplastics,' ',pure_metal_compound,' ',post_processing_necessary,' ',processing_with_one_sided_access_to_the_joint,' ',connection_type_punctual,' ',connection_type_linear,' ',connection_type_field,' ',select_Information,' ',num2str(costs_TailoredJoints(1)),' ',num2str(costs_TailoredJoints(2)), ' ',num2str(cycle_TailoredJoints(1)),' ',num2str(cycle_TailoredJoints(2)), ' ',num2str(stress_TailoredJoints(1)),' ',num2str(stress_TailoredJoints(2)),' ',num2str(costs_AdhensiveBonding(1)),' ',num2str(costs_AdhensiveBonding(2)), ' ',num2str(cycle_AdhensiveBonding(1)),' ',num2str(cycle_AdhensiveBonding(2)), ' ',num2str(stress_AdhensiveBonding(1)),' ',num2str(stress_AdhensiveBonding(2)),' ',num2str(costs_Soldering(1)),' ',num2str(costs_Soldering(2)), ' ',num2str(cycle_Soldering(1)),' ',num2str(cycle_Soldering(2)), ' ',num2str(stress_Soldering(1)),' ',num2str(stress_Soldering(2)),' ',num2str(costs_Rivet(1)),' ',num2str(costs_Rivet(2)), ' ',num2str(cycle_Rivet(1)),' ',num2str(cycle_Rivet(2)), ' ',num2str(stress_Rivet(1)),' ',num2str(stress_Rivet(2)),' ',num2str(costs_Screws(1)),' ',num2str(costs_Screws(2)), ' ',num2str(cycle_Screws(1)),' ',num2str(cycle_Screws(2)), ' ',num2str(stress_Screws(1)),' ',num2str(stress_Screws(2)),' ',num2str(costs_Welding(1)),' ',num2str(costs_Welding(2)), ' ',num2str(cycle_Welding(1)),' ',num2str(cycle_Welding(2)), ' ',num2str(stress_Welding(1)),' ',num2str(stress_Welding(2)),' ',removable_connection];

[status, commandOut] = system(commandStr);
    
    if status~=0
       disp("Failed to call decision script in Python");
    end
    
    feedbackOfDecisionAlgorithm = (commandOut);
    
out = [feedbackOfDecisionAlgorithm];

end