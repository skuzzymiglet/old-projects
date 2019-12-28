public class GameTest
{
    static Deck d = new Deck();
    static boolean direction = true;
    static int player = 0;
    static GameFlag flag = GameFlag.NONE;
    static Player currentPlayer;
    static String currentPlayerName;
    static Card move;
    static int numOfPlays = 0;
    static
    {
        d.shuffle();
        d.addToPlayDeck(1);
    }
    static Player[] players = {new Player(d, "Aneurin"), new Player(d, "Asyn")};
    public static void main(String[] args)
    {
       System.out.println("========================================");
       System.out.println("Welcome to jUNO - Java UNO!");
       System.out.println(d.friendlyGetDeck());
       System.out.println("Top of deck = " + d.getTop());
       while(true)
       {
           if (hasAnyoneWon())
           {
               break;
           }
           System.out.println(flag);
           flag = GameFlag.NEXT_MISS;
           numOfPlays++;
           System.out.println("========================================= Move #" + Integer.toString(numOfPlays) + " ========================================="); 
           nextPlayer();
           System.out.println(player);
           currentPlayer = players[player];
           currentPlayerName = currentPlayer.getName();
           System.out.println(currentPlayer);
           System.out.println((flag == GameFlag.NEXT_MISS)|(flag == GameFlag.NEXT_TAKE_TWO)|(flag == GameFlag.NEXT_TAKE_FOUR));
           if(flag.equals(GameFlag.NEXT_MISS))
           {
               System.out.println(currentPlayerName + " missed a turn");
               flag = GameFlag.NONE;
               nextPlayer();
               continue;
           }
           if(flag.equals(GameFlag.NEXT_TAKE_TWO))
           {
               System.out.println(currentPlayerName + " took two cards");
               currentPlayer.takeCards(2, d);
               System.out.println(currentPlayerName + " has " + Integer.toString(currentPlayer.getCards().size()) + " cards");
               flag = GameFlag.NONE;
               nextPlayer();
               continue;
           }
           if(flag.equals(GameFlag.NEXT_TAKE_FOUR))
           {
               System.out.println(currentPlayerName + " took four cards");
               currentPlayer.takeCards(4, d);
               System.out.println(currentPlayerName + " has " + Integer.toString(currentPlayer.getCards().size()) + " cards");
               flag = GameFlag.NONE;
               nextPlayer();
               continue;
           }
           else
           {
               move = move(currentPlayer);
               if(move == null)
               {
                   continue;
               }
               System.out.println(currentPlayerName + " played " + move);
               if(move.getType().equals(Type.MISS))
               {
                   flag = GameFlag.NEXT_MISS;
                   System.out.println("hi rafik");
               }
               else if(move.getType().equals(Type.TAKE))
               {
                   flag = GameFlag.NEXT_TAKE_TWO;
                   System.out.println("hi rafik");
               }
               else if(move.getType().equals(Type.SUPER))
               {
                   flag = GameFlag.NEXT_TAKE_FOUR;
                   System.out.println("hi rafik");
               }
               else if(move.getColor().equals(Color.WILD))
               {
                   //currentPlayer.randomMove(d, true);
                   System.out.println("hi rafik");
               }
               else if(move.getType().equals(Type.REVERSE))
               {
                   changeDirection();
                   System.out.println("hi rafik");
               }
           }
       }
    }
    public static boolean hasWon(Player p)
    {
       return (p.getCards().size() == 0);
    }
    public static boolean hasAnyoneWon()
    {
        for(Player p : players)
        {
            if (p.getCards().size() == 0)
            {
                return true;
            }
        }
        return false;
    }
    public static Card move(Player p)
    {
        Card randomCard = p.randomMove(d, false);
        System.out.println("Move = " + randomCard);
        if(randomCard == null)
        {
            p.takeCard(d.giveTop());
        }
        else
        {
            d.addToPlayDeck(p.giveCard(randomCard));
            return null;
        }
        return randomCard;
    }
    public static void nextPlayer()
    {
        if(flag.equals(GameFlag.PLAY_TWICE))
        {
            flag = GameFlag.NONE;
        }
        else
        {
            if(direction)
            {
                player++;
                if(player >= players.length)
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
    }
    public static void changeDirection()
    {
        direction = !direction;
        if(players.length == 2)
        {
            flag = GameFlag.PLAY_TWICE;
        }
    }
}
