import gradio as gr
import json
import os,sys
def load_log_json(json_path):
    if os.path.exists(json_path)==False:
        return []
    f= open(json_path)
    all_data = f.readlines()
    for i in range(len(all_data)):
        all_data[i] = json.loads(all_data[i])    
    f.close()
    return all_data


if __name__ == '__main__':
    origin_file = sys.argv[1]
    labeled_file = os.path.join(os.path.dirname(origin_file),'labeled_'+os.path.basename(origin_file))
    all_data = load_log_json(origin_file)
    labeled_data  =load_log_json(labeled_file)
    label_index = len(labeled_data)
    def convert_convsersation_md(item):
        conversations = item['conversations']
        conversations_md = ''
        for one_ in conversations:
            conversations_md += '## '+one_['role']+':\n\n'+one_['content']+'\n\n'
        return conversations_md
    with gr.Blocks() as demo:
        with gr.Row():
            content_data_gr = gr.Markdown( convert_convsersation_md(all_data[label_index]) )
            with gr.Column():
                accept_label_bt = gr.Button(value='接受')
                refuse_label_bt = gr.Button(value='拒绝')
        
        def accept_():
            global all_data,label_index
            all_data[label_index]['label']='yes'
            labeled_data.append(all_data[label_index])
            labeled_logfile = open(labeled_file,'+a')
            labeled_logfile.write(json.dumps(all_data[label_index],ensure_ascii=False)+'\n')
            labeled_logfile.close()
            label_index+=1
            if label_index>= len(all_data):
                return '# 数据集已经标注完成'
            return convert_convsersation_md(all_data[label_index])
        accept_label_bt.click(accept_,[],content_data_gr)
        
        def refuse_():
            global all_data,label_index
            all_data[label_index]['label']='no'
            labeled_data.append(all_data[label_index])
            labeled_logfile = open(labeled_file,'+a')
            labeled_logfile.write(json.dumps(all_data[label_index],ensure_ascii=False)+'\n')
            labeled_logfile.close()
            label_index+=1
            if label_index>= len(all_data):
                return '# 数据集已经标注完成'
            return convert_convsersation_md(all_data[label_index])
        refuse_label_bt.click(refuse_,[],content_data_gr)
    demo.queue().launch(share=False,debug = True,server_port=21230)