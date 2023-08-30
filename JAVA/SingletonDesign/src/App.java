            public class App {
                public static void main(String[] args) throws Exception {
                    Singleton obj1= Singleton.getInstance();
                    obj1.i=100;
                    Singleton obj2= Singleton.getInstance();
                    System.out.println(obj2.i);
                }
}
