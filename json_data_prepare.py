# 将本地pdf的书籍向量化后存储到database中
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json

loader = PyPDFLoader(
    "./data/红楼梦 [Hong Lou Meng (2-volume-set, 120 chapters 3rd ed. 2008] (曹雪芹, 高鹗, 程伟元) (Z-Library).pdf"
)
pages = loader.load_and_split()
print(type(pages[0]))
print(type(pages[0].page_content))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=10,
    length_function=len,
    add_start_index=True,
)

texts = text_splitter.split_documents(pages)
texts = text_splitter.split_documents(pages)
print(f"Split the pages in {len(texts)} chunks")


with open("./data/honglou-book.jsonl", "w", encoding="utf-8") as f:
    for text in texts:
        f.write(
            json.dumps(
                {"content": text.page_content, "page": text.metadata["page"]},
                ensure_ascii=False,
            )
        )
        f.write("\n")
