fertilizer_composition = {
    "Urea": {"N": 46},
    "DAP": {"N": 18, "P": 46},
    "MOP": {"K": 60},
    "Zinc Sulphate": {"Zn": 21},
    "Sulphur": {"S": 90},
}

fertilizer_recommendations = {
    "paddy": {
        "germination": {"N": 10, "P": 20, "K": 5, "Zn": 50},
        "tillering_initiation": {},
        "tillering": {"N": 15, "K": 5},
        "panicle": {"N": 15, "K": 5},
        "flowering": {},
        "milking": {"N": 15, "K": 5},
        "dough": {},
        "harvesting": {},
        # Add other stages as per your requirement
    },
    "maize": {
        "germination": {"N": 15, "P": 25, "K": 15, "Zn": 15},
        "vegetative": {"N":15},
        "flowering": {"N":15},
        # Add other stages as per your requirement
    },
    # Add recommendations for other crops here
}

crop_duration_days = {
    "paddy": {
        "germination": {"days_range": (0, 25)},
        "tillering_initiation": {"days_range": (26, 30)},
        "tillering": {"days_range": (31, 40)},
        "panicle": {"days_range": (41, 70)},
        "flowering": {"days_range": (71, 115)},
        "milking": {"days_range": (125, 135)},
        "dough": {"days_range": (150, 170)},
        "harvesting": {"days_range": (170, 200)},
    },
    "maize": {
        "germination": {"days_range": (0, 15)},
        "vegetative": {"days_range": (16, 40)},
        "flowering": {"days_range": (41, 65)},
        "cob development": {"days_range": (66, 99)},
        "harvesting": {"days_range": (100, 135)},
    },
    # Add recommendations for other crops here
}
def get_growth_stage(crop, days):
    for stage, duration in crop_duration_days.get(crop, {}).items():
        if duration["days_range"][0] <= days <= duration["days_range"][1]:
            return stage
    return "No stage found for this duration."

def calculate_fertilizer_requirements(crop, days, acres):
    stage = get_growth_stage(crop, days)
    if stage == "No stage found for this duration.":
        return stage

    recommendations = fertilizer_recommendations.get(crop, {}).get(stage, {})
    if not recommendations:
        return "No recommendations available for this stage or crop."

    fertilizer_amounts = {}
    dap_required = False

    # Check if both N and P are required
    if 'N' in recommendations and 'P' in recommendations:
        dap_required = True

    for fertilizer, composition in fertilizer_composition.items():
        fertilizer_amounts[fertilizer] = {}
        for nutrient, value in composition.items():
            if nutrient in recommendations:
                required_amount = (recommendations[nutrient] * acres)

                if dap_required and nutrient == 'P' and fertilizer == 'DAP':
                    dap_amount = round(required_amount / value * 100, 2)
                    dap_nitrogen = composition.get('N', 0) * dap_amount / 100
                    remaining_nitrogen = recommendations['N'] * acres - dap_nitrogen

                    #urea_amount = round((remaining_nitrogen * acres) / (fertilizer_composition['Urea']['N'] / 100), 2)
                    urea_amount = round((remaining_nitrogen) / (fertilizer_composition['Urea']['N'] / 100), 2)
                    fertilizer_amounts['DAP']['P'] = dap_amount
                    fertilizer_amounts['Urea']['N'] = urea_amount
                else:
                    fertilizer_amounts[fertilizer][nutrient] = round(required_amount / value * 100, 2)

    urea_amount = fertilizer_amounts.get("Urea", {}).get("N", 0)
    dap_amount = fertilizer_amounts.get("DAP", {}).get("P", 0)
    mop_amount = fertilizer_amounts.get("MOP", {}).get("K", 0)
    zn_amount = fertilizer_amounts.get("Zinc Sulphate", {}).get("Zn", 0)

    #return f"For {crop} in {stage} stage: DAP: {dap_amount} kg, Urea: {urea_amount} kg, MOP: {mop_amount} kg, Zinc Sulphate: {zn_amount} kg"
    return f"For {crop} in {stage} stage: DAP: {round(dap_amount)} kg, Urea: {round(urea_amount)} kg, MOP: {round(mop_amount)} kg, Zinc Sulphate: {round(zn_amount)} kg"


# Taking user inputs2

crop_name = input("Enter crop name: ")
days = int(input("Enter number of days: "))
acres = float(input("Enter number of acres: "))

result = calculate_fertilizer_requirements(crop_name, days, acres)
print(result)
