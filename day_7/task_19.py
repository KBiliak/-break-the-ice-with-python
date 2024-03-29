"""You are required to write a program to sort the (name, age, score) tuples by
 ascending order where name is string, age and score are numbers. The tuples
 are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]"""

names = input("Enter names separated by comma: ").split(',')
ages = input("Enter ages separated by comma: ").split(',')
scores = input("Enter scores separated by comma: ").split(',')

data = []


def sort_data(names, ages, scores):
    for name, age, score in zip(names, ages, scores):
        data.append((name.strip(), age.strip(), score.strip()))

    return data


result = sort_data(names, ages, scores)
print(result)



