# Intialisation
groups = ['1a', '1b', '2a', '2b', '3']
yesResponse = ['yes', 'Yes', 'Y', 'y']
noResponse = ['no', 'No', 'N', 'n']
phaseAllocation = 'Vaccines will be made available to you in Phase '
yesNoError = "Please enter either 'Y' for 'Yes' or 'N' for 'No'"

# Allow the user to only input yes or no
def yes_or_no_input(choice):
  if choice in yesResponse or choice in noResponse:
    return True
  try:
    choice = str(choice)
  except (TypeError, ValueError):
    return False

# Allow the user to only input a positive integer
def age_input(value):
  if not isinstance(value, (str, int)):
    return False
  try:
    value = int(value)
  except (TypeError, ValueError):
    return False
  return value > 0         

# Main eligibility criteria to determine phase for user
def main():
    # Determine if user is high priority
    highPriority = input("Are you a quarantine and border worker, prioritised frontline healthcare worker, or an aged care/disability care staff member or resident (Y/N)? ")
    while not yes_or_no_input(highPriority):
        print(yesNoError)
        highPriority = input("Are you a quarantine and border worker, prioritised frontline healthcare worker, or an aged care/disability care staff member or resident (Y/N)? ")
    
    # Phase 1a allocation if user is high priority
    if highPriority in yesResponse:
            print((phaseAllocation) + str(groups[0]))
    
    elif highPriority in noResponse:
            # Determine if user is a front line worker
            frontLine = input("Are you a health care worker or a critical or high risk worker (including defence, police, fire, emergency services and meat processing)? (Y/N) ")
            while not yes_or_no_input(frontLine):
                print(yesNoError)
                frontLine = input("Are you a health care worker or a critical or high risk worker (including defence, police, fire, emergency services and meat processing)? (Y/N) ")
            
            # Phase 1b allocation if front line
            if frontLine in yesResponse:
                print((phaseAllocation) + str(groups[1]))

            # If user is not high priority or front line then determine age
            else:
                age = (input("How old are you? Enter you age in years. "))
                while not age_input(age):
                    print("Please enter a non-negative integer") 
                    age = (input("How old are you? Enter you age in years. "))
                age = int(age)       

                # If user is under 18, determine if a critical worker and/or recommended vaccine
                if (age < 18):
                    otherCritical = input("Are you an other critical or high risk worker? (Y/N) ")
                    while not yes_or_no_input(otherCritical):
                        print(yesNoError) 
                        otherCritical = input("Are you an other critical or high risk worker? (Y/N) ")
                    
                    # Phase 2a allocation if other critical workers
                    if otherCritical in yesResponse:
                        print((phaseAllocation) + str(groups[2]))

                    elif otherCritical in noResponse: 
                        # Determine if user is under 18  
                        underageRecommendation = input("Have you been recommended the vaccination by a doctor? (Y/N) ")
                        while not yes_or_no_input(underageRecommendation):
                            print(yesNoError)
                            underageRecommendation = input("Have you been recommended the vaccination by a doctor? (Y/N) ")
                        
                        # Phase 3 allocation if underage user is doctor recommended
                        if underageRecommendation in yesResponse:
                            print((phaseAllocation) + str(groups[4]))

                        # Vaccine not recommended if underage user does not meet any criteria
                        else:
                            print("Vaccination is not recommended for you")
                
                # Phase 1b allocation if user is over 70
                else: 
                    if (age >= 70):
                        print((phaseAllocation) + str(groups[1]))
                                
                    # If user is between 18 and 69 then determine phase group            
                    else:
                        if (age >= 18 and age <= 69):
                                    # Determine if user has a medical background
                                    medicalBackground = input("Do you have an underlying medical condition, including those with a disability (Y/N)? ")
                                    while not yes_or_no_input(medicalBackground):
                                        print(yesNoError) 
                                        medicalBackground = input("Do you have an underlying medical condition, including those with a disability (Y/N)? ")
                                    
                                    # Phase 1b allocation if user is between 18 - 69 and has medical condition
                                    if medicalBackground in yesResponse:
                                        print((phaseAllocation) + (groups[1]))
                  
                                    else:
                                        if medicalBackground in noResponse and (age >= 18 and age <= 59):
                                                # Determine if user is other critical worker between 18 - 59 years old
                                                otherCritical = input("Are you an other critical or high risk worker? (Y/N) ")
                                                while not yes_or_no_input(otherCritical):
                                                    print(yesNoError) 
                                                    otherCritical = input("Are you an other critical or high risk worker? (Y/N) ")
                                                
                                                # Phase 2a allocation if user is between 18 - 69 and other critical worker
                                                if otherCritical in yesResponse:
                                                    print((phaseAllocation) + str(groups[2]))

                                                elif otherCritical in noResponse and (age >= 18 and age <= 54):
                                                    # Determine if user is an Aboriginal or Torres Strait Islander between 18 - 54 years old
                                                    aboriginalOrTorresStrait = input("Do you identify as an Aboriginal and/or Torres Strait Islander person. (Y/N)? ")
                                                    while not yes_or_no_input(aboriginalOrTorresStrait):
                                                        print(yesNoError)
                                                        aboriginalOrTorresStrait = input("Do you identify as an Aboriginal and/or Torres Strait Islander person. (Y/N)? ")
                                                    
                                                    # Phase 2a allocation if user is between 18 - 69 and Aboriginal and/or Torres Strait Islander
                                                    if aboriginalOrTorresStrait in yesResponse:
                                                        print((phaseAllocation) + (groups[2])) 
                                                    
                                                    # Phase 2b allocation if user is not Aboriginal and/or Torres Strait Islander
                                                    else: 
                                                        print((phaseAllocation) + str(groups[3]))

                                                # Phase 2b allocation if above conditions not met     
                                                else:
                                                    print((phaseAllocation) + str(groups[3]))


                                        elif medicalBackground in noResponse and (age >= 55):
                                            # Determine if user is an Aboriginal or Torres Strait Islander over 55 years old
                                            aboriginalOrTorresStrait = input("Do you identify as an Aboriginal and/or Torres Strait Islander person. (Y/N)? ")
                                            while not yes_or_no_input(aboriginalOrTorresStrait):
                                                print(yesNoError)
                                                aboriginalOrTorresStrait = input("Do you identify as an Aboriginal and/or Torres Strait Islander person. (Y/N)? ")  
                                            
                                            # Phase 1b allocation if user has no medical background, is an Aboriginal and/or Torres Strait Islander and 55 or over 
                                            if aboriginalOrTorresStrait in yesResponse and (age >= 55):
                                                print((phaseAllocation) + (groups[1]))

                                        # Phase 2a allocation if no medical background, is not an Aboriginal and/or Torres Strait Islander and under 55                        
                                        else:
                                            print((phaseAllocation) + (groups[2]))

    # Phase 2b allocation if all conditions are not met                                                   
    else:
        print((phaseAllocation) + (groups[3]))
                                                
# Run the main function
if __name__ == "__main__":
    main()                 


