package paquetes;

import java.util.ArrayList;

/**
 *
 * @author cristian
 */
public class Voraz {
     /*Indica la actividad  por la cual se empieza
    */
    public int vertice(ArrayList<Integer> a, ArrayList<Integer> b){
       
        int v_;
        if(Math.min(a.get(0),b.get(0))==a.get(0)){
             v_= a.get(0);
        }else{
            v_= b.get(0);
        }
        
        return v_;
    }
    
    /*Determina la ruta optima
    */
    public ArrayList<String> voraz(ArrayList<Integer> a, ArrayList<Integer> b,int m[][]){
        
        int inicia=vertice(a, b);//Indica el numero menos entre los elementos de a y b
        ArrayList<Integer> ruta = new ArrayList();//Se almacenara el conjunto de vertices que tienen el camino minimo
        ArrayList<Integer> solucion = new ArrayList();//Indica los pesos que tarda un vertice hacia los otros
        ArrayList<Integer> verticesCambio = new ArrayList();//es el conjunto de vertices que ira disminuyendo despues de encontrar la mejor alternativa
        ArrayList<Integer> vertices = new ArrayList();//Es el comjunto de vertices totales
        ArrayList<Integer> c = new ArrayList();//contiene los datos de el arreglo a y arregle b
        
        //Agrega los datos del arreglo a al arreglo c
        for(int i = 0; i<a.size();i++){
            c.add(a.get(i));
        }
        //Agrega los datos del arreglo b al arreglo c
        for(int i = 0; i<b.size();i++){
            c.add(b.get(i));
        }
        
        //Agrega a el arreglo vertices y verticesCambio el numero de vertices 
        //que equivale al numero de actividades posibles que se pueden hacer 
        for(int i = 0; i<c.size();i++){
            vertices.add(i);
            verticesCambio.add(i);
        }
     
        int posicionInicia = c.indexOf(inicia) ;//indica la posicion donde se encuentra el numero inicia
        int division=(verticesCambio.size()/2)-1;
        
        ruta.add(posicionInicia);
        if(posicionInicia>division){
            verticesCambio.remove(posicionInicia);
            verticesCambio.remove(0);
        }else{
            verticesCambio.remove(posicionInicia);
            verticesCambio.remove(division);
        }
       
        int pv;
        // se ejecuta mientras verticesCambio este vacio
        while(!verticesCambio.isEmpty()){
            
            pv=posicionInicia;
           
            for(int j=0;j<c.size();j++){
            solucion.add(m[pv][j]);// Indica el peso que cuesta ir del vertice 
                                   //hasta cada uno de los vertices                           
            }
          
            int c_;
            int e;
            c_= solucion.indexOf(minimo(solucion));//Indica el indice donde se ecuentra el valor minimo de la solucion
            e = verticesCambio.indexOf(vertices.get(c_));
            ruta.add(c_);
           
            division=(verticesCambio.size()/2)-1;
            
            if(c_>division){
                verticesCambio.remove(e);
                verticesCambio.remove(0);
            }else{
                verticesCambio.remove(e);
                verticesCambio.remove(division);
            }
            
            posicionInicia=c_;
            solucion.clear();
            
            
        }
        //ruta.add(c.get(inicia));
        for(int y=0; y<ruta.size();y++){
            System.out.print(ruta.get(y) + ", ");
        }
        
        return salidaRuta(ruta);
    }
    /*Realiza la matriz de pesos de la cadena segun los arreglos de entrada
    */
    public int [][] matriz (ArrayList<Integer> a,ArrayList<Integer> b,
                            ArrayList<Integer> ab,ArrayList<Integer>ba ){
    
    ArrayList<Integer> completo= new ArrayList<Integer> ();
        for(int i =0;i<a.size();i++){
        completo.add(a.get(i));
        }
        for(int z =0;z<b.size();z++){
        completo.add(b.get(z));
        }
  
    int [][] matriz = new int [completo.size()][completo.size()] ;    

    int mitad = (completo.size()/2);
    int ultimo = completo.size()-1;
    int contador1=0;
    int contador2 = mitad+1;
    int contador3=0;
    
        for(int x=0;x<a.size();x++){ 
             contador1=x+1;
             
            for(int y=0;y<completo.size();y++){
               
                if(x==mitad-1){
                   matriz[x][y]=999; 
                   contador1=0;
                }else if(x==ultimo){
                   matriz[x][y]=999;    
                }else if(y==contador1){
                    matriz[x][y]=completo.get(y);
                }else if(y==contador2){
                    matriz[x][y]=completo.get(y)+ab.get(contador3);
                    //contador2++;
                    contador3++;
                }else{
                    matriz[x][y]=999;
                }
            }
            contador2++;
        }
        
         contador2=mitad+1; 
         contador3=0;
         for(int x2=mitad;x2<completo.size();x2++){ 
             contador1++;
             
            for(int y2=0;y2<completo.size();y2++){
               
                if(x2==ultimo){
                   matriz[x2][y2]=999;    
                }else if(y2==contador1){
                    matriz[x2][y2]=completo.get(y2)+ba.get(contador3);
                    contador3++;  
                }else if(y2==contador2){
                    matriz[x2][y2]=completo.get(y2);
                }else{
                    matriz[x2][y2]=999;
                }
            }
            contador2++;
        }
        
              
      
      for(int l=0;l<completo.size();l++){
            for(int s=0;s<completo.size();s++){
                System.out.print(matriz[l][s] + ",");                

            }               
            System.out.print("\n"); 
      }
          
    return matriz;    
        
    
   }
   
    /*Indica si el vertice elegido en el array pertenece a la cadena a o b 
    */
    public ArrayList<String> salidaRuta(ArrayList<Integer> r){
        ArrayList<String> ruta= new ArrayList<String> ();
        int mitad = r.size()/2;
        for(int i =0; i<r.size();i++){
            if(r.get(i)<r.size()){
                ruta.add("a");
            }else{
                ruta.add("b");
            }
        }
       //ruta.add();
          System.out.print("\n");
          for(int y=0; y<ruta.size();y++){
            System.out.print(ruta.get(y) + ", ");
        }
        
        return ruta;
    } 
    
    /*Indica el elemento minimo de un ArrayList de enteros
    */
    public int minimo(ArrayList<Integer> d){
        int minimo=d.get(0);
        for(int i=0; i<d.size();i++){
            if(minimo>d.get(i)){
                minimo=d.get(i);
            }
        }
        
        return minimo;
    }
}
