import sys,os
sys.path.append('/mnt/nvme0n1/zhangzheng/workspace')
from CloneLLM.clone_llm.clone_llm import CloneLLM
if __name__ == '__main__':
    model = CloneLLM(logfile_path= sys.argv[1],model_name=sys.argv[2],api_key=sys.argv[3],url=sys.argv[4])
    result = model.ask('最强大的大模型是哪个模型')
    print(result)