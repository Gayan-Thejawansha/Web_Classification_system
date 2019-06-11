import java.io.*;
import java.net.*;

public class SourceViewer
{
    public static void main (String[] args) 
    {
        if (args.length > 0)
        {
            
            InputStream in         = null;
            FileOutputStream  fout = null;
            try 
            {
                URL u    = new URL(args[0]);                   // OPEN THE URL FOR READING 
                in       = u.openStream();                     // BUFFER THE INPUT TO INCREASE PERFORMANCE
                in       = new BufferedInputStream(in);        // CHAIN THE INPUTSTREAM TO A READER
                fout     = new FileOutputStream (args[1]);     // OUTPUT OF THE PROGRAM
                Reader r = new InputStreamReader(in);
                
                int c;
                while ((c = r.read()) != -1) 
                {
                    if(c != -1) 
                    {
                        fout.write(c);       
                    }
                }

            }
            catch (MalformedURLException ex) 
            {
                System.err.println(args[0] + " is not a parseable URL");
            
            }
            catch (IOException ex) 
            {
                System.err.println(ex);
            
            }
            finally
            {
                if (in != null) 
                {
                    try {
                       in.close();
                    } catch (IOException e) {}
                }
            }
            try
            {
                if(fout != null) fout.close();       
       
            } 
            catch(IOException e2) 
            {         
                System.out.println("Error Closing Output File");       
            }

        }
    }
}

