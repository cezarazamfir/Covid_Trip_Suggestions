import csv 

def correct_region(region):
    switch = 1
    if region == 1 or region == 2 or region == 3 or region ==4 or region == 5: switch=0
    return switch



print('Find a safe destiation for your trip during the pandemic./n')

maximum_cases = int(input('What is the maximum number of cases you would accept for your destiation?\n '))

region = int(input('Where would you like your trip to be?(select a number)\n 1. Europe\n 2.Africa\n 3.Americas\n 4.Western Pacific\n 5.Eastern Mediterranean\n'))
while correct_region(region):
    region = int(input("Please type a valid region (numbers 1-5):\n"))

if region == 1:
    region = 'Europe'
elif region == 2:
    region = 'Africa'
elif region == 3:
    region = 'Americas'
elif region == 4:
    region = 'Western Pacific'
else:
    region = 'Eastern Mediterranean'


with open('dataset.csv') as dataset:
    dataset_dict = csv.DictReader(dataset)

    header_written = False
    for row in dataset_dict:
        if int(row['Active'])<=maximum_cases and row['WHO Region'] == region:
            
            with open('trip_suggestions.csv','a', newline='') as trip_suggestions:
                fields = ['Country', 'Active Cases']
                writer = csv.DictWriter(trip_suggestions, fieldnames = fields)
                if header_written == False:
                    writer.writeheader()
                    header_written = True
                writer.writerow({'Country': row['Country/Region'], 'Active Cases': row['Active']})
                
        
            
            

            
        
            print(row['Country/Region'])