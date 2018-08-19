import javax.swing.*;
public class TemplateRun
{
    //-----------------------------------------------------------------
    //  Displays the main frame of the program.
    //-----------------------------------------------------------------
    public static void main (String[] args)
    {

        JFrame frame = new JFrame ("Organizer");
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.getContentPane().add (new Template());
        frame.pack();
        frame.setVisible(true);

    }
}