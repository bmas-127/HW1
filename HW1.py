import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107060015.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    C0A880 = []
    C0F9A0 = []
    C0G640 = []
    C0R190 = []
    C0X260 = []

    for row in mycsv:
        if(row['station_id'] == 'C0A880') :
            C0A880.append(row['TEMP'])
        elif(row['station_id'] == 'C0F9A0') :
            C0F9A0.append(row['TEMP'])
        elif(row['station_id'] == 'C0G640') :
            C0G640.append(row['TEMP'])
        elif(row['station_id'] == 'C0R190') :
            C0R190.append(row['TEMP'])
        elif(row['station_id'] == 'C0X260') :
            C0X260.append(row['TEMP'])
            
        #print(dick)
        #data.append(dick)
        #print(data)
        #print()
        #print()
        

C0A880.sort(reverse=True)
C0F9A0.sort(reverse=True)
C0G640.sort(reverse=True)
C0R190.sort(reverse=True)
C0X260.sort(reverse=True)


if ((float(C0A880[0]) != -99) & (float(C0A880[0]) != -999)) :
    a = ['C0A880', C0A880[0]]
else :
    a = ['C0A880', 'None']
    
if ((float(C0F9A0[0]) != -99) & (float(C0F9A0[0]) != -999)) :
    b = ['C0F9A0', C0F9A0[0]]
else :
    b = ['C0F9A0', 'None']
    
if ((float(C0G640[0]) != -99) & (float(C0G640[0]) != -999)) :
    c = ['C0G640', C0G640[0]]
else :
    c = ['C0G640', 'None']

if ((float(C0R190[0]) != -99) & (float(C0R190[0]) != -999)) :
    d = ['C0R190', C0R190[0]]
else :
    d = ['C0R190', 'None']
    
if ((float(C0X260[0]) != -99) & (float(C0X260[0]) != -999)) :
    e = ['C0X260', C0X260[0]]
else :
    e = ['C0X260', 'None']
    
c = [a, b, c, d, e] 

print(c)
