#include <iostream> //# Importing the iostream standard library

//@ cette fonction Function declaration
void greetUser(const std::string& name);

//@ cette class A simple C++ class
class Example {
public:
    //# Constructor
    Example() {
        std::cout << "Example class constructor called." << std::endl;
    }

    //# Destructor
    ~Example() {
        std::cout << "Example class destructor called." << std::endl;
    }

    //# Member function
    void displayMessage() {
        std::cout << "Welcome to C++ programming!" << std::endl;
    }
};

//@ cette fonction Main function, entry point of the program
int main() {
    //# Creating an Example object
    Example example;

    //# Calling a member function of the Example class
    example.displayMessage();

    //# Prompting the user for input
    std::cout << "Enter your name: ";
    std::string name;
    std::cin >> name;

    //# Calling a function to greet the user
    greetUser(name);

    return 0;
}

//# cette fonction Function definition
void greetUser(const std::string& name) {
    std::cout << "Hello, " << name << "! Have a great day with C++ programming." << std::endl;
}