#coding:utf-8

import faker

fake = faker.Faker(locale='zh_CN')

target = open("mac.csv",'a')

'''
for i in range(10000):
    data = fake.name() + ',' + fake.ssn() \
           + ',' + fake.phone_number() + ',' + fake.job()\
           + ',' + fake.email() + ',' + fake.credit_card_number(card_type=None) \
           + ',' + fake.company()
    target.writelines(str(data) + '\n')
target.close()
'''
for i in range(5000):
    data = fake.name() + ',' + fake.mac_address()
    target.writelines(str(data) + '\n')
target.close()