class State 
{
    private Diverter diverter;
    private KeyTranslator kt;
    private int id;
    public State(int id, KeyTranslator kt, Diverter dv)
    {
        this.id = id;
        this.kt = kt;
        this.diverter = dv; 
    }
    public char translateKeyPress()
    {
        
    }
}
interface KeyTranslator
{
    public char translate_key(int key);
}
interface Diverter
{
    public void divert(int key, int id);
}