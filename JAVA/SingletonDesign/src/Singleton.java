public class Singleton
{
    private static Singleton obj; // class itself create obj send that
    private Singleton() {
        System.out.println("Instance created");
    } // forcing to not create objects
    public int i;
    public static Singleton getInstance()
    {
        if (obj==null)
            obj = new Singleton();
        return obj;
    }
}