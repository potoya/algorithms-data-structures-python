/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.stack;

import java.lang.reflect.Array;
import java.util.StringJoiner;

public class ArrayStack<T> extends MyStack<T> {

    private T[] arr;
    private int top;

    public ArrayStack(Class clazz, int size) {
        this.arr = (T[]) Array.newInstance(clazz, size);
        this.top = 0;
    }

    @Override
    public void push(T element) {
        if(top < arr.length){
            arr[top++] = element;
        }else{
            throw new IllegalStateException("Stack Overflow");
        }
    }

    @Override
    public T pop() {
        if(isEmpty()){
            throw new IllegalStateException("Stack is empty nothing to pop");
        }else{
            return arr[top--];
        }
    }

    @Override
    public boolean isEmpty() {
        return top == 0;
    }
    
    @Override
    public String toString(){
        StringJoiner buff = new StringJoiner(",");
        for(int i = 0 ; i < top ; i++){
            buff.add(arr[i].toString());
        }
        return buff.toString();
    }

}
