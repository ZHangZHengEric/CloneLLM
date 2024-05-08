# 这里面封装一个可以保存日志的api调用，利用openai 的api

from openai import OpenAI
import time
class AutoLLMAPI:
    def __init__(self,api_key,base_url,model_name) -> None:
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model_name = model_name
    
    def ask(self,messages,temperature,presence_penalty):
        if type(messages)==str:
            messages = [ 
                {"role": "user", "content": messages}
            ]
        start_time = time.time()
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            presence_penalty =presence_penalty
        )
        return_content = completion.choices[0].message.content
        print('使用模型',self.model_name,'推理耗时',time.time()-start_time)
        self.check_time = 0
        return return_content,messages
        