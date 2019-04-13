import csv
import hashlib

info_file = open('UserInfo.csv', 'r')
csv_reader = csv.reader(info_file)

hash_info = open("Infohash.csv", 'a')
csv_writer = csv.writer(hash_info)

for line in csv_reader: 
    password = line[2]
    hash256 = hashlib.sha256()
    password = password.encode('utf-8')
    hash256.update(password)
    password_hash = hash256.hexdigest()
    line[2] = password_hash

    CC = line[8]
    hash256 = hashlib.sha256()
    CC = CC.encode('utf-8')
    hash256.update(CC)
    CC_hash = hash256.hexdigest()
    line[8] = CC_hash
    print(line)

    csv_writer.writerow(line)

info_file.close()
hash_info.close()








"""
       hash_object = hashlib.sha256(b"password")
       hex_dig = hash_object.hexdigest()
       print(hex_dig)
"""


       
    

