
interface Notification {
    void notifyUser();
}
class SMSNotification implements Notification {
 
    @Override
    public void notifyUser()
    {
        System.out.println("Sending an SMS notification");
    }
}
class EmailNotification implements Notification {

	@Override
	public void notifyUser()
	{
		// TODO Auto-generated method stub
		System.out.println("Sending an e-mail notification");
	}
}
class PushNotification implements Notification {

	@Override
	public void notifyUser()
	{
		// TODO Auto-generated method stub
		System.out.println("Sending a push notification");
	}
}
class NotificationFactory {
	public Notification createNotification(String channel)
	{
		if (channel == null || channel.isEmpty())
			return null;
		switch (channel) {
		case "SMS":
			return new SMSNotification();
		case "EMAIL":
			return new EmailNotification();
		case "PUSH":
			return new PushNotification();
		default:
			throw new IllegalArgumentException("Unknown channel "+channel);
		}
	}
}
public class Main {
	public static void main(String[] args)
	{
		NotificationFactory notificationFactory = new NotificationFactory();
		Notification notification1 = notificationFactory.createNotification("SMS");
		notification1.notifyUser();
		Notification notification2 = notificationFactory.createNotification("EMAIL");
		notification2.notifyUser();
		Notification notification3 = notificationFactory.createNotification("PUSH");
		notification3.notifyUser();
	}
}
