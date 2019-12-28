import java.util.Arrays;
/**
 * Represents an UNO Card
 * (Immutable)
 */
public class Card
{
    private Color color;
    private Type type;
    private int id;
    /**
     * Constructor for objects of class Card, using traditional Color and Type
     */
    public Card(Color color, Type type)
    {
        this.color = color;
        this.type = type;
        this.id = findId(color, type);
    }
    /**
     * Constructor for objects of class card, using convenient ID System
     */
    public Card(int id)
    {
        this.id = id;
        this.color = (Color)ID_LIST[id] [0];
        this.type = (Type)ID_LIST[id] [1];
    }
    /**
     * Gets the color of the card
     * @return Color Enum type
     */
    public Color getColor()
    {
        return color;
    }
    /**
     * Gets the type of card
     * @return Type Enum type
     */
    public Type getType()
    {
        return type;
    }
    /**
     * Gets the card ID
     * @return int representing ID
     */
    public int getId()
    {
        return id;
    }
    private static final Object[][] ID_LIST = { 
        {Color.RED, Type.ZERO}, {Color.RED, Type.ONE}, {Color.RED, Type.TWO}, {Color.RED, Type.THREE}, {Color.RED, Type.FOUR}, {Color.RED, Type.FIVE}, {Color.RED, Type.SIX}, {Color.RED, Type.SEVEN}, {Color.RED, Type.EIGHT}, {Color.RED, Type.NINE}, {Color.RED, Type.MISS}, {Color.RED, Type.REVERSE}, {Color.RED, Type.TAKE},
        {Color.ORANGE, Type.ZERO}, {Color.ORANGE, Type.ONE}, {Color.ORANGE, Type.TWO}, {Color.ORANGE, Type.THREE}, {Color.ORANGE, Type.FOUR}, {Color.ORANGE, Type.FIVE}, {Color.ORANGE, Type.SIX}, {Color.ORANGE, Type.SEVEN}, {Color.ORANGE, Type.EIGHT}, {Color.ORANGE, Type.NINE}, {Color.ORANGE, Type.MISS}, {Color.RED, Type.REVERSE}, {Color.RED, Type.TAKE},
        {Color.GREEN, Type.ZERO}, {Color.GREEN, Type.ONE}, {Color.GREEN, Type.TWO}, {Color.GREEN, Type.THREE}, {Color.GREEN, Type.FOUR}, {Color.GREEN, Type.FIVE}, {Color.GREEN, Type.SIX}, {Color.GREEN, Type.SEVEN}, {Color.GREEN, Type.EIGHT}, {Color.GREEN, Type.NINE}, {Color.GREEN, Type.MISS}, {Color.GREEN, Type.REVERSE}, {Color.GREEN, Type.TAKE},
        {Color.BLUE, Type.ZERO}, {Color.BLUE, Type.ONE}, {Color.BLUE, Type.TWO}, {Color.BLUE, Type.THREE}, {Color.BLUE, Type.FOUR}, {Color.BLUE, Type.FIVE}, {Color.BLUE, Type.SIX}, {Color.BLUE, Type.SEVEN}, {Color.BLUE, Type.EIGHT}, {Color.BLUE, Type.NINE}, {Color.BLUE, Type.MISS}, {Color.BLUE, Type.REVERSE}, {Color.BLUE, Type.TAKE},
        {Color.WILD, Type.CHANGE}, {Color.WILD, Type.SUPER}
    }; // Indexes correspond to IDs
    private static int findId(Color color, Type type)
    {
        Object c;
        Object t;
        int id = 0;
        for (Object[] props : ID_LIST)
        {
            if(props[0] == color && props[1] == type)
            {
                break;
            }
            id++;
        }
        return id;
    }
    /**
     * @deprecated
     * Use toString()
     */
    public String[] friendly()
    {
        String[] friendly = {this.type.name(), this.color.name()};
        return friendly;
    }
    /**
     * @deprecated
     */
    public int getTier()
    {
        if(this.color.equals(Color.WILD))
        {
            return 3;
        }
        else if(this.type.equals(Type.MISS) || this.type.equals(Type.REVERSE) || this.type.equals(Type.TAKE))
        {
            return 2;
        }
        else 
        {
            return 1;
        }
    }
    /**
     * @deprecated
     * Use toString()
     */
    public String friendlyString()
    {
        return this.friendly()[0] + this.friendly()[1];
    }
    // Overriding Object method (yay!!)
    /**
     * Gets a String containing color and type
     * @return A String with color and type
     */
    public String toString()
    {
        return this.friendlyString();
    }
}
