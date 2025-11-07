# ☕ Coffee Machine - OOP Version

A coffee machine simulator built with Python using Object-Oriented Programming principles. This project demonstrates clean code architecture, modular design, and practical OOP implementation.

## 🎯 Project Overview

This is a refactored version of a procedural coffee machine program, rebuilt using OOP concepts to improve code organization, maintainability, and scalability.

## ✨ Features

- **Menu Management**: Browse available drinks (Espresso, Latte, Cappuccino)
- **Resource Tracking**: Monitor water, milk, and coffee levels
- **Payment Processing**: Accept coins and calculate change
- **Resource Validation**: Check if sufficient ingredients are available
- **Financial Reporting**: Track machine profits
- **Maintenance Mode**: Secret commands for staff (`off`, `report`)

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- Modular design with separate classes

## 📂 Project Structure

```
coffee-machine-oop/
├── main.py              # Main program entry point
├── menu.py              # Menu and MenuItem classes
├── coffee_maker.py      # CoffeeMaker class (resources & brewing)
├── money_machine.py     # MoneyMachine class (payment processing)
└── README.md            # Project documentation
```

## 🏗️ Architecture

The project uses four main classes:

### 1. `MenuItem`
Represents a single drink item with its properties:
- Name
- Cost
- Required ingredients (water, milk, coffee)

### 2. `Menu`
Manages the collection of available drinks:
- Find drinks by name
- Display available options

### 3. `CoffeeMaker`
Handles machine resources and coffee making:
- Check resource availability
- Deduct ingredients
- Generate resource reports

### 4. `MoneyMachine`
Manages all financial transactions:
- Process coin payments
- Calculate change
- Track profits
- Generate financial reports

## 🚀 How to Run

1. Clone this repository
2. Ensure you have Python 3.x installed
3. Run the program:
```bash
python main.py
```

## 💡 Usage

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
```

### Special Commands:
- `report` - Display current resources and money
- `off` - Turn off the machine (maintenance mode)

## 🔄 Differences from Procedural Version

| Aspect | Procedural Version | OOP Version |
|--------|-------------------|-------------|
| **Code Organization** | All logic in one file | Separated into multiple classes |
| **Maintainability** | Hard to modify and extend | Easy to update individual components |
| **Reusability** | Limited code reuse | Classes can be reused in other projects |
| **Readability** | Sequential logic flow | Clear separation of concerns |
| **Testing** | Difficult to test parts individually | Each class can be tested independently |
| **Scalability** | Adding features affects entire code | New features isolated to specific classes |

## 📚 What I Learned

- **OOP Principles**: Encapsulation, abstraction, and separation of concerns
- **Class Design**: Creating cohesive classes with single responsibilities
- **Code Refactoring**: Converting procedural code to object-oriented design
- **Modular Programming**: Building maintainable and scalable applications
- **Python Best Practices**: Using `if __name__ == "__main__"` and docstrings

## 🔗 Related Projects

- [Coffee Machine - Procedural Version](https://github.com/leonardomejiadev-cell/coffee-machine-procedural) - The original implementation using basic Python without OOP

## 👤 Author

**Leonardo Mejia**
- GitHub: [leonardomejiadev-cell](https://github.com/yourusername)
- Learning Journey: 100 Days of Code - Python

## 📝 License

This project is part of my learning journey with Angela Yu's 100 Days of Code course.

## 🙏 Acknowledgments

- Project requirements from Angela Yu's Python Course
- Built as part of Day 16 - Object-Oriented Programming module
