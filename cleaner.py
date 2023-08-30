import pandas
 
# reading the CSV file
csvFile = pandas.read_csv('')
csvFile2 = pandas.DataFrame(columns=csvFile.columns)
# displaying the contents of the CSV file
print(csvFile.columns)
csvFile2.columns =csvFile.columns
x=[]
# for note in csvFile['Notes']:
#   x.append(note.split("MOBILE 1 - Value: "))
count=0
print(len(csvFile))
temp=0
global i
i=0
leng=len(csvFile)
while i in range(leng):
  # if(type(str(csvFile['MOBILE'][i]))==type('str')):
  #   print(i,csvFile['Company Name'][i],csvFile['MOBILE'][i],len(str(csvFile['MOBILE'][i])))
  # if len(str(csvFile['MOBILE'][i])) ==12:
  #   if(type(csvFile['MOBILE'][i])=='str'):
  #     csvFile['MOBILE'][i]=csvFile['MOBILE'][i].replace(' ', '')
  if str(csvFile['MOBILE'][i]) !='nan' and str(csvFile['MOBILE'][i]) !='Null':
    csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).strip()
    csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).replace(' ', '')
    
    if len(str(csvFile['MOBILE'][i])) !=12:
      print(i,csvFile['COMPANY NAME'][i],csvFile['MOBILE'][i],len(str(csvFile['MOBILE'][i])))
      count=count+1
      # csvFile['MOBILE'][i]=str(csvFile['PHONE'][i])
      if len(str(csvFile['MOBILE'][i])) ==13:
        csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).replace('91-', '91')
      if len(str(csvFile['MOBILE'][i])) ==11 and str(csvFile['MOBILE'][i][0])=='0':
        csvFile['MOBILE'][i]='91'+str(csvFile['MOBILE'][i][1:])
      # if ',' in str(csvFile['MOBILE'][i]):
      #   numbers=str(csvFile['MOBILE'][i]).split(',')
      #   print(numbers)
      #   for number in numbers:
      #     new=csvFile.loc[i]
        
      #     new['MOBILE']=number
      #     csvFile.append(new,ignore_index=True)
      #   # csvFile = csvFile.drop(csvFile.index[i])
          
      # if '/' in str(csvFile['MOBILE'][i]):
      #   numbers=str(csvFile['MOBILE'][i]).split('/')
      #   print(numbers)
      #   print(i)
      #   for number in numbers:
      #     new=0
      #     new=csvFile.loc[i].copy(deep=True)
      
      #     new['MOBILE']=number
      #     print(new['MOBILE'])
      #     # print(new)
      #     csvFile.loc[len(csvFile.index)]=new
      #     # csvFile.concat(new)
      #     # pandas.concat([csvFile, new])
      #   temp=temp+1
        # print(i)
        # print(csvFile['MOBILE'][i])
        
      # csvFile['MOBILE'][i].replace(' ', '')
      #   csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).replace('-', '')
     
      # if(type(csvFile['MOBILE'][i])=='str'):
      if len(str(csvFile['MOBILE'][i])) ==10:
        csvFile['MOBILE'][i]= '91'+str(int(csvFile['MOBILE'][i]))
        print(csvFile['MOBILE'][i])
      #   if len((csvFile['MOBILE'][i])) ==14:
      #     csvFile['MOBILE'][i]= str(csvFile['MOBILE'][i])
      #     print(csvFile['MOBILE'][i])
  i=i+1
  leng=len(csvFile)
      
        
  # csvFile['MOBILE 1 - Value'][i]=x[i][1].strip()
    # print(csvFile['MOBILE'][i])
  # csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).replace(' ', '')
  # csvFile['MOBILE'][i]=str(csvFile['MOBILE'][i]).replace('-', '')
print(len(csvFile))
print(count)
csvFile.to_csv('cleanData.csv')
# csvFile2.to_csv('Architect_dupes2.csv')