/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mydatastructures.utils;

import java.util.Collection;
import java.util.Iterator;
import java.util.StringJoiner;

/**
 *
 * @author PC
 */
public class MyUtils {

    public static <T> String Stringify(T[] arr) {
        StringJoiner strJoiner = new StringJoiner(",");
        for (T element : arr) {
            strJoiner.add(element.toString());
        }
        return new StringBuilder("[").append(
                strJoiner.toString()).append("]").toString();
    }

    public static String Stringify(Collection collection) {
        StringJoiner strJoiner = new StringJoiner(",");
        Iterator iter = collection.iterator();
        while (iter.hasNext()) {
            strJoiner.add(iter.next().toString());
        }
        return new StringBuilder("[").append(
                strJoiner.toString()).append("]").toString();
    }

}
