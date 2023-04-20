from slangtranslator.styleformer.styleformer import Styleformer
import warnings
warnings.filterwarnings("ignore")
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1234)
 
source_sentences = [
"OMG! It's finger-lickin' good."
] 
# style = [0=Casual to Formal, 1=Formal to Casual, 2=Active to Passive, 3=Passive to Active etc..]
sf = Styleformer(style = 0) 

def results(source):
    for source_sentence in source:
    # inference_on = [-1=Regular model On CPU, 1= Regular model On GPU, 2=Quantized model On CPU]
        target_sentence = sf.transfer(source_sentence, inference_on=-1, quality_filter=0.95, max_candidates=5)
        return(target_sentence)
        
    

