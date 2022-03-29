# University Assignment COSC110: Programming Assignment 1 - Vaccination Phases

### The challenge

Users should be able to:

- Through a series of questions determine in which phase the user will be given access to a vaccine.

Groups in each Phase of vaccine rollout:

- 1a: Quarantine and border workers; Frontline health care worker sub-groups for prioritisation; Aged care and disability care staff; Aged care and disability care residents
- 1b: Elderly adults aged 80 years and over; Elderly adults aged 70-79 years; Other health care workers; Aboriginal and Torres Strait Islander people > 55; Younger adults with an underlying medical condition, including those with a disability; Critical and high risk workers including defence, police, fire, emergency services and meat processing
- 2a: Adults aged 60-69 years; Adults aged 50-59 years; Aboriginal and Torres Strait Islander people 18-54; Other critical and high risk workers
- 2b: Balance of adult population; Catch up any unvaccinated Australians from previous phases
- 3: < 18 if recommended (Pfizer vaccine only)

### How to run this program

1. Ensure you have the file download locally and can be accessed via your terminal.
2. To start the program type in the terminal: python3 vaccination_phase.py
3. You will now answer a question or a series of questions to determine your phase group allocation
4. A print out statement will appear when the program determines you eligibility

### My process

3 functions were used:
    - Yes or No input validation: this ensures the user can only enter yes, y, Y, no, n or N.
    - Age input validation: this ensures the user can only enter a positive integer for the age value
    - Main function: the main component of the program, where users will be asked a series of questions

# yes_or_no_input:
- The user can only input what is in the array of yesResponse or noResponse
- A TypeError or a ValueError appears if the user does not input the valid values
- While loops are used for each question/input, if the input is invalid an error message occurs (yesNoError) and the user is prompted to answer correctly

# age_input:
- The user can only input a positive integer
- A TypeError or a ValueError appears if the user does not input the valid values
- A while loop is used for the age input, if the input is invalid an error message occurs (yesNoError) and the user is prompted to answer correctly with a positive integer

# main:
- The user is asked a series of questions to determine their phase allocation
- Nested with several if, elif and else statements which helps determine the users eligibility

### Built with

- Python
# vaccination-phases
