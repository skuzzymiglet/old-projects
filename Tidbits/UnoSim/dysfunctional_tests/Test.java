public class Test
{
    public static void main(String[] args)
    {
        Deck d = new Deck();
        //d.shuffle();
        /*
        while(!d.getDeck().isEmpty())
        {
            Card top = d.getTop();
            System.out.print(top.friendly()[0]);
            System.out.print(top.friendly()[1]);
            System.out.println(d.getDeck().size());
        }*/
        for(Card x:d.getDeck())
        {
            System.out.print(x.friendly()[0]);
            System.out.println(x.friendly()[1]);
        }
        System.out.println("==========================================================================================================");
        d.addToPlayDeck(18);
        for(Card x:d.getPlayDeck())
        {
            System.out.print(x.friendly()[0]);
            System.out.println(x.friendly()[1]);
        }
        System.out.println(d.playable(new Card(Color.RED, Type.TAKE)));
        //System.out.println(d.getPlayDeck().stream().forEach(s -> System.out.println(s.friendly())));
    }
 
}
