---

# Quintell Bank Management System

Quintell Bank Management System is a Python-based command-line application designed to manage bank accounts efficiently. The system allows users to sign in, sign up, manage their accounts, perform transactions, and check account details. Built with Object-Oriented Programming principles, it provides robust functionality for user management, transactions, and account balance inquiries, along with separate accounts for each user.

## Features

- **User Authentication**: 
  - Sign Up for new users with unique usernames.
  - Sign In for existing users.
  - Username availability check during registration.
- **Account Management**:
  - Balance inquiry for account holders.
  - Cash deposit and withdrawal with real-time balance updates.
  - Fund transfer between accounts.
  - Separate account numbers for each user.
- **Transaction History**:
  - Detailed transaction history for each user account, including date, amount, and transaction type (Credit/Debit).
  - Records for deposits, withdrawals, and transfers.
- **Additional Functionalities**:
  - Database connection for persistent data storage.
  - Date and time-stamped transactions.
  - Error handling for invalid inputs and transactions.

## Technologies Used

- **Python**: Core language for program logic and functionality.
- **MySQL**: Database to store user data, account details, and transaction history.
- **SQLTools**: Used for database and SQL queries.

## Project Structure

The project includes the following key files:

- **`main.py`**: Main script for running the application. It includes options for sign-up, sign-in, and accessing bank facilities.
- **`register.py`**: Handles user registration and authentication.
- **`customer.py`**: Defines the `Customer` class, responsible for user account creation and data storage.
- **`bank.py`**: Defines the `Bank` class, with methods for balance inquiry, deposit, withdrawal, and fund transfer.
- **`databases.py`**: Contains the database connection setup and query execution functions.

## Getting Started

### Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **MySQL**: A MySQL database instance is required.
3. **SQLTools (optional)**: For easier SQL database management.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hamsa-joshua/Quintell-Banking.git 
   ```

2. **Set Up the Database**:
   - Open `databases.py` and configure the MySQL connection with your own MySQL username and password:
     ```python
     mydbs = sql.connect(
         host="localhost",
         user="your_mysql_username",
         password="your_mysql_password",
         database="Bank"
     )
     ```
   - Create the required tables by running `databases.py`.

3. **Run the Application**:
   ```bash
   python main.py
   ```

### Usage

1. **Sign Up**: 
   - Run `main.py`, choose the "Sign Up" option, and provide your details.
2. **Sign In**: 
   - Use your username and password to log in.
3. **Banking Options**:
   - **Balance Enquiry**: Check your current account balance.
   - **Cash Deposit**: Add funds to your account.
   - **Cash Withdraw**: Withdraw funds from your account.
   - **Fund Transfer**: Transfer funds to another account by entering their account number.

## Sample Commands

- **Balance Enquiry**:
  ```
  Enter your choice: 1
  ```

- **Deposit Funds**:
  ```
  Enter your choice: 2
  Enter the amount to deposit: 1000
  ```

- **Withdraw Funds**:
  ```
  Enter your choice: 3
  Enter the amount to withdraw: 500
  ```

- **Fund Transfer**:
  ```
  Enter your choice: 4
  Enter the receiver's account number: 87654321
  Enter the amount to transfer: 200
  ```
  
## Troubleshooting

- **Database Connection Issues**: Ensure that MySQL is running and your credentials are correctly set in `databases.py`.
- **Invalid Inputs**: The program currently handles most incorrect inputs with prompts; ensure that numeric values are entered where expected.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to propose changes or report bugs.

## License

This project is licensed under the MIT License.

---
