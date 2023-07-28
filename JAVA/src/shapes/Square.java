package shapes;
public class Square {
    private double side;
    public Square(){
        side=0;
    }
    public Square(double side){
        this.side=side;
    }
    public double getSide(){
        return side;
    }
    public void setRadius (double side){
        this.side=side;
    }
    public double getArea(){
        return side*side;
    }
    public double getPerimeter(){
        return 2*side;
    }
}
