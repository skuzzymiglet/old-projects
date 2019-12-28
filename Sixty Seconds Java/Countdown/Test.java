public class Test
{
    static CountDown cd = new CountDown();
    static Thread t = new Thread(cd);
    public static void main(String[] args)
    {
        t.start();
    }
}
