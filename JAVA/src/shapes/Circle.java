package shapes;
public class Circle {
    protected double radius;
    public Circle(){
        radius=0;
    }
    public Circle(double r){
        radius=r;
    }
    public void setRadius(double r){
        radius=r;
    }
    public double getRadius(){
        return radius;
    }
    public double getPerimeter(){

        return 2*3.14*radius;
    }
    public double getArea() {
        double area=radius*radius*3.14;
        return area;
    }
}
