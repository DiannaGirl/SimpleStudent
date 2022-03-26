import random;

from Student import Student

s = "Minh";
student = Student(s);
student.setName(s);
student.setAge(14);


student.setRank("GOOD");

print(student.rank);
print(student.name);
print(student.age);

