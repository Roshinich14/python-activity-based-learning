# Problem Statement
The Multi-Stage ATM Transaction Audit system simulates banking transactions involving deposits, withdrawals, and transfers between accounts. It maintains account balances after each transaction, detects invalid operations such as insufficient funds or non-positive transaction amounts, and identifies suspicious repeated patterns. For example, multiple withdrawals of the same amount or several failed transactions within a short sequence can be flagged for review. The system generates a transaction audit report showing transaction details, updated balances, invalid operations, and suspicious activity.
# Objectives
1. To simulate deposits, withdrawals, and transfers between bank accounts.
2. To maintain accurate account balances after each transaction.
3. To validate transaction amounts and account details.
4. To detect invalid transactions, including withdrawals exceeding available balances.
5. To identify suspicious repeated transaction patterns.
6. To generate a final audit report containing transaction statuses and account balances.
# Assumptions
1. The system begins with two simulated bank accounts: A101 and A102.
2. Both accounts have an initial balance entered by the user.
3. Supported transactions are deposits, withdrawals, and transfers.
4. Transaction amounts must be positive.
5. Withdrawals and transfers are rejected if the source account has insufficient funds.
6. Transfers require two different, registered accounts.
7. A transaction is considered suspicious if:
   - Three or more consecutive withdrawals from the same account have the same amount.
   - Three or more consecutive failed transactions occur.
8. Suspicious transactions are flagged for review; the system does not automatically conclude that fraud has occurred.
9. All transactions are simulated. No real bank account or payment service is connected.
# Algorithm
1. Start the program.
2. Create two bank accounts and input their initial balances.
3. Initialize the transaction history, invalid transaction counter, and suspicious activity counters.
4. Input the number of transactions to process.
5. For each transaction:
   - Read the transaction type: deposit, withdrawal, or transfer.
   - Read the relevant account details and transaction amount.
   - Validate the account numbers and transaction amount.
   - For a deposit, add the amount to the destination account.
   - For a withdrawal, check the available balance before deducting the amount.
   - For a transfer, check the source balance and destination account before updating both balances.
   - Record whether the transaction succeeded or failed.
6. Track consecutive withdrawals of the same amount from the same account.
7. Detect three or more consecutive failed transactions.
 ```mermaid flowchart
   flowchart TD
    A([Start]) --> B[Initialize bank accounts]
    B --> C[Enter initial balances]
    C --> D[Enter number of transactions]
    D --> E[Enter transaction type and details]
    E --> F{Is transaction valid?}
    F -- No --> G[Record failed transaction]
    G --> H[Update failed transaction counter]
    F -- Yes --> I{Transaction type?}
    I -- Deposit --> J[Add amount to account]
    I -- Withdrawal --> K{Sufficient balance?}
    I -- Transfer --> L{Valid destination and sufficient balance?}
    K -- No --> G
    L -- No --> G
    K -- Yes --> M[Deduct withdrawal amount]
    L -- Yes --> N[Update source and destination balances]
    J --> O[Record successful transaction]
    M --> O
    N --> O
    O --> P[Check repeated transaction patterns]
    P --> Q{More transactions?}
    Q -- Yes --> E
    Q -- No --> R[Generate audit report]
    R --> S[Display final balances and suspicious activity]
    S --> T([Stop])
   ```
# Sample Input
Use the following values to test the program.
Enter initial balance for A101: 1000
Enter initial balance for A102: 500
Enter number of transactions: 7
# Sample Output
The following is a shortened illustration of the audit report produced by the program.
========== ATM AUDIT REPORT ==========

TRANSACTION HISTORY
Transaction 1 | Deposit of Rs. 200.0 into A101 | Status: SUCCESS
Transaction 2 | Withdrawal of Rs. 100.0 from A101 | Status: SUCCESS
Transaction 3 | Withdrawal of Rs. 100.0 from A101 | Status: SUCCESS
Transaction 4 | Withdrawal of Rs. 100.0 from A101 | Status: SUCCESS
Transaction 5 | Withdrawal failed: insufficient balance | Status: FAILED
Transaction 6 | Withdrawal from invalid account | Status: FAILED
Transaction 7 | Transfer failed: accounts must be different | Status: FAILED

FINAL ACCOUNT BALANCES
A101 : Rs. 900.00
A102 : Rs. 500.00

Total failed transactions: 3

SUSPICIOUS ACTIVITY REPORT
- Three consecutive withdrawals of Rs. 100.0 from A101, ending at transaction 4
- Three or more consecutive failed transactions ending at transaction 7

ATM transaction audit completed.

9. Flag suspicious patterns for review.
10. Display the transaction audit log and final account balances.
11. Stop the program.
