import re
import ftfy
from pathlib import Path
#from mask_functions import *


def clean_bert(texto):

    """
        Cleans a text based on bad Unicode and other characters

        Parameters
        -----------
        texto:  str
            A piece of text


        Returns
        -----------
        str
            Fixed text

    """

        
    txt = ftfy.fix_text(texto)
    txt=result.replace("\n", " ")
    txt=re.sub(' +', ' ', txt)
    return(txt)

def clean(texto, lower=True, return_masked=False):  

    """
        Cleans a text by removing general patterns, such as url, email, acronyms and other symbols, plural
        of words and specific Portuguese-related grammar

        Parameters
        -----------
        texto:  str
            A piece of text

        lower: bool
            Whether text is lowercase (Default: True)

        return_masked: bool
            Whether to return masked text (Default: False)


        Returns
        -----------
        dict
            Clean text

        dict
            Masked text if return_masked = True

    """
        
    dic={}
    
    #Limpeza geral
    dic['txt'], dic['url']=mask_url(texto) #Remove URLs
    dic['txt'], dic['email']=mask_email(dic['txt']) #Remove emails
    dic['txt']=re.sub("([A-Z])\.", r"\1", dic['txt']) #Siglas (e.g., C.P.F => CPF)
    if lower: dic['txt']=dic['txt'].lower() #Tornando letras minúsculas
    dic['txt']=re.sub("s[\/\.]a", " sa ",dic['txt'], flags=re.I) #s.a ou s/a => sa
    dic['txt']=dic['txt'].replace(" - - ", " - ")
    dic['txt']=dic['txt'].replace(" - ", " - - ")
    dic['txt']=re.sub("(\W)", r" \1 ", dic['txt']) #Colocando espaço aos lados dos símbolos 
    dic['txt']=dic['txt'].replace("\n", " ")
    dic['txt']=dic['txt'].replace("\t", " ")
    
    #Possíveis plurais e gênero
    dic['txt']=dic['txt'].replace("( s )", "(s)")
    dic['txt']=dic['txt'].replace("( a )", "(a)")
    dic['txt']=dic['txt'].replace("( as )", "(as)")
    dic['txt']=dic['txt'].replace("( o )", "(o)")
    dic['txt']=dic['txt'].replace("( os )", "(os)")
    
    #Juntando algumas strings
    dic['txt']=re.sub("(?<=\d) [-\.] (?=\d)", '', dic['txt'])
    dic['txt']=re.sub("(?<=\d) , (?=\d)", ',', dic['txt'])
    dic['txt']=dic['txt'].replace("[ email ]", "[email]")
    dic['txt']=dic['txt'].replace("[ url ]", "[url]")
    dic['txt']=re.sub("(\w) - (\w)", r"\1-\2", dic['txt']) # (e.g., arquivem - se => arquivem-se) 
    dic['txt']=re.sub(' +', ' ', dic['txt'])
    
    #Mascarando
    dic['txt'], dic['oab']=mask_oab(dic['txt'])
    dic['txt'], dic['data']=mask_data(dic['txt'])
    dic['txt'], dic['processo']=mask_processo(dic['txt'])
    dic['txt'], dic['valor']=mask_valor(dic['txt']) #Consideramos que as casas decimais são dadas pela vírgula
    dic['txt'], dic['numero']=mask_numero(dic['txt'])
    
    #Extra spaces
    dic['txt']=re.sub(' +', ' ', dic['txt']) 
    dic['txt']=dic['txt'].strip()
    
    #Output
    if return_masked:
        return dic
    else: 
        return dic['txt']
