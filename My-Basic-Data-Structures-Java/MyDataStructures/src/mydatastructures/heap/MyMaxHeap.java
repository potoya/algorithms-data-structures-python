/*
 * My Implementation of a max or min heap.
 */
package mydatastructures.heap;

import java.util.Arrays;
import java.util.StringJoiner;
import java.util.stream.IntStream;
import mydatastructures.utils.MyUtils;

/**
 * Class representing my heap impl
 *
 * @author PC
 * @param <T>
 */
public final class MyMaxHeap<T extends Comparable<? super T>> {

    T[] A;

    public MyMaxHeap(T[] Aprime) {
        A = Aprime;
        buildMaxHeap(A);
    }

    private int parent(int i) {
        return Math.floorDiv(i - 1, 2);
    }

    private int left(int i) {
        return 2 * i + 1;
    }

    private int right(int i) {
        return 2 * i + 2;
    }

    private void swap(T[] A, int i, int j) {
        T temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }

    /**
     * Floats the element i which is violating the max heap property.
     *
     * @param A
     * @param i Index of number violating the property.
     */
    private void MaxHeapify(T[] A, int heapSize, int i) {
        int l = left(i);
        int r = right(i);
        int best;
        if (r < heapSize && A[r].compareTo(A[i]) > 0) {
            best = r;
        } else {
            best = i;
        }

        if (l < heapSize && A[l].compareTo(A[best]) > 0) {
            best = l;
        }

        if (best != i) {
            swap(A, i, best);
            MaxHeapify(A, heapSize, best);
        }
    }

    /**
     *
     * @param Aprime
     */
    public void buildMaxHeap(T[] Aprime) {
        int mid = Math.floorDiv(Aprime.length - 1, 2) ;
        for (int i = mid; i >= 0; i--) {
            MaxHeapify(Aprime, Aprime.length, i);
        }
    }
    
    
    
    /**
     * Returns sorted array by performing a heapsort.
     *
     * @return
     */
    public T[] sorted() {
        System.out.println("Heap Sort Execution: Starting");
        T[] a = Arrays.copyOf(A, A.length);
        int n = a.length;
        for (int i = n - 1; i > 0; i--) { 
            //loops from n-1 to 1
            swap(a, 0, i);
            MaxHeapify(a, i ,0);
        }
        System.out.println("Heap Sort Execution: Finished");
        return a;
    }

    @Override
    public String toString() {
        return MyUtils.Stringify(A);
    }

}
