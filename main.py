from llama_cpp import Llama
from duckduckgo_search import DDGS

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path=r"B:\AI\Mistral\TheBloke\dolphin-2.2.1-mistral-7b.Q5_K_M.gguf\dolphin-2.2.1-mistral-7b.Q5_K_M.gguf", 
  n_ctx=2048,  
  n_threads=4,            
  n_gpu_layers=35,
  n_batch=512    
)

while True:
     
    system1 = """You are an AI model that is trained in tool and function calling. Think through the question, and return what all functions to call and how to call them, to give the best response to user's question.
    These are the tools avaliable to you:
    
    Google(): This function googles any query that you feel can't be answered like real events.
    calc_no(): This function is used to calculate numbers.
    None(): This function is used when you feel that the user's query does not need the use of google or cannot be answered.
    
    Respond only in this JSON format, with no extra text.
    {
        "thought":"thought of the LLM about which tool to use",
        "tool": "google()" or "calc_no" or "none()"
    }
    """
    prompt = input("Enter question ")

    output = llm(
    "<|im_start|>system {}<|im_end|>\n<|im_start|>user {}<|im_end|>\n<|im_start|>assistant".format(system1,prompt),
    max_tokens=-1,
    stop=["<|im_start|>","<|im_end|>"],
    temperature=0.8,
    top_k=40,
    repeat_penalty=1.1,
    min_p=0.05,
    top_p=0.95,
    echo=False
    )
    search_list = output['choices'][0]['text']
    print(search_list)