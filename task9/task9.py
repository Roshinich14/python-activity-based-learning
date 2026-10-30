print("MULTI-STAGE ATM TRANSACTION AUDIT")
print("----------------------------------")

# Initialize bank accounts
accounts = {
    "A101": 0.0,
    "A102": 0.0
}

# Enter initial balances
for account in accounts:
    while True:
        try:
            balance = float(
                input("Enter initial balance for " + account + ": ")
            )

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                accounts[account] = round(balance, 2)
                break

        except ValueError:
            print("Please enter a valid numeric balance.")

# Initialize audit details
audit_log = []
suspicious_patterns = []
invalid_count = 0
consecutive_failures = 0

# Track consecutive withdrawals
last_withdrawal_account = None
last_withdrawal_amount = None
withdrawal_streak = 0

# Get number of transactions
while True:
    try:
        n = int(input("Enter number of transactions: "))

        if n < 0:
            print("Number of transactions cannot be negative.")
        else:
            break

    except ValueError:
        print("Enter a valid whole number.")


def record_transaction(transaction_number, details, status):
    """Store transaction details in the audit log."""
    audit_log.append({
        "number": transaction_number,
        "details": details,
        "status": status
    })


# Process each transaction
for i in range(1, n + 1):
    print("\nTransaction", i)
    print("D - Deposit")
    print("W - Withdrawal")
    print("T - Transfer")

    transaction_type = input(
        "Enter transaction type (D/W/T): "
    ).strip().upper()

    details = ""
    status = "FAILED"
    successful_withdrawal = False
    source_account = None
    amount = 0.0

    try:
        if transaction_type == "D":
            destination = input(
                "Enter account to deposit into: "
            ).strip().upper()

            amount = float(input("Enter deposit amount: "))

            if destination not in accounts:
                details = "Deposit to invalid account"
            elif amount <= 0:
                details = "Invalid deposit amount"
            else:
                accounts[destination] = round(
                    accounts[destination] + amount, 2
                )
                details = (
                    "Deposit of Rs. " + str(round(amount, 2))
                    + " into " + destination
                )
                status = "SUCCESS"

        elif transaction_type == "W":
            source_account = input(
                "Enter account to withdraw from: "
            ).strip().upper()

            amount = float(input("Enter withdrawal amount: "))

            if source_account not in accounts:
                details = "Withdrawal from invalid account"
            elif amount <= 0:
                details = "Invalid withdrawal amount"
            elif accounts[source_account] < amount:
                details = "Withdrawal failed: insufficient balance"
            else:
                accounts[source_account] = round(
                    accounts[source_account] - amount, 2
                )
                details = (
                    "Withdrawal of Rs. " + str(round(amount, 2))
                    + " from " + source_account
                )
                status = "SUCCESS"
                successful_withdrawal = True

        elif transaction_type == "T":
            source_account = input(
                "Enter source account: "
            ).strip().upper()

            destination = input(
                "Enter destination account: "
            ).strip().upper()

            amount = float(input("Enter transfer amount: "))

            if source_account not in accounts:
                details = "Transfer failed: invalid source account"
            elif destination not in accounts:
                details = "Transfer failed: invalid destination account"
            elif source_account == destination:
                details = "Transfer failed: accounts must be different"
            elif amount <= 0:
                details = "Transfer failed: invalid amount"
            elif accounts[source_account] < amount:
                details = "Transfer failed: insufficient balance"
            else:
                accounts[source_account] = round(
                    accounts[source_account] - amount, 2
                )
                accounts[destination] = round(
                    accounts[destination] + amount, 2
                )

                details = (
                    "Transfer of Rs. " + str(round(amount, 2))
                    + " from " + source_account
                    + " to " + destination
                )
                status = "SUCCESS"

        else:
            details = "Invalid transaction type"

    except ValueError:
        details = "Invalid numeric input"

    # Update failure tracking
    if status == "FAILED":
        invalid_count += 1
        consecutive_failures += 1

        if consecutive_failures == 3:
            suspicious_patterns.append(
                "Three or more consecutive failed transactions "
                "ending at transaction " + str(i)
            )
    else:
        consecutive_failures = 0

    # Detect repeated consecutive withdrawals
    if successful_withdrawal:
        if (
            source_account == last_withdrawal_account
            and round(amount, 2) == last_withdrawal_amount
        ):
            withdrawal_streak += 1
        else:
            withdrawal_streak = 1

        last_withdrawal_account = source_account
        last_withdrawal_amount = round(amount, 2)

        if withdrawal_streak == 3:
            suspicious_patterns.append(
                "Three consecutive withdrawals of Rs. "
                + str(round(amount, 2))
                + " from " + source_account
                + ", ending at transaction " + str(i)
            )
    else:
        # A different transaction breaks the withdrawal streak
        last_withdrawal_account = None
        last_withdrawal_amount = None
        withdrawal_streak = 0

    record_transaction(i, details, status)

    print("Transaction status:", status)
    print("Details:", details)


# Display transaction audit report
print("\n========== ATM AUDIT REPORT ==========")

print("\nTRANSACTION HISTORY")
for entry in audit_log:
    print(
        "Transaction", entry["number"], "|",
        entry["details"], "|",
        "Status:", entry["status"]
    )

# Display final account balances
print("\nFINAL ACCOUNT BALANCES")
for account, balance in accounts.items():
    print(account, ": Rs.", format(balance, ".2f"))

# Display invalid transaction count
print("\nTotal failed transactions:", invalid_count)

# Display suspicious patterns
print("\nSUSPICIOUS ACTIVITY REPORT")

if suspicious_patterns:
    for pattern in suspicious_patterns:
        print("-", pattern)
else:
    print("No suspicious repeated patterns detected.")

print("\nATM transaction audit completed.")
