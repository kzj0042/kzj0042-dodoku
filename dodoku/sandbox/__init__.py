grid=[0,1,2,3,4]
hash=1234
result = {'op':'create&level=2'}
results = result['op']
split = results.split('=')
print(split[1])   
