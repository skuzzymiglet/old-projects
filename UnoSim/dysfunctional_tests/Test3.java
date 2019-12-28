public class Test3
{
    static Deck d = new Deck();
    static
    {
        d.shuffle();
    }
    static Player p = new Player(d, "Asentorov");
    //public static void main(String[] args)
    //{
    //    for(Card c : p.randomMove(d))
    //    {
    //        System.out.println(c);
    //   }
    //}
}
