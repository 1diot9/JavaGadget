# JavaGadget

此项目记录我在Java安全学习过程中遇到的一些利用链或恶意服务等Payload，便于自己的复习和使用。

目前打算按照：

readObject-->toString

toString-->getter

Sink

这样的形式去分段整理利用链。

另外，像CC，JDBC这种常见，但是不太适合归类到分段利用链里的，会单独创建文件夹。



**idea项目中，exp一般都位于 com.test.exp 中。**



当前目录结构：

|-- CC

|-- Gadget  按照 readObject2toString 整理

|-- JDBC

|-- PyScript  整理用到的py脚本，目录结构与最外层一致

|-- README.md

`-- docs   文档整理，简单分析利用链，方便使用时查找