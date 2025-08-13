import re
import os
os.environ['HUGGINGFACEHUB_API_TOKEN']='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'
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

#Analyser
def read_source_code(file_path):
    with open(file_path,'r') as file:
        source_code=file.read()
    return source_code

#Collecting comments
def extract_comments(source_code):
    # Pattern to match multi-line comments enclosed within triple single quotes
    triple_single_quote_pattern = r"'''(?:.|\n)*?'''"
    triple_single_quote_comments = re.findall(triple_single_quote_pattern, source_code, re.DOTALL)
    list_1_3_quote=[]
    for i in triple_single_quote_comments:
        list_1_3_quote.append(i.strip("''"))
    # Pattern to match multi-line comments enclosed within triple double quotes
    triple_double_quote_pattern = r'"""(?:.|\n)*?"""'
    triple_double_quote_comments = re.findall(triple_double_quote_pattern, source_code, re.DOTALL)
    list_2_3_quote=[]
    for i in triple_double_quote_comments:
        list_2_3_quote.append(i.strip('""'))
    # Pattern to match inline comments starting with n python or //# in c++/c/java/javascript
    inline_pattern = r'#//.*?$|//#.*?$'#// i
    inline_comments = re.findall(inline_pattern, source_code, re.MULTILINE)
    list_inline_comment=[]
    for i in inline_comments:
        list_inline_comment.append(i[4:])
    # Pattern to match multi-line comments enclosed within /*
    multiline_pattern_c = r'\/\*[\s\S]*?\*\/'
    multiline_comments_c = re.findall(multiline_pattern_c, source_code, re.DOTALL)
    list_multiline_comments_c=[]
    for i in multiline_comments_c:
        list_multiline_comments_c.append(i[3:-2])
    
    return list_1_3_quote+list_2_3_quote+list_inline_comment+list_multiline_comments_c

# Pattern to match comments starting with (#/@ cette class in python OR //@ cette class in c++/c/java/javascript) for a class
def extract_class(source_code):
    class_pattern=r'^#/@ cette class.*|^[ ]*//@ cette class.*'
    class_comments=re.findall(class_pattern,source_code,re.MULTILINE)
    list_class_comment=[]
    for i in class_comments:
        list_class_comment.append(i[4:])
    return list_class_comment
    
#Pattern to match inline comments starting with (#/@ cette fonction in python OR //@ cette fonction in c++/c/java/javascript) for a function
def extracte_funct(source_code):
    funct_pattern=r'^#/@ cette fonction.*|^[ ]*//@ cette fonction.*'
    funct_comments=re.findall(funct_pattern,source_code,re.MULTILINE)
    list_funct_comment=[]
    for i in funct_comments:
        list_funct_comment.append(i[4:])
    return list_funct_comment

#Pattern to match Imports
def extract_imports(source_code):
    imports_pattern=r'import.*|import.*$;'
    imports=re.findall(imports_pattern,source_code)
    return imports

#Pattern to match Includes
def extract_includes(source_code):
    include_pattern=r'#include.*'
    includes=re.findall(include_pattern,source_code)
    return includes

#AI
def explanations(comments):
    list_exp=[]
    for comment in comments:
        template="""{comment}
        Explanation:this means that it"""
        prompt=PromptTemplate(template=template,input_variables=["comment"])
        llm_chain=LLMChain(prompt=prompt,llm=HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.2",model_kwargs={"temprature":0,"max_lenght":64}))
        list_exp.append(llm_chain(comment))
    return list_exp

file_path="C:/Users/MA21/Desktop/USJ/ESIB Maths spe/Semestre 2/Projet d'initiation dans l'ingenierie/Projet Code/Projet Code/python_script.py" #python_script
#file_path="C:/Users/MA21/Desktop/USJ/ESIB Maths spe/Semestre 2/Projet d'initiation dans l'ingenierie/Projet Code/Projet Code/c++_script.cpp" #c++_script
#file_path="C:/Users/MA21/Desktop/USJ/ESIB Maths spe/Semestre 2/Projet d'initiation dans l'ingenierie/Projet Code/Projet Code/java_script.java" #java_script
source_code=read_source_code(file_path)
comments=extract_comments(source_code)
classes=extract_class(source_code)
functions=extracte_funct(source_code)
imports=extract_imports(source_code)
includes=extract_includes(source_code)
print(comments)
print()
print(classes)
print()
print(functions)
print()
print(imports)
print()
print(includes)
print()
total_comments=comments+classes+functions+imports+includes
list_dic=explanations(total_comments)
print(list_dic)

list_info=[]
for dictionaire in list_dic:
    dic={}
    for key,value in dictionaire.items():
        if key=='comment':
            dic["Comment"]=value
        else:
            clean_value_list=value.split(":")
            print(clean_value_list)
            exp=""
            for letter in clean_value_list[1]:
                if letter!=".":
                     exp=exp+letter
                else:
                    break
            dic["Explination"]=exp
    list_info.append(dic)
print(list_info)

with open('Explanation','w') as f:
    f.write('')

for dic in list_info:
    for key,val in dic.items():
        with open('Explanation','a') as f:
            f.write(key+":")
            f.write(val+"\n")
    with open('Explanation','a') as f:
        f.write("\n\n")

#quelques exemplaires de Shortcuts:
#Ctrl+M=
#Ctrl+N=
#Ctrl+O=
#Ctrl+P=