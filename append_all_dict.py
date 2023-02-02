# ips_data = {
# "1.2.3.4": {
#     "data_one": 1,
#     "data_two": 8,
#     "list_one": [],
#     "list_two": [
#         "item_one"
#     ],
#     "data_three": "string1"
# },
# "5.6.7.8": {
#     "data_one": 1,
#     "data_two": 9,
#     "list_two": [
#         "item_one"
#     ],
#     "data_three": "string1",
#     "data_four": "string2",
#     "data_five": "string3"
# }
# }
# ips_data.keys()
# # ['1.2.3.4', '5.6.7.8']
# ips = ips_data.keys()

# sorted_ips = sorted(ips, key=lambda ip: ips_data[ip]['data_two'], reverse=True)
# print(sorted_ips)
# # ['5.6.7.8', '1.2.3.4']







spisok_urls = []
    
for num_link in range(1,50): # [4:6] только с 4 по 6
    url = f'{num_link}'
    spisok_urls.append(url)
    print (url)

# spisok_urls = zip(spisok_urls)
print (spisok_urls)