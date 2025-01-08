var_seqA=[3,None,2,None,1]
var_tot=0
for value in var_seqA:
    if value is None:
        continue
    var_tot+=value
print(var_tot)

print(var_seqA)