package mydatastructures;

import mydatastructures.heap.MyMaxHeap;
import mydatastructures.utils.MyUtils;

/**
 *
 * @author PO
 */
public class MyDataStructures {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Integer[] array = {5, 13, 2, 25, 7, 17, 20, 8, 4};
        MyMaxHeap heap = new MyMaxHeap(array);
        System.out.println(MyUtils.Stringify(heap.sorted()));
        System.out.println(heap.toString());   
    }

}

