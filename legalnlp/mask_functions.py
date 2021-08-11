import re

def mask_email(txt):
    pattern=r'[^\s]+@[^\s]+'
    sub=' [email] '
    return re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)

def mask_url(txt):
    pattern='http\S+'
    pattern2='www\S+'
    sub=' [url] '
    txt, find = re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)
    txt, find2 = re.sub(pattern2, sub, txt, flags=re.I), re.findall(pattern2, txt, flags=re.I)
    return txt, find+find2

def mask_oab(txt):  
    find=[]
    pattern='OAB\s?[:-]?\s?\d+\s?/?\s?[A-Z]?[A-Z]?'
    pattern2='OAB\s?/?\s?[A-Z]?[A-Z]?\s?[:-]?\s?\d+'
    pattern3='\s\d+\s?/\s?[A-Z][A-Z]'
    sub=' [oab] '
    txt, find = re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)
    txt, find2 = re.sub(pattern2, sub, txt, flags=re.I), re.findall(pattern2, txt, flags=re.I)
    txt, find3 = re.sub(pattern3, sub, txt, flags=re.I), re.findall(pattern3, txt, flags=re.I)
    return txt, find+find2+find3

def mask_data(txt):
    pattern="\d{2}\s?\/\s?\d{2}\s?\/\s?\d{4}"
    sub=' [data] '
    return re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)

def mask_processo(txt, num=20):
    pattern="\d{"+str(num)+",}" #consideramos números com mais de 15 dígitos como sendo o número de um processo
    sub=' [processo] '
    return re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)

def mask_numero(txt):
    pattern="\d+"
    sub=' [numero] '
    return re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)

def mask_valor(txt):
    pattern="R\s?\$\s?\d+[.,]?\d+[.,]?\d+"
    sub=' [valor] '
    return re.sub(pattern, sub, txt, flags=re.I), re.findall(pattern, txt, flags=re.I)