from typing import List, Dict, Union, Tuple, Optional
import math

# Constants based on the problem description
MULTIPLE_OF = 50
WITHDRAW_FEE_PERCENT = 0.015  # 1.5%
WITHDRAW_FEE_MIN = 30
WITHDRAW_FEE_MAX = 600
INTEREST_RATE = 0.03  # 3%
OPERATIONS_FOR_INTEREST = 3
WEALTH_TAX_THRESHOLD = 5_000_000
WEALTH_TAX_RATE = 0.10  # 10%

class ATM:
    """Implements the functionality of an ATM machine."""

    def __init__(self):
        self._balance: float = 0.0
        self._operation_count: int = 0
        self._transaction_log: List[Dict[str, Union[str, float, Optional[str]]]] = []

    def _display_balance(self, action_message: str = "Current"):
        """Displays the current balance."""
        print(f"{action_message} balance: {self._balance:.2f} y.e.")

    def _add_to_transaction_log(self, op_type: str, amount: float, details: Optional[str] = None):
        """Adds an operation to the transaction log."""
        log_entry = {"type": op_type, "amount": amount, "balance_after": self._balance}
        if details:
            log_entry["details"] = details
        self._transaction_log.append(log_entry)

    def _apply_wealth_tax(self) -> None:
        """Applies wealth tax if balance exceeds the threshold."""
        if self._balance > WEALTH_TAX_THRESHOLD:
            # The rule is: "При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией"
            # This means if balance > 5,000,000, a 10% tax on the *current total balance* is deducted.
            # This tax applies before the main operation and even if the subsequent operation might fail.
            actual_tax_amount = self._balance * WEALTH_TAX_RATE
            self._balance -= actual_tax_amount
            print(f"Wealth tax of {actual_tax_amount:.2f} y.e. applied due to balance exceeding {WEALTH_TAX_THRESHOLD} y.e.")
            self._add_to_transaction_log("wealth_tax", actual_tax_amount, f"Balance was {self._balance + actual_tax_amount:.2f} y.e.")
            self._display_balance("Balance after wealth tax")

    def _apply_interest_if_needed(self) -> None:
        """Applies 3% interest after every 3rd operation."""
        if self._operation_count > 0 and self._operation_count % OPERATIONS_FOR_INTEREST == 0:
            interest_earned = self._balance * INTEREST_RATE
            self._balance += interest_earned
            print(f"Interest of {interest_earned:.2f} y.e. (3%) accrued.")
            self._add_to_transaction_log("interest_accrued", interest_earned, f"After {self._operation_count} operations")
            self._display_balance("Balance after interest")

    def _calculate_withdrawal_fee(self, amount: float) -> float:
        """Calculates the fee for a withdrawal operation."""
        fee = amount * WITHDRAW_FEE_PERCENT
        if fee < WITHDRAW_FEE_MIN:
            fee = float(WITHDRAW_FEE_MIN)
        elif fee > WITHDRAW_FEE_MAX:
            fee = float(WITHDRAW_FEE_MAX)
        return round(fee, 2) # Round to 2 decimal places for currency

    def deposit(self, amount: float) -> None:
        """Handles a deposit operation."""
        self._apply_wealth_tax() # Tax check before any operation

        if amount <= 0:
            print("Deposit amount must be positive.")
            self._display_balance("Operation failed, current")
            return
        if amount % MULTIPLE_OF != 0:
            print(f"Deposit amount must be a multiple of {MULTIPLE_OF} y.e.")
            self._display_balance("Operation failed, current")
            return

        self._balance += amount
        self._operation_count += 1
        print(f"Successfully deposited {amount:.2f} y.e.")
        self._add_to_transaction_log("deposit", amount)
        self._apply_interest_if_needed()
        self._display_balance()

    def withdraw(self, amount: float) -> None:
        """Handles a withdrawal operation."""
        self._apply_wealth_tax() # Tax check before any operation

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            self._display_balance("Operation failed, current")
            return
        if amount % MULTIPLE_OF != 0:
            print(f"Withdrawal amount must be a multiple of {MULTIPLE_OF} y.e.")
            self._display_balance("Operation failed, current")
            return

        fee = self._calculate_withdrawal_fee(amount)
        total_deduction = amount + fee

        if total_deduction > self._balance:
            print(f"Insufficient funds. Requested {amount:.2f} + fee {fee:.2f} = {total_deduction:.2f} y.e., but balance is {self._balance:.2f} y.e.")
            self._display_balance("Operation failed, current")
            return

        self._balance -= total_deduction
        self._operation_count += 1
        print(f"Successfully withdrew {amount:.2f} y.e. Fee: {fee:.2f} y.e. Total deducted: {total_deduction:.2f} y.e.")
        self._add_to_transaction_log("withdraw", amount, f"Fee: {fee:.2f}")
        self._apply_interest_if_needed()
        self._display_balance()
    
    def get_transaction_log(self) -> List[Dict[str, Union[str, float, Optional[str]]]]:
        """Returns the transaction log."""
        return self._transaction_log

    def run(self) -> None:
        """Main loop to run the ATM."""
        print("Welcome to the ATM!")
        self._display_balance("Initial")

        while True:
            print("\nChoose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Transaction Log")
            print("4. Exit")
            
            choice = input("Enter choice (1-4): ")

            if choice == '1':
                try:
                    amount_str = input(f"Enter deposit amount (must be a multiple of {MULTIPLE_OF}): ")
                    amount = float(amount_str)
                    self.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    self._display_balance("Operation failed, current")
            elif choice == '2':
                try:
                    amount_str = input(f"Enter withdrawal amount (must be a multiple of {MULTIPLE_OF}): ")
                    amount = float(amount_str)
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    self._display_balance("Operation failed, current")
            elif choice == '3':
                log = self.get_transaction_log()
                if not log:
                    print("Transaction log is empty.")
                else:
                    print("\n--- Transaction Log ---")
                    for entry in log:
                        details = f", Details: {entry['details']}" if 'details' in entry and entry['details'] else ""
                        print(f"Type: {entry['type']}, Amount: {entry['amount']:.2f}, Balance After: {entry['balance_after']:.2f}{details}")
                    print("--- End of Log ---")
                self._display_balance()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                self._display_balance()

if __name__ == "__main__":
    atm_instance = ATM()
    atm_instance.run() 