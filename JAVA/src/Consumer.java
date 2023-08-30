public class Consumer implements Runnable {
    private final Item itemManager;

    public Consumer(Item itemManager) {
        this.itemManager = itemManager;
		Thread t = new Thread(this ,"Consumer");
		t.start();
    }

    @Override
    synchronized public void run() {
        int consumedItems = 0;
        while (consumedItems < SimpleProducerConsumerDemo.MAX_ITEMS) {
            itemManager.consume();
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            consumedItems++;
        }
    }
}