# Linux DeepLearning tools
These are some useful tools to use with Linux (focus on Ubuntu) when working with Deep Learning.

# Linux system:
  - htop: to view in %CPU uses by threads, %RAM: kill thread, filter, search,...
  - ncdu: to view files/folders size over local or ssh
  - find file/folder in Linux:
    - find -name "\*ASR\*" : find all file/dir name include ASR
    - find -typy d -name "\*ASR\*" : find all *dir* name include ASR
    - find -type f -name "*libcudart*"   : find all files libcudart.so.* in current folder
    - find -type f -name "*libcudnn.so*"   : find all files libcudnn.so.*

# Check Envs for Deep Learning:
  - nvidia-smi
  - nvcc -V
  - find -type f -name "*libcudnn.so*"
  - nvidia-smi --format=csv --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
  - nvidia-smi --format=csv,noheader --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
  - nvidia-smi --format=csv --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics

  # Install Deeplearning Libraries:
  - PYTHON - AUTO GENERATE REQUIREMENTS.TXT:
  
    Method 1:
      * pip freeze > requirements.txt   

    Method 2:
      * pip install pipreqs
      * pipreqs /path/to/project
    (to install: pip install -r requirements.txt)
      
  - pip install python-levenshtein
  - 
  
  # Python functions List:
   - (def LastNlines(NLs=15,LineContainKey="Key to Fine"))   [https://github.com/holianh/Linux_DeepLearning_tools/blob/master/python_funcs_codes.py#L7]
   - ( Plot history and accuray when training with Keras to PDF)[https://github.com/holianh/Linux_DeepLearning_tools/blob/master/python_funcs_codes.py#L38]
   - (Save data to json file)[https://github.com/holianh/Linux_DeepLearning_tools/blob/master/python_funcs_codes.py#L113] 
   - (Files_2csv_inDir: Find and Add All wav & label files to *.CSV)[https://github.com/holianh/Linux_DeepLearning_tools/blob/master/python_funcs_codes.py#L130]
   - (Timing: Calculate running time)[https://github.com/holianh/Linux_DeepLearning_tools/blob/master/python_funcs_codes.py#L174] 
   - ()[]
   - ()[] 
   - ()[]
   - ()[] 
   - ()[]
   - ()[] 
   - ()[]
   - ()[] 
   - ()[]
   - ()[] 
   - ()[]
   
   
   
   
   
   
   
   
   
   
