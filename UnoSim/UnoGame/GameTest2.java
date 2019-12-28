public class GameTest2
{
    static Deck d = new Deck();
    static boolean direction = true;
    static int player = 0;
    static GameFlag flag = GameFlag.NONE;
    static Player currentPlayer;
    static String currentPlayerName;
    static Card lastPlayed;
    static
    {
        d.shuffle();
        d.addToPlayDeck(1);
    }
    static Player[] players = {new Player(d, "Aneurin"), new Player(d, "Asyn"), new Player(d, "DJohn")};
    public static void main(String[] args)
    {
        do
        {
            playGame();
        }while(!hasAnyoneWon());
    }
    public static void totalDump()
    {
        System.out.println(d.friendlyGetDeck());
        System.out.println(direction);
        System.out.println(player);
        System.out.println(flag);
        System.out.println(currentPlayer);
        System.out.println(currentPlayerName);
        System.out.println(lastPlayed);
        System.out.println(players);
    }
    public static void nextPlayer()
    {
        if(direction)
        {
            player++;
            if(player > players.length-1 && players.length > 2)
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
    public static boolean hasAnyoneWon()
    {
        for(Player p : players)
        {
            if(!p.hasWon())
            {
                return false;
            }
        }
        return true;
    }
    public static void playGame()
    {
        nextPlayer();
        currentPlayer = players[player];
        currentPlayerName = currentPlayer.getName();
        System.out.println(currentPlayerName);
    }
    public static void play(Player p)
    {
        Card move = p.randomMove(d);
        if(move == null)
        {
            p.takeCards(1, d);
        }
        else
        {
            d.take(move);
            if(move.getType().equals(Type.MISS))
            {
                flag = GameFlag.NEXT_MISS;
            }
            else if(move.getType().equals(Type.REVERSE))
            {
                direction = !direction;
            }
            else if(move.getType().equals(Type.TAKE))
            {
                flag = GameFlag.NEXT_TAKE_TWO;
            }
            else if(move.getType().equals(Type.SUPER))
            {
                flag = GameFlag.NEXT_TAKE_FOUR;
            }
        }
    }
}
