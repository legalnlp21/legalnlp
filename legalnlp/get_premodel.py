import wget
import zipfile


def get_premodel(model):
    d = None
    if model == 'bert':
        # BERTikal
        url = 'https://ndownloader.figshare.com/files/29110152'
        filename = wget.download(url, out=d)
        if d == None:
            d = ''
        with zipfile.ZipFile(d+filename, "r") as zip_ref:
            zip_ref.extractall(d+filename.replace('.zip', ''))
    # Download Word2Vec Continuous Bag-of-Words (CBOW) or Doc2Vec Distributed Memory (DM)
    if model == 'wdocdm':
        url2 = 'https://ndownloader.figshare.com/files/29110809'
        filename2 = wget.download(url2, out=d)
        if d == None:
            d = ''
        with zipfile.ZipFile(d+filename2, "r") as zip_ref:
            zip_ref.extractall(d+filename2.replace('.zip', ''))
    # Download Doc2Vec Distributed Bag-of-Words (DBOW) or Word2Vec Skip-Gram (SG)
    if model == 'wdocdbow':
        url2 = 'https://ndownloader.figshare.com/files/29138835'
        filename2 = wget.download(url2, out=d)
        if d == None:
            d = ''
        with zipfile.ZipFile(d+filename2, "r") as zip_ref:
            zip_ref.extractall(d+filename2.replace('.zip', ''))
    return
