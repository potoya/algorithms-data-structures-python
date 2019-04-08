/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.excercises;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import mydatastructures.stack.LinkedListStack;
import mydatastructures.stack.MyStack;

/**
 *
 * @author PC
 */
public class CheckParenthesis {

    public static void main(String[] args) throws IOException {
        BufferedReader stdInReader = new BufferedReader(
                new InputStreamReader(System.in));
        while (true) {
            System.out.print(">");
            String codeToCheck = stdInReader.readLine();
            print(check(codeToCheck));
        }
    }

    public static String check(String codeToCheck) {
        List<CodeSymbol> codeSymbols = CodeSymbol.convertToCodeSymbol(
                codeToCheck, new ArrayList<>());

        // Case 1: {[pedro ss][dk] => 1
        // Case 2: {} => Success
        MyStack<CodeSymbol> stack = new LinkedListStack<>();
        
        for (int i = 0; i < codeSymbols.size(); i++) {
            CodeSymbol codeSymbol = codeSymbols.get(i);
        
            if (codeSymbol.isOpenParen()) {
                stack.push(codeSymbol);
            
            }else if(codeSymbol.isClosingParen()){
            
                //Then this closing guy should match the Opened one atop Stack
               CodeSymbol openerCodeSymbol = stack.pop();
               if(!openerCodeSymbol.isClosedBy(codeSymbol)){
                   return String.valueOf(openerCodeSymbol.index);
               }
            
            }
        }
        
        return stack.isEmpty() ? "Success" : 
                String.valueOf(stack.pop().index);
    }

    public static void print(Object o) {
        System.out.println(o.toString());
    }

}

// Class representing a code symbol.
class CodeSymbol {

    String symbol;
    int index;

    CodeSymbol(String symb, int ind) {
        symbol = symb;
        index = ind;
    }
    
    boolean isOpenParen(){
        return this.symbol.matches("\\{|\\(|\\[");
    }
    
    boolean isClosingParen(){
        return this.symbol.matches("\\}|\\)|\\]");
    }
    
    boolean isClosedBy(CodeSymbol potentialClosingParen){
        switch(potentialClosingParen.symbol){
            case ")":
                return this.symbol.equals("(");
            case "}":
                return this.symbol.equals("{");
            case "]":
                return this.symbol.equals("[");
            default:
                return false;
        }
    }
    
    static List<CodeSymbol> convertToCodeSymbol(String codeToConvert, 
            List<CodeSymbol> sink) {
        String[] symbols = codeToConvert.split("");
        for (int i = 0; i < symbols.length; i++) {
            sink.add(new CodeSymbol(symbols[i], i));
        }
        return sink;
    }

}
