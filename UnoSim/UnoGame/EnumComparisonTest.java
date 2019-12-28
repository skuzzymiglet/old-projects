public class EnumComparisonTest
{
    static GameFlag gf1 = GameFlag.NEXT_MISS;
    static GameFlag gf2 = GameFlag.NEXT_TAKE_TWO;
    public static void main(String args[])
    {
        System.out.println(gf1 == gf2);
        if(!(gf1 == gf2))
        {
            System.out.println("FLUCK");
        }
    }
}
