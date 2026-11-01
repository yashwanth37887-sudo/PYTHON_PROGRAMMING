1. Problem Statement
Develop a Python program to validate student email-like strings and registration identifiers based on predefined formatting rules.

The program should identify and report the following errors:
1. Missing username or domain in an email address.
2. Invalid characters in the email username or domain.
3. Malformed separators such as multiple dots or misplaced @ symbols.
4. Missing components in a registration identifier.
5. Invalid character groups in the registration identifier.
6. Incorrect registration identifier format.
The program displays whether the entered student email and registration identifier are valid or invalid, along with the corresponding error messages.
2. Algorithm
Step 1: Start the program.

Step 2: Read the student email address from the user.

Step 3: Read the student registration identifier.

Step 4: Validate the email address:
- Check whether the @ symbol is present exactly once.
- Check whether the username is present.
- Check whether the domain is present.
- Check for invalid characters.
- Check whether the domain contains a valid extension.
- Check for malformed separators.
Step 5: Validate the registration identifier:
- Check whether all required components are present.
- Check whether the identifier follows the specified format.
- Check for invalid characters.
Step 6: Display the validation results and error messages.
Step 7: Stop the program.
folwchart:(mermaid):

flowchart TD
    A([START]) --> B[/Enter Student Email/]
    B --> C[/Enter Registration ID/]
    C --> D{Validate Email}
    D --> E{Email Format Correct?}
    E -- No --> F[Display Email Errors]
    E -- Yes --> G[Display Valid Email]
    F --> H{Validate Registration ID}
    G --> H
    H --> I{ID Format Correct?}
    I -- No --> J[Display ID Errors]
    I -- Yes --> K[Display Valid ID]
    J --> L[Display Final Results]
    K --> L
    L --> M([STOP])

 
5. Sample Input
STUDENT EMAIL AND IDENTIFIER VALIDATION
---------------------------------------
Enter Student Email: student123@gmail.com
Enter Registration ID: STU-2026-1234


6. Sample Output
EMAIL VALIDATION
Valid

Valid Email



REGISTRATION ID VALIDATION
Valid

Valid Registration ID



Validation Completed

7. Sample Input with Errors
Enter Student Email: student@@gmail
Enter Registration ID: STU-AB-123


8. Sample Output with Errors
EMAIL VALIDATION:
Invalid Email
- Invalid or missing @ separator

REGISTRATION ID VALIDATION:
Invalid Registration ID
- Invalid registration ID format
- Invalid year character group

VALIDATION COMPLETED


9. Result
Thus, the Python program for Student Email and Identifier Validation was successfully developed and executed.

The program checks email addresses and student registration identifiers using regular expressions and conditional statements. It identifies malformed separators, invalid character groups, and missing components and displays appropriate validation messages.

Note: The email and registration ID rules used here are example formatting rules. They can be modified according to your college's actual student registration format.
