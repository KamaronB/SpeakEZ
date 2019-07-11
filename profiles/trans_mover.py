import os


def translate(messages):
    #change to the correct directory
    try:
        os.chdir("/home/shaveandahaircut/OpenNMT-py/")
        print('successful')
    except:
        pass

    try:
        message_sheet=open("message_sheet.txt",'x')
        print('creating file')

    except:
        message_sheet=open("message_sheet.txt","r+")
        print('opening file that is already made')
    #write messages to file

    for msg in messages:
        if msg!='':
         try:
           message_sheet.write(msg)
           message_sheet.write('\n')
           print( msg)
         except:
           print('didnt work' )

    #os call
    os.system('python translate.py -model en-es_model_step_5000.pt -src message_sheet.txt -output pred.txt -replace_unk -verbose')



    #open the prediction file


    p=open("pred.txt")

    p=p.read()


    ###split by newline and create empty array
    preds=p.split('\n')

    predictions=[]

    ###add the predictions to new array
    for line in preds:
        predictions.append(line)
    os.chdir("/home/shaveandahaircut/django_project/SpeakEasy")
    return predictions





# words=['hello','whats up']
# print(translate(words))
