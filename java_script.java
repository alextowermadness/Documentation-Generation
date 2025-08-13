//# Importing the Scanner class from java.util package
import java.util.Scanner;

//@ cette class A simple Java class
public class Example {
    
//@ cette fonction Main method, entry point of the program
    public static void main(String[] args) {
        //# Creating a Scanner object for input
        Scanner scanner = new Scanner(System.in);
        
        //# Prompting the user for input
        System.out.print("Enter your name: ");
        
        //# Reading user input
        String name = scanner.nextLine();
        
        //# Calling a function to greet the user
        greetUser(name);
        
        //# Closing the Scanner object
        scanner.close();
    }
    
    /* 
     * Function to greet the user
     * Takes a String parameter (name) and prints a greeting message
     */
    public static void greetUser(String name) {
        System.out.println("Hello, " + name + "! Welcome to Java programming.");
    }
    
    /*
     * This is a multi-line comment
     * It can span multiple lines
     * Used for providing detailed explanations or annotations
     */
}