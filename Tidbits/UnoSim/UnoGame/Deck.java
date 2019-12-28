import java.util.LinkedList;
import java.util.Collections;

/**
 * An extension to the LinkedList class.
 * Methods use more game-relevant terms.
 * It also puts more authority over what can be done to the deck.
 * Contains the deck and the cards that are being played on (the playDeck).
 */
public class Deck
{
    private  LinkedList<Card> deck = new LinkedList<Card>();
    private LinkedList<Card> playDeck = new LinkedList<Card>();
    /**
     * Constructor for objects of type Deck. Sets up deck with 108 Cards
     */
    public Deck()
    {
        for(byte id = 0; id <= 53; id++)
        {
            if((id==0)||(id==13)||(id==26)||(id==39))
            {
                deck.addFirst(new Card(id));
            }
            else if((id==52)||(id==53))
            {
                deck.addFirst(new Card(id));
                deck.addFirst(new Card(id));
                deck.addFirst(new Card(id));
                deck.addFirst(new Card(id));
            }
            else
            {
                deck.addFirst(new Card(id));
                deck.addFirst(new Card(id));
            }
        }
    }
    /**
     * Shuffles the deck with Collections.shuffle()
     */
    public void shuffle()
    {
        Collections.shuffle(deck);
    }
    /**
     * Gets the deck
     * @return A LinkedList of Cards containing the whole deck
     */
    public LinkedList<Card> getDeck()
    {
        return deck;
    }
    /**
     * Gets the cards being played on (the playDeck)
     * @return A LinkedList of Cards containing the whole playDeck
     */
    public LinkedList<Card> getPlayDeck()
    {
        return playDeck;
    }
    /**
     * Gets rid of the top of the deck
     * @return The Card at the top of the deck
     */
    public Card giveTop()
    {
         return deck.removeFirst();
    }
    /**
     * Gets what card was last played on the playDeck
     * @return A Card representing the lst played Card
     */
    public Card getLastPlayed()
    {
        return playDeck.getFirst();
    }
    /**
     * 
     */
    public Card getTop()
    {
        return deck.peek();
    }
    public void addToPlayDeck(int times)
    {
        for(int i=1; i <= times;i++)
        {
            playDeck.addFirst(deck.removeFirst());
        }
    }
    public void addToPlayDeck(Card c)
    {
        playDeck.addFirst(c);
    }
    public void take(Card c)
    {
        deck.add(c);
    }
    public String friendlyGetDeck()
    {
        String friendly = "";
        for(Card c : deck)
        {
           friendly += c + ", ";
        }
        return friendly;
    }
    public String friendlyGetPlayDeck()
    {
        String friendly = "";
        for(Card c : playDeck)
        {
           friendly += c + ", ";
        }
        return friendly;
    }
    public boolean playable(Card c)
    {
        if(playDeck.size()==0)
        {
            return false;
        }
        Card t = playDeck.peek();
        if(c.getColor().equals(Color.WILD))
        {
            return true;
        }
        else if(c.getType().equals(t.getType()))
        {
            return true;
        }
        else if(c.getColor().equals(t.getColor()))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
