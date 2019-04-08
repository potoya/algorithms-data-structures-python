/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.stack;

import java.util.StringJoiner;

public class LinkedListStack<T> extends MyStack<T> {

    Node<T> top = null;
    
    @Override
    public void push(T element) {
        if (top == null) {
            top = new Node(element, null);
        } else {
            Node<T> newNode = new Node(element, top);
            top = newNode;
        }
    }

    @Override
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        } else {
            Node<T> temp = top;
            top = temp.below;
            return temp.element;
        }
    }

    @Override
    public boolean isEmpty() {
        return top == null;
    }

    @Override
    public String toString() {
        mydatastructures.stack.Node<T> iter = top;
        StringJoiner stringJoiner = new StringJoiner(",");
        while (iter != null) {
            stringJoiner.add(iter.element.toString());
            iter = iter.below;
        }
        return "[" + stringJoiner.toString() + "]";
    }
}

class Node<T> {

    T element;
    Node<T> below;

    Node(T e, Node<T> b) {
        element = e;
        below = b;
    }
}
