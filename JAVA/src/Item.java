import java.util.Queue;

public class Item {
    private final Queue<Integer> buffer;
    private static int itemCount = 0;

		public Item(Queue<Integer> buffer) {
        this.buffer = buffer;
    }

    public synchronized void produce(int item) {
        while (buffer.size() == SimpleProducerConsumerDemo.BUFFER_SIZE) {
            try {
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        buffer.add(item);
        itemCount++;
        System.out.println("Produced: " + item);
        notifyAll();
    }

    public synchronized void consume() {
        while (buffer.isEmpty()) {
            try {
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        int item = buffer.poll();
        System.out.println("Consumed: " + item);
        notifyAll();
    }
}