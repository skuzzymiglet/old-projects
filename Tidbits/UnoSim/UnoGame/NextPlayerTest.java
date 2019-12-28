public class NextPlayerTest
{
    static Deck d = new Deck();
    static
    {
        d.shuffle();
        d.addToPlayDeck(1);
    }
    static Player[] players = {new Player(d, "Aneurin"), new Player(d, "Muhammad"), new Player(d, "DJohn")};
    static int player = 0;
    static boolean direction = true;
    static GameFlag flag = GameFlag.NONE;
    public static void main(String[] args)
    {
        System.out.println("#####################################################################################################################################");
        while(true)
        {
            System.out.print(players[player].getName() + Integer.toString(player));
            if(flag.equals(GameFlag.NEXT_MISS))
            {
                System.out.print(" missed ");
                flag = GameFlag.NONE;
                System.out.println();
            }
            else
            {
                if(randInt(1, 6) == 4)
                {
                    System.out.print(" reversing direction...");
                    direction = !direction;
                }
                if(randInt(1, 12) == 4)
                {
                    flag = GameFlag.NEXT_MISS;
                }
            }
            System.out.println();
            nextPlayer();
        }
    }
    public static void nextPlayer()
    {
        if(direction)
        {
            player++;
            if(player > players.length-1)
            {
                player = 0;
            }
        }
        else
        {
            player--;
            if(player < 0)
            {
                player = players.length-1;
            }
        }
    }
    public static int randInt(int high, int low)
    {
        return (int)(Math.random() * (high - low + 1)) + low;
    }
}
