import java.util.Scanner;

import shapes.*;

public class Lab2 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("enter the radius of circle : ");
        double radius = s.nextDouble();
        Circle circle = new Circle(radius);
        System.out.println("Area of circle :"+circle.getArea());
        System.out.print("enter the side of square  : ");
        double side = s.nextDouble();
        Square square = new Square(side);
        System.out.println("Area of square :"+square.getArea());
        s.close();
    }
}
