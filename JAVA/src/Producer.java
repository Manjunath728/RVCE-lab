public class Producer implements Runnable {
    private final Item itemManager;

    public Producer(Item itemManager) {
        this.itemManager = itemManager;
				Thread t = new Thread(this ,"Producer");
				t.start();
    }

    @Override
    synchronized public void run() {
        int item = 1;
        while (item <= SimpleProducerConsumerDemo.MAX_ITEMS) {
            itemManager.produce(item);
            try {
                Thread.sleep(5000);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            

            item++;
        }
    }
}