# CloneLLM
将你喜欢的模型的能力克隆到自己的模型上。
先用当前较为优秀的模型的api进行线上跑效果。然后使用该模型讲较好模型的能力复制到自己的模型上。

# 使用说明

## 使用clone llm api 自动保存日志

```
from CloneLLM.clone_llm.clone_llm import CloneLLM
if __name__ == '__main__':
    model = CloneLLM(logfile_path= ,model_name= ,api_key= ,url= )
    result = model.ask('最强大的大模型是哪个模型')
    print(result)
```
使用 ```model.ask()``` 的过程则自动将日志保存到logfile_path 中

model.ask() 多轮对话输入格式
```
messages = [
                {"role":"user","content":"你好"},
                {"role":"assistant","content":"你好"},
                {"role":"user","content":"介绍一下你自己"}
            ]
result = model.ask(messages)
```

## 对日志进行标注是否是满意答案
```
python script/label_log.py logfile_path
```
会打开一个gradio的标注界面，标注结果保存在logfile_path同级目录下的labeled_filename 位置。

## 将标注结果的可训练部分转化成Atom格式的标准文件以及训练文件

标准文件方便后续其他训练从中提取数据
```
python script/convert_to_standard.py data/labeled_temp.jsonl data/standard_temp.json
```
会生成standard_temp.json 标准文件，以及对应的训练文件，train_standard_temp.csv

TODO

- [x] 搭建好整体的框架
- [x] 实现支持openai的api的调用代码，并且自动保存下log
- [] ppo的奖励函数实现
- [x] 数据标注的gradio 的界面
- [] sft训练代码
- [] ppo训练代码
- [] dpo进行训练
- [] 模型增量训练更新