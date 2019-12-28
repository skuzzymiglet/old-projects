public class Test2
{
    static Deck d = new Deck();
    static
    {
        d.shuffle();
        d.addToPlayDeck(6);
    }
    static Player p = new Player(d, "Muhammad");
    public static void main(String[] args)
    {
        System.out.println("==================================================");
        System.out.println(p.getName());
        System.out.print(d.getTop().friendly()[0]);
        System.out.println(d.getTop().friendly()[1]);
        for(Card c:p.getCards())
        {
            System.out.print(c.friendly()[0]);
            System.out.print(c.friendly()[1]);
            System.out.println(d.playable(c));
        }
    }
}
