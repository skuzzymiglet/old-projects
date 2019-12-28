public class ScopeTest
{
    static GameFlag flag = GameFlag.NONE;
    public static void main(String[] args)
    {
        System.out.println(flag);
        flag = GameFlag.NEXT_MISS;
        System.out.println(flag);
    }
}
