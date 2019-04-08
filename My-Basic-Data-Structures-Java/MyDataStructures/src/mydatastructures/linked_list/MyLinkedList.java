/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.linked_list;

import java.util.StringJoiner;

/**
 *
 * @author PC
 * @param <T>
 */
public class MyLinkedList<T> {

    Node<T> head;
    Node<T> tail;
    int size;
    
    public Node<T> findByKey(T key){
        Node<T> iter = head;
        for(; iter.key != key ; iter = iter.next);
        return iter;
    }
    
    public void pushBack(T key) {
        Node<T> node = new Node<>();
        node.key = key;
        node.next = null;
        if (tail == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        size++;
    }

    public void popBack() {
        if (head == null) {
            throw new IllegalStateException();
        }
        if (head == tail) {
            // If size == 1
            head = null;
            tail = null;
            size--;
        } else {
            tail = tail.prev;
            tail.next = null;
        }

    }

    public void addAfter(Node<T> node, T key) {
        Node<T> node2 = new Node(key);
        
        Node<T> nodesExNext = node.next;
        node.next = node2;

        node2.prev = node;
        node2.next = nodesExNext;

        if(node2.next != null){
            // node2 has a next for sure (e.g node2.next not tail)
            node2.next.prev = node2;
        }
        
        if (tail == node) {
            tail = node2;
        }
    }
    
    public void addBefore(Node<T> node, T key){
        Node<T> nodePrime = new Node(key);
        
        Node<T> nodesExPrev = node.prev;
        nodePrime.next = node;
        nodePrime.prev = nodesExPrev;
        
        node.prev = nodePrime;
        
        if(nodePrime.prev != null){
            //NodePrime is not the head
            nodesExPrev.next = nodePrime;
        }
        
        if(head == node){
            head = nodePrime;
        }
        
    }

    @Override
    public String toString() {
        Node<T> iter = head;
        StringJoiner stringJoiner = new StringJoiner(",");
        while (iter != null) {
            stringJoiner.add(iter.key.toString());
            iter = iter.next;
        }
        return "[" + stringJoiner.toString() + "]";
    }

}

class Node<T> {

    T key;
    Node<T> next;
    Node<T> prev;

    Node() {
    }

    Node(T key) {
        this.key = key;
    }

    @Override
    public String toString() {
        return new StringBuilder().append('{')
                .append(" key = ").append(key)
                .append(" ")
                .append("next.key = ").append(next.key)
                .append(" ")
                .append("next.prev = ").append(prev.key)
                .toString();
    }
    
    
}
