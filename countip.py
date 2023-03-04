import csv

filename = "client_ip.csv"


ip_counts = {}


with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 
    for row in csvreader:
        ip_address = row[0]
        
        if ip_address in ip_counts:
            ip_counts[ip_address] += 1
        
        else:
            ip_counts[ip_address] = 1

# print out the results
for ip, count in ip_counts.items():
    print(f"{ip}: {count}")
