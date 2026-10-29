# Problem Statement
Develop a Python program for a Password Policy Validation Engine that evaluates sample password strings against a set of predefined password security requirements. The program should check whether each password meets the minimum length requirement, contains uppercase and lowercase letters, includes at least one digit and a special character, avoids excessive consecutive character repetition, and does not contain prohibited substrings. The program should identify all failed conditions for each password and display a clear explanation of each failure. Finally, it should classify each password as valid or invalid according to the specified policy.
# Algorithm
1. Start the program.
2. Define the password policy rules.
3. Define a list of prohibited substrings.
4. Input the number of passwords to be evaluated.
5. For each password:
   - Read the password string.
   - Check whether its length is at least 8 characters.
   - Check for at least one uppercase letter.
   - Check for at least one lowercase letter.
   - Check for at least one digit.
   - Check for at least one special character.
   - Check whether any character appears consecutively three or more times.
   - Check whether the password contains any prohibited substring.
6. Record every failed condition.
7. If no conditions fail, classify the password as valid.
8. Otherwise, classify the password as invalid and display the reasons.
9. Repeat the process for all passwords.
10. Stop the program.
11. ```mermaid flowchart
    flowchart TD
    A([Start]) --> B[Define password policy rules]
    B --> C[/Enter number of passwords/]
    C --> D[/Enter a password/]
    D --> E[Initialize failed conditions list]
    E --> F{Length at least 8?}
    F -- No --> G[Add length error]
    F -- Yes --> H[Check character categories]
    G --> H
    H --> I[Check uppercase, lowercase, digit and special character]
    I --> J[Check consecutive character repetition]
    J --> K[Check prohibited substrings]
    K --> L{Any failed conditions?}
    L -- Yes --> M[Display Invalid and explain failures]
    L -- No --> N[Display Valid]
    M --> O{More passwords?}
    N --> O
    O -- Yes --> D
    O -- No --> P([Stop])
    ```
# Sample Input
For this example, we will test four passwords against the predefined rules.
PASSWORD POLICY VALIDATION ENGINE
Enter number of passwords to check: 4

Enter password 1: Hello@123

Enter password 2: abc

Enter password 3: ADMIN@123

Enter password 4: Abccc@12

# Sample Output
Password 1 Validation Result:
Status: VALID
All password policy rules are satisfied.

Password 2 Validation Result:
Status: INVALID
Failed Conditions:
- Password must contain at least 8 characters.
- Password must contain an uppercase letter.
- Password must contain at least one digit.
- Password must contain a special character.

Password 3 Validation Result:
Status: INVALID
Failed Conditions:
- Password must contain a lowercase letter.
- Password must not contain the prohibited substring 'admin'.

Password 4 Validation Result:
Status: INVALID
Failed Conditions:
- Password must not contain the same character 3 or more times consecutively.
- Password validation completed.
- 
