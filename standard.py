crop_nutrient_requirements = {
    "Maize": {"N": 50, "P": 25, "K": 20, "Zn": 2},
    "Paddy": {"N": 50, "P": 25, "K": 25, "Zn": 3},
    "Wheat": {"N": 35, "P": 25, "K": 20, "Zn": 2.5},
    "Groundnut": {"N": 10, "P": 25, "K": 20, "Zn": 2},
    "Cotton": {"N": 50, "P": 25, "K": 25, "Zn": 3.5},

    
}


fertilizer_composition = {
    "Urea": {"N": 46},
    "DAP": {"N": 18, "P": 46},
    "MOP": {"K": 60},
    "Zinc Sulphate": {"Zn": 21},
    
}


crop = input("Enter the crop name: ")
area = float(input("Enter the cultivation area (in acres): "))

if crop in crop_nutrient_requirements:
    crop_requirements = crop_nutrient_requirements[crop]

    
    phosphorus_needed = crop_requirements["P"]
    dap_needed = (phosphorus_needed * area / fertilizer_composition["DAP"]["P"]) * 100
    nitrogen_in_dap = (dap_needed / 100) * fertilizer_composition["DAP"]["N"]
    remaining_nitrogen = crop_requirements["N"] * area - nitrogen_in_dap
    urea_needed = (remaining_nitrogen / fertilizer_composition["Urea"]["N"]) * 100

    
    potassium_needed = crop_requirements["K"]
    mop_needed = (potassium_needed * area/ 60) * 100

    
    zinc_needed = crop_requirements["Zn"]
    zinc_sulphate_needed = (zinc_needed * area / 21) * 100

    print(f"Recommended Fertilizer Composition for {crop} on {area} acres:")
    print(f"DAP: {round(dap_needed )} kg")
    print(f"Urea: {round(urea_needed )} kg")
    print(f"MOP: {round(mop_needed )} kg")
    print(f"Zinc Sulphate: {round(zinc_sulphate_needed )} kg")
else:
    print("Crop not found in the database. Please add its nutrient requirements.")

