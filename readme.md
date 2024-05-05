## 辩论agent
本项目实现一个更加灵活的辩论agent，该agent能够结合红楼梦名著中的内容进行辩论
### 文件详情
- json_data_prepare.py——将pdf的原著进行切分后存储到jsonl文件中
- faiss_database.py——读取jsonl文件，并建立faiss数据库，文本经过m3e-base模型向量化后存入到faiss数据库中
- main.py——构建辩论的agent，并展示在前台页面上