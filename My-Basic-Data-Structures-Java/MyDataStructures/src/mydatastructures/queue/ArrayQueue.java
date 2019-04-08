/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.queue;

import java.lang.reflect.Array;
import java.util.StringJoiner;

public class ArrayQueue<T> extends MyQueue<T> {

    T[] arr;
    int head;
    int tail;

    public ArrayQueue(Class clazz, int size) {
        arr = (T[]) Array.newInstance(clazz, size+1);
        head = 0;
        tail = 0;
    }

    public void Enqueue(T element) {
        if (!isFull()) {
            arr[tail] = element;
            tail = nextSlot(tail);
        }else{
            throw new IllegalStateException("Queue is full");
        }
    }

    public T Dequeue() {
        T ele = null;
        if (!isEmpty()) {
            ele = arr[head];
            arr[head] = null;
            head = nextSlot(head);
        }else{
            throw new IllegalStateException("No dequeue from empty");
        }
        return ele;
    }

    private boolean isEmpty() {
        return head == tail;
    }

    private boolean isFull() {
        return nextSlot(tail) == head;
    }

    private int nextSlot(int p) {
        return (p + 1) % arr.length;
    }

    @Override
    public String toString() {
        StringJoiner buff = new StringJoiner(",");
        for (int i = head; i < tail; i++) {
            buff.add(arr[i].toString());
        }
        return buff.toString();
    }
}
