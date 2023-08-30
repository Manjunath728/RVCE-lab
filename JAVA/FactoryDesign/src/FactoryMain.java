import com.phone.*;
public class FactoryMain {
    public static void main(String[] args) {
        OSfactory factory= new OSfactory();
        OS mi = factory.getInstance("close");
        mi.spec();
    }
}
