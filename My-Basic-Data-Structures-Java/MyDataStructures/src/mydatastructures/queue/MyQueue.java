/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.queue;

/**
 *
 * @author PC
 * @param <T>
 */
public abstract class MyQueue<T> {
    
    public abstract void Enqueue(T element);
    
    public abstract T Dequeue();
    
}
