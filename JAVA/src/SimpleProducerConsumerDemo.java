import java.util.LinkedList;
import java.util.Queue;

public class SimpleProducerConsumerDemo {
	public static final int BUFFER_SIZE = 5;
    public static final int MAX_ITEMS = 20;
    public static void main(String[] args) {
		Item i = new Item(new LinkedList<>());
		Producer p1= new Producer(i);
		Consumer c1= new Consumer(i);
    } 
}