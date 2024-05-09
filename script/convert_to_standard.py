import json
import os,sys
from tqdm import tqdm
import pandas as pd
def load_log_json(json_path):
    if os.path.exists(json_path)==False:
        return []
    f= open(json_path)
    all_data = f.readlines()
    for i in range(len(all_data)):
        all_data[i] = json.loads(all_data[i])    
    f.close()
    return all_data

def convert_for_train(standard_data,save_path):
    new_conversations = []
    for one_conversations in tqdm(standard_data):
        one_new_conversations=[]
        for one_conversation in one_conversations['conversations']:
            one_new_conversations.append({'role':one_conversation['role'],'content':'<s>'+one_conversation['role']+': '+one_conversation['content'].strip()+'\n</s>',"is_trainable": (True if one_conversation['role'] in ['Assistant','AssistantTool'] else False)  })
        new_conversations.append(one_new_conversations)
    all_data_df = pd.DataFrame({'conversations':new_conversations})
    all_data_df.to_csv(save_path,index=False,quoting=1)
    

if __name__ == '__main__':
    all_data = load_log_json(sys.argv[1])
    accept_data = []
    for item in all_data:
        if item['label'] =='yes':
            for index,conversation in enumerate(item['conversations']):
                if item['conversations'][index]['role'] in ['user','human']:
                    item['conversations'][index]['role']='Human'
                elif item['conversations'][index]['role'] in ['assistant']:
                    item['conversations'][index]['role']='Assistant'
                elif item['conversations'][index]['role'] in ['system']:
                    item['conversations'][index]['role']='System'
            accept_data.append(item)
    json.dump(accept_data,open(sys.argv[2],'w'),ensure_ascii=False,indent=4)
    convert_for_train(accept_data,os.path.join( os.path.dirname(sys.argv[2]),'train_'+'.'.join(os.path.basename(sys.argv[2]).split('.')[:-1])+'.csv' ))
    