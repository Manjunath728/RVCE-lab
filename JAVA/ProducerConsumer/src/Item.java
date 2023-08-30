public class Item {
      int item;
      int 
      public void put(int item){
        this.item=item;
      }
      public int get(){
        return item;
      }
}

class Producer implements Runnable{
    Item i;
    public Producer(Item i){
        this.i=i;
    }
    public void run(){
        int  i=0;
        while (true) {
            i.put()
        }
    }
}
