'''
Nguyen Tuan Anh, 2018-01-19
usful python functions
--------------------------
'''
########################################################################
# Extract N end lines contain "Key to find" from files  ----------------
########################################################################
def LastNlines(NLs=15,LineContainKey="Key to Fine"):
    #lss=glob.glob(clayPath+"*.txt")
    #newestFileindir = max(lss, key=os.path.getctime)
    newestFileindir ="/Path/to/file.txt"
    #print(newestFileindir)
    f = open(newestFileindir, 'rb'); strData = f.read().decode('utf8', 'ignore')
    
    data=strData.split('\n')
    Ndata=len(data)
    print('Ndata=',Ndata)
    Lines=[]
    NumberLine=0
    flag=True
    while flag:
        if NumberLine==NLs:
            return Lines
        if(data[Ndata-1].find(LineContainKey)>0):
            Lines.append(data[Ndata-1])
            NumberLine+=1
        if(Ndata>1):
            Ndata=Ndata-1
        else:
            return Lines
#Liness=LastNlines() 
#for s in Liness:print(s)
#exit()
    

########################################################################
# Plot history and accuray when training with Keras to PDF -------------
########################################################################
import matplotlib                                    ###############
matplotlib.use('agg')
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages

def hist(history,
         strNeedPlot=('loss','acc'),#,'loss'),#,'acc','loss','acc'),
         Labels=(['Training Loss'    ,'Epochs','Loss value'],
                 ['Training Accuracy','Epochs','Accuracy value'],
                 ['Label 3','X label3','Ylabel3'],
                 ['Label 4','X label4','Ylabel4'],
                 ['Label 5','X label5','Ylabel5'],
                 ['Label 6','X label6','Ylabel6'],
                 ),
          NoColumns=1,
          nb_plots_per_page = 3,               # Total number in one page to print.
          fdfName='history_training.pdf'
         ):
    # Plot history of training in keras to pdf
    # history=model.fit(...) in keras
    # history={'loss':[1,2,3,...n],'acc':[1,2,3,...,m]}
    # strNeedPlot=('loss','acc','loss','acc','loss')

    pdf_pages = PdfPages(fdfName)
    nb_plots = len(strNeedPlot)         # Number of images
    if(nb_plots_per_page>nb_plots):nb_plots_per_page=nb_plots;
    nb_pages = int(np.ceil(nb_plots / float(nb_plots_per_page)))#No of Pages
    grid_size = (nb_plots_per_page, NoColumns)  # Number of columns
    PaperSize=A4=(8.27, 11.69)          # paper size in inch
    i=0
    for sType in strNeedPlot:
        # Create a figure instance (ie. a new page) if needed
        if i % nb_plots_per_page == 0: fig = plt.figure(figsize=PaperSize, dpi=100) 
        # Plot stuffs !
        ax=plt.subplot2grid(grid_size, (i % nb_plots_per_page, 0))
        plt.subplots_adjust(wspace=0, hspace=.5)
        plt.subplots_adjust(left=0.2)
        plt.subplots_adjust(top=0.88)
        plt.plot(history.history[sType])
        
        ax.set_title(Labels[i][0])
        plt.xlabel(Labels[i][1], fontsize=14)
        plt.ylabel(Labels[i][2], fontsize=14)
        
        # Close the page if needed
        if (i + 1) % nb_plots_per_page == 0 or (i + 1) == nb_plots:
            #plt.tight_layout()
            pdf_pages.savefig(fig)
        i+=1
        ''' #examples
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)
        ax1.title.set_text('First Plot')
        ax2.title.set_text('Second Plot')
        ax3.title.set_text('Third Plot')
        ax4.title.set_text('Fourth Plot')
        plt.show()
        '''
    # Write the PDF document to the disk
    pdf_pages.close()
    print(fdfName + " - already save successful!")
    print("to view, please see at:" + os.getcwd())
    # How to use:
    #   history = model.fit(x_data, y_data, epochs=5000,verbose=1)
    #   hist(history)

# hist(history)    
# exit()

########################################################################
# Save data to json file -----------------------------------------------
########################################################################
FnSave='test.txt'
import io, json
data = {'DataHome':DataHome,
        'Wav_path':Wav_path,
        'DataPath':Wav_path
        }
with io.open(FnSave, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)
#uses:
#with open(FnSave) as data_file:data_loaded = json.load(data_file)
#print(data_loaded['DataPath'])
########################################################################

########################################################################
# Files_2csv_inDir -----------------------------------------------------
# Find and Add All wav & label files to *.CSV
########################################################################
import os
from random import shuffle
Wav_path='/home/tact/AudioDBs/All_DataBase/'#
sNeedRemove='/home/tact/AudioDBs/All_DataBase' # loại bỏ đường dẫn dư thừa.
# .....
#--------------- --------------- --------------- ---------------
def Files_2csv_inDir(path, wav_ext, lbl_ext):
    count = 0
    Fis=[]
    for subdir, dirs, files in os.walk(path):
        for fi in files:
            if fi.endswith(wav_ext): # eg: '.txt'
                count += 1
                ph=subdir.replace(sNeedRemove,'')
                Fis.append(ph+'/'+fi)
    shuffle(Fis)
    Full_len=len(Fis)
    train_len= round(Full_len * 0.8)
    test_len = Full_len - train_len
    
    print(train_len,test_len)
    fn=open(csv_path+'data_train_path.csv','w')
    ft=open(csv_path+'data_test__path.csv','w')
    
    k=0
    for item in Fis:
        k+=1
        if(k<train_len): fn.write("%s\n" % item)
        else:            ft.write("%s\n" % item)
    fn.close()
    ft.close()
    return count
''' #--------------- --------------- --------------- ---------------
/home/tact/ta/asr_ta_2018_01/info
|===data_test__path.csv
        /home/tact/AudioDBs/All_DataBase/tadb106/BAC009S0059W0246.wav
        /home/tact/AudioDBs/All_DataBase/tadb128/BAC009S0663W0453.wav
        /home/tact/AudioDBs/All_DataBase/tadb169/BAC009S0745W0291.wav
|===data_train_path.csv
'''
########################################################################
# Timing ------------ ------------------- ------------------- ---------
# Calculate running time 
########################################################################

import timeit
start = timeit.default_timer()  # Start counting time
#--------------- --------------- --------------- ---------------
def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)
#--------------- --------------- --------------- ---------------
 # Stop counting time, make a time string to print out to screen
stop = timeit.default_timer()
total_time=stop-start # in seconds
tRan=format_seconds_to_hhmmss(math.trunc(total_time))
tWait=format_seconds_to_hhmmss(math.trunc(((Max_samples-k)*total_time)/k))

########################################################################




            

