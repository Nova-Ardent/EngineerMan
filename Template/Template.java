import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
//import javax.swing.JPanel;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.io.*;


public class Template extends JPanel implements KeyListener
{   
    int w_size = 200;
    int height = 3 * w_size;
    int width = 4 * w_size;

    private Timer timer;
    // a timer class

    
    public Template( )
    {
        setPreferredSize(new Dimension( width, height ));
        setBackground(new Color(233, 233, 233));
        setLayout(null);

        addKeyListener(this);

        timer = new Timer( 500, new TimerListener());
        timer.start( );
        // sets up the timer and starts it.
    }
    public void paintComponent (Graphics page)
    {
        super.paintComponent (page);
        //page.setColor(Color.blue);
    }
    public void addNotify() 
    {
        // ignore this, it just ReNotifies, only worry about it, 
        // and run this method if a button is pressed, or else
        // you lose your key notifications for the program.
        super.addNotify();
        requestFocus();
    }
    public void keyPressed(KeyEvent e)
    {
        //System.out.println("pressed: " + (char)e.getKeyCode());
    }
    public void keyReleased(KeyEvent e)
    {
    }
    public void keyTyped(KeyEvent e)
    { 
    }
    private class TimerListener implements ActionListener
    {
        public void actionPerformed (ActionEvent event)
        {  
            repaint();
        }
    }
    private class LineListener implements MouseListener, MouseMotionListener
    {
        public void mousePressed (MouseEvent event)
        {
            if( event.getButton() == MouseEvent.BUTTON1 )
            {
            }
            else if(event.getButton() == MouseEvent.BUTTON3)
            {
                // right click will run this.
            }
        }
        public void mouseDragged (MouseEvent event)
        {
            // clicking and dragging your mouse will run this
        }
        public void mouseClicked (MouseEvent event) 
        {
            // clicking your mouse will run this
        }
        public void mouseReleased (MouseEvent event) 
        {
            // releasing the mouse will drag this
        }
        public void mouseEntered (MouseEvent event) 
        {
            // the mouse entering the frame, will activate this.
        }
        public void mouseExited (MouseEvent event) 
        {
            // mouse leaving the frame will activate this.
        }
        public void mouseMoved (MouseEvent event) 
        { 
            // moving the mouse will activate this.
        }
    }
}