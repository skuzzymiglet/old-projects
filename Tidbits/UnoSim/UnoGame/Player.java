import java.util.LinkedList;

public class Player
{
    private LinkedList<Card> cards = new LinkedList<Card>();
    private final LinkedList<Card> INITIAL_CARDS;
    private String name;
    public Player(Deck d, String name)
    {
        takeCards(7, d);
        this.name = name;
        INITIAL_CARDS = cards;
    }
    public void takeCards(int q, Deck deck)
    {
        for(int i = 1; i<= q; i++)
        {
            cards.add(deck.giveTop());
        }
    }
    public void takeCard(Card c)
    {
        cards.add(c);
    }
    public LinkedList<Card> getCards()
    {
        return cards;
    }
    public Card giveCard()
    {
        return cards.removeFirst();
    }
    public Card giveCard(Card x)
    {
        try
        {
            cards.remove(x);
            return x;
        }
        catch(Exception e)
        {
            return null;
        }
    }
    public String getName()
    {
        return name;
    }
    public Card randomMove(Deck d, boolean isPlayAfterWild)
    {
        if(isPlayAfterWild)
        {
            LinkedList<Card> notWilds = getNotWild();
            return notWilds.get(randInt(0, notWilds.size()-1));
        }
        else
        {
            LinkedList<Card> playables = getPlayables(d);
            if(playables.size() == 0)
            {
                return null;        
            }
            else
            {
                for(Card c : cards)
                {
                    if(d.playable(c))
                    {
                        playables.add(c);
                    }
                }
                int index = randInt(0, (playables.size()-1));
                return playables.get(index);
            }
        }
    }
    public Card randomMove(Deck d)
    {
        LinkedList<Card> playables = getPlayables(d);
        if(playables.size() == 0)
        {
            return null;        
        }
        else
        {
            for(Card c : cards)
            {
                if(d.playable(c))
                {
                    playables.add(c);
                }
            }
            int index = randInt(0, (playables.size()-1));
            return giveCard(playables.get(index));
        }
    }
    private int randInt(int high, int low)
    {
        return (int)(Math.random() * (high - low + 1)) + low;
    }
    public LinkedList<Card> getPlayables(Deck d)
    {
        LinkedList<Card> playables = new LinkedList<Card>();
        for(Card c : cards)
        {
            if(d.playable(c))
            {
                playables.add(c);
            }
        }
        return playables;
    }
    private LinkedList<Card> getNotWild()
    {
        LinkedList<Card> notWilds = new LinkedList<Card>();
        for (Card c : cards)
        {
            if(!c.getColor().equals(Color.WILD))
            {
                notWilds.add(c);
            }
        }
        return notWilds;
    }
    public String friendlyGetCards()
    {
        String friendly = "";
        for(Card c : cards)
        {
           friendly += c.friendlyString() + ", ";
        }
        return friendly;
    }
    public boolean hasWon()
    {
        if(cards.size() == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public String toString()
    {
        return name + " has cards " + friendlyGetCards();
    }
    public LinkedList<Card> getInitialCards()
    {
        return INITIAL_CARDS;
    }
}
