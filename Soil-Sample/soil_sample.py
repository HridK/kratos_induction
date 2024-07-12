def highest_concentration(concentration,dim):
    max = 0
    for i in range(dim[1]):
        if concentration[i] > concentration[max]:
            max = i
    if (max+1) == dim[1]:
        max = -1
    else:
        max+=1
    return max


def weights_to_list():
    weight_in_str = input()
    weights_in_list = []
    start,end = -1,0
    for i in range(len(weight_in_str)):
        if weight_in_str[i].isspace():
            end = i
            weights_in_list.append(float(weight_in_str[start+1:end]))
            start = end
    weights_in_list.append(float(weight_in_str[start+1:len(weight_in_str)]))
    return weights_in_list


def input_to_list(dim):
    sample_list = []
    for row in range(dim[0]):
        temp = []
        sample = input()
        for i in sample:
            if i.isdigit():
                temp.append(i)
        sample_list.append(temp)
    return sample_list


# MAIN Function
length = input()
dim = []
for i in length:
    if i.isdigit():
        dim.append(int(i))
# Getting the samples in form of list
samples = input_to_list(dim)

# Getting the weights to list
weights = weights_to_list()

concentration = []
for row in range(dim[0]):
    for col in range(dim[1]):
        concentration.append(float(samples[row][col]) * weights[col])
print(highest_concentration(concentration,dim))

