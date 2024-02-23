# py_document_signing_tool

## 文档签名工具支持 doc ，docx ，xlsx ，xls ，pdf

## 困难

1. doc 转换 docx , xls 转换 xlsx
2. 签名如何定位
3. 签名如何生成
4. 工具应该支持离线部署，而非只能在线

## 项目介绍

### 项目背景

    1. 由于业务需要，需要对文档进行签名
    2. 由于签名的文档格式较多，需要支持 doc ，docx ，xlsx ，xls ，pdf
    3. 业务部署是在内网环境，无法链接互联网
    4. 文档格式千奇百怪，没有统一模版。

### 项目目的

    0. 这是本人的第一python项目，因此项目目的主要是学习python
    1. 通过python造一个轮子，解决业务问题
    2. 因为是是轮子，所以要有通用性
    3. 借此机会 研究一下 AI 使用 AI 实现签名的定位

### Day 1 2024-02-23 项目启动第一天

    1. python版本 3.8.8
    2. 在不同环境中 使用的 转换工具不一样，在windows 上使用的是 pywin32 + office ，在linux 上使用的是 unoconv + libreoffice 
    3. 先搞定ubuntu版本的吧。
    
    ```shell
        apt-get install unoconv libreoffice
    ```
    4. 一个很尴尬的问题 ，github 查看unoconv 文档时发现他不在维护了。而是换成了 unoserver 然后我安装文档换成了这个。但是但是，安装后 调用失败。

### Day 2 2024-02-24 项目启动第二天
