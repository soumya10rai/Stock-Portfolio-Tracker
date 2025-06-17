# Stock-Portfolio-Tracker

The Stock Portfolio Tracker is a beginner-friendly Python project designed to help users calculate the total value of their stock investments. It is a simple command-line tool that asks the user to input the name of a stock they own and the quantity they have invested in. Using a predefined dictionary of stock prices, the program calculates the total investment value and optionally saves this information to a text file.

The core functionality begins with the user providing the stock symbol (such as "AAPL" for Apple or "TSLA" for Tesla) and the number of shares they own. The program then checks whether the stock symbol exists in its dictionary of stock prices. If found, it retrieves the corresponding price and multiplies it by the quantity to get the total investment amount. This value is then displayed on the screen in a readable format.

To enhance usability, the program also includes file handling capabilities. Once the total investment is calculated, it writes the results—including the stock name, quantity, and total value—into a text file named portfolio.txt. This ensures that the user has a saved record of their investment, which they can refer to later. If the user enters a stock name that is not in the dictionary, the program gracefully informs them that the stock is not found in the database.

This project uses basic Python concepts such as variables, input/output, conditionals (if-else), dictionaries, and file handling. It is a great exercise for beginners to practice working with user inputs, simple arithmetic operations, and file writing. The program also helps build confidence in writing clean, structured Python code and understanding how to manage data using built-in data structures.

Overall, the Stock Portfolio Tracker is a practical and educational mini-project that introduces essential programming concepts while providing a useful real-world application. It can easily be extended in the future by incorporating features like fetching real-time stock prices from an API, allowing multiple stock entries, or exporting the data to a CSV file.
