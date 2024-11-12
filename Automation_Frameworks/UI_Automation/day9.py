import csv

def wite_inside_csv(row,filename='sample.csv'):
    with open(filename,'w') as f:
        writter=csv.writer(f)
        writter.writerow(row)

wite_inside_csv(['Name','City','Age'])
wite_inside_csv(['A1','Pune1','23'])
wite_inside_csv(['A2','Pune2','25'])
wite_inside_csv(['A4','Mumbai1','25'])
wite_inside_csv(['A5','Mubai3','25'])
wite_inside_csv(['A21','Pune11','23'])
wite_inside_csv(['A22','Pune22','25'])







# filed=['name','city']
# rows=[['a','pune'],['aa','mumbai'],['zz','chennai']]
# r3=['dd','pune']
# filename='sample.csv'
# with open(filename,'w') as file:
#     writterobject=csv.writer(file)
#     writterobject.writerow(filed)   #write the single row
#     writterobject.writerows(rows)   #write mulple row
#     writterobject.writerow(r3)

with open('sample.csv') as f:
    l1=csv.reader(f)
    for r in l1:
        print(r)

