/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.stack;

/**
 *
 * @author PC
 * @param <T>
 */
public abstract class MyStack<T> {

    public void pushAndPrint(T element) {
        push(element);
        System.out.println(toString());
    }

    public void popAndPrint() {
        pop();
        System.out.println(toString());
    }

    public abstract void push(T element);

    public abstract T pop();

    public abstract boolean isEmpty();
}
