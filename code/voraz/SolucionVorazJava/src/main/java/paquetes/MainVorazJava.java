
package paquetes;

import java.util.ArrayList;
import  paquetes.Voraz;       
        

/**
 *
 * @author cristian
 */
public class MainVorazJava {

    public static void main(String[] args) {
        Voraz v = new Voraz();
        
        /*ArrayList<Integer> vertices = new ArrayList();
        vertices.add(7);vertices.add(9);vertices.add(3);
        vertices.add(4);vertices.add(8);vertices.add(4);

        ArrayList<Integer> vertices2 = new ArrayList();
        vertices2.add(8);vertices2.add(5);vertices2.add(6);
        vertices2.add(4);vertices2.add(5);vertices2.add(7);
     
        ArrayList<Integer> verticesab = new ArrayList();
        verticesab.add(2);verticesab.add(1);verticesab.add(2);
        verticesab.add(2);verticesab.add(1);
        
        ArrayList<Integer> verticesba = new ArrayList();
        verticesba.add(2);verticesba.add(3);verticesba.add(1);
        verticesba.add(3);verticesba.add(4);*/
        
        ArrayList<Integer> vertices = new ArrayList();
        vertices.add(2);vertices.add(2);vertices.add(6);
        
        ArrayList<Integer> vertices2 = new ArrayList();
        vertices2.add(3);vertices2.add(5);vertices2.add(3);
        
        ArrayList<Integer> verticesab = new ArrayList();
        verticesab.add(1);verticesab.add(1);
        
        ArrayList<Integer> verticesba = new ArrayList();
        verticesba.add(4);verticesba.add(2);

        
       /* ArrayList<Integer> vertices = new ArrayList();
        vertices.add(4);vertices.add(6);vertices.add(9);vertices.add(2);
        
        ArrayList<Integer> vertices2 = new ArrayList();
        vertices2.add(3);vertices2.add(5);vertices2.add(10);vertices2.add(8);
        
        ArrayList<Integer> verticesab = new ArrayList();
        verticesab.add(1);verticesab.add(4);verticesab.add(2);
        
        ArrayList<Integer> verticesba = new ArrayList();
        verticesba.add(5);verticesba.add(2);verticesba.add(1);
        */
        
        v.voraz(vertices, vertices2, v.matriz(vertices, vertices2, verticesab, verticesba));
        System.out.print("-----"+"\n");
        v.matriz(vertices, vertices2, verticesab, verticesba);
    }
    
}
