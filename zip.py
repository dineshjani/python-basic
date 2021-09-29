country  = [ 'India', 'Italy', 'Japan' ] 
capital = [ 'Delhi' , 'Rome', 'Tokyo' ] 
output_dict = {}
# Using loop for constructing dictionary
for (key, value) in zip(country  , capital):
    output_dict[key] = value
print("Output Dictionary using for loop:", output_dict)