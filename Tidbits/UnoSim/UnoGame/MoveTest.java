public class MoveTest
{
    static Deck d = new Deck();
    static
    {
        d.shuffle();
        d.addToPlayDeck(1);
    }
    static Player p = new Player(d, "Aneurin");
    public static void main(String args[])
    {
        System.out.println();
        System.out.println("================================================");
        System.out.println(friendlyGetPlayDeck(d));
        System.out.println(friendlyGetCards(p));
        System.out.println(friendlyString(p.randomMove(d, false)));
        move(p);
        System.out.println(friendlyGetCards(p));
        System.out.println(friendlyGetPlayDeck(d));
    }
    public static String friendlyString(Card c)
    {
        String[] friendly = c.friendly();
        return friendly[0] + friendly[1];
    }
    public static String friendlyGetDeck(Deck d)
    {
        String friendly = "";
        for(Card c : d.getDeck())
        {
           friendly += friendlyString(c) + ", ";
        }
        return friendly;
    }
    public static String friendlyGetPlayDeck(Deck d)
    {
        String friendly = "";
        for(Card c : d.getPlayDeck())
        {
           friendly += friendlyString(c) + ", ";
        }
        return friendly;
    }
    public static String friendlyGetCards(Player p)
    {
        String friendly = "";
        for(Card c : p.getCards())
        {
           friendly += friendlyString(c) + ", ";
        }
        return friendly;
    }
    public static void move(Player p)
    {
        Card randomCard = p.randomMove(d, false);
        if(randomCard == null)
        {
            p.takeCard(d.giveTop());
        }
        else
        {
            d.addToPlayDeck(p.giveCard(randomCard));
            System.out.println(friendlyString(randomCard));
        }
    }
}
