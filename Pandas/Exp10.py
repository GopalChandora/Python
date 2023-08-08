import Pandas as p


data = p.DataFrame({'Name':p.Series(['Gopal', 'Ayush']),' Roll_no': p.Series([31, 9]), 'Division':p.Series(['B', 'B'])})

data1 = p.DataFrame({'Name':p.Series(['Arvind', 'Yash']), 'Roll_no':p.Series([19, 10]), 'Division':p.Series(['B', 'B'])})


print('A.Students Details')

print(data)

print(data1)


print('\n B.Merging Students Details')

print(p.merge(data, data1, on='Division'))


print('\n C.Deleted Students Details from data')

del data['Division']

print(data)
