
def load_memory():

    learned_concepts = ""
    
    raw_signature = ""
    raw_keywords = [] 
    
    signature_keywords = ""
    
    keyword = ""
    keyword_weight = 0
    keyword_link_weight = 0
    keyword_links = ""

    keyword_links = [keyword, keyword_link_weight]
    raw_memory = [keyword, keyword_links, learned_concepts, signature_keywords]
    learned_signatures = [learned_concepts, raw_keywords, raw_signature, raw_memory] 
    
    classification_keywords_array = [learned_concepts, keyword, keyword_weight, keyword_links] 

    # Memory datas structure
    memory = [concepts, 
             signatures]  
    return True

def read_classify_text():
    classification = ""
    return classification