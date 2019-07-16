import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""script by Kamaron Bickham to calculate the different percentages of the different languages spoken in various states across
the United States"""
###get the data
state=input('enter your State code \n')
file="languages_spoken_"+state.upper()+".csv"
data = pd.read_csv(file)



##print head of data
print(data.head())

countries=data.index[1:]
print(countries)


#save the total Population
pop=data['Number of speakers']['Population 5 years and over']

#replace commas
pop =pop.replace(",",'')

#save as a float
pop2=int(pop)

print(pop2)



# calculate percentage of total speakers
df = data['Number of speakers'][1:]

#initialize empty array
lang_num=[]

#replace commas and turn to numpy array float
for num in df:
    if num!="--":
        try:
            lang_num.append(num.replace(',',''))
        except:
            lang_num.append(num)

lang_num=np.array(lang_num,dtype='float')

print(lang_num)


#calculate percentage

lang_percent=[x/pop2*100 for x in lang_num]
print(lang_percent)
x_num=[i for i,_ in enumerate(countries)]

############BAR CHART##################################################
plt.figure(figsize=(20,10))
plt.bar(x_num,lang_percent,label="Languages Spoken By Percentage",align='edge', width=0.9)
plt.legend()
plt.title('Languages Spoken at home By Percentage In '+state.upper()+ ' From 2006-2008. Data from the US Census bureau')
plt.xticks(x_num,countries)
plt.tick_params(axis='x', which='major', labelsize=3)
plt.xlabel('Languages Spoken')
plt.ylabel('Percentage spoken')
plt.show()



######PIE CHART#######################################################

#explode means split apart
explode = [0.1 for x in countries]
fig1, ax = plt.subplots()
ax.pie(lang_percent, explode=explode, labels=countries, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.set_title('Languages Spoken at home By Percentage In '+state.upper()+ ' From 2006-2008. Data from the US Census bureau')

ax.axis('equal')
plt.show()
