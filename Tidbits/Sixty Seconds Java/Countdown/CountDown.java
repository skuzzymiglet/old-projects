public class CountDown implements Runnable
{
    int t = 60;
    public void run()
    {
        for(t=60; t >= 0; t--)
        {
            System.out.println(t);
            try
            {
                Thread.sleep(1000);
            }
            catch(InterruptedException ie){}
        }
        System.out.println("Off the web he goes!");
    }
    public void addSecond()
    {
        t++;
    }
    public void subtractSecond()
    {
        t--;
    }
}
