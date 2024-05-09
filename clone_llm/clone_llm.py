from CloneLLM.clone_llm.llm_api import AutoLLMAPI
from datetime import datetime
import json
class CloneLLM:
    def __init__(self,logfile_path,model_name,api_key,url) -> None:
        self.logfile_path = logfile_path
        self.model = AutoLLMAPI(api_key,base_url=url,model_name=model_name)
        pass
    
    def clone_one_question_answer(self,question,temperature=0.4,presence_penalty=1.2):
        result,input_messages = self.model.ask(messages=question,temperature=temperature,presence_penalty=presence_penalty)
        input_messages.append({'role':'assistant','content':result})
        one_conversation = {'conversations':input_messages,'model':self.model.model_name,'date':datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        logfile = open(self.logfile_path,'+a')
        logfile.write(json.dumps(one_conversation,ensure_ascii=False)+'\n')
        logfile.close()
        return result

    def clone_questions_answer(self,questions):
        # 将大量的问题跑流程，下载下来问答对。
        for question in questions:
            self.clone_one_question_answer(question)
        
    def ask(self,question,temperature=0.4,presence_penalty=1.2):
        result,input_messages = self.model.ask(messages=question,temperature=temperature,presence_penalty=presence_penalty)
        input_messages.append({'role':'assistant','content':result})
        one_conversation = {'conversations':input_messages,'model':self.model.model_name,'date':datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        logfile = open(self.logfile_path,'+a')
        logfile.write(json.dumps(one_conversation,ensure_ascii=False)+'\n')
        logfile.close()
        return result