/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.queue;

import java.util.StringJoiner;
import mydatastructures.stack.LinkedListStack;
import mydatastructures.stack.MyStack;

public class DoubleStackQueue<T> extends MyQueue<T> {

    private MyStack<T> stack1;
    private MyStack<T> stack2;

    public DoubleStackQueue() {
        super();
        stack1 = new LinkedListStack<>();
        stack2 = new LinkedListStack<>();
    }

    @Override
    public void Enqueue(T element) {
        stack1.push(element);
    }

    @Override
    public T Dequeue() {
        if (stack2.isEmpty()) {
            // stack2 has no elements
            moveAllFromStack1ToStack2();
        }
        return stack2.pop();
    }
    
    private void moveAllFromStack1ToStack2(){
        while(!stack1.isEmpty()){
            stack2.push(stack1.pop());
        }
    }
    
    @Override
    public String toString(){
        StringJoiner sj = new StringJoiner("\n");
        return sj.add("Stack 1: ["+ stack1.toString() +"]")
          .add("Stack 2: ["+ stack2.toString() +"]")
                .toString();
    }
    
}
