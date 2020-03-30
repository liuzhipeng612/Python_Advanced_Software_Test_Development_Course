# Author:'haijing'
# date:2018/10/29
# 对象的封装 *****
# 将一个类的对象,封装到,另一个类中的方法中去

class Teacher:
    def __init__(self, tea_name, tea_age):
        self.teacher_name = tea_name
        self.teacher_age = tea_age
        self.salary = 2000  # 老师的初始工资为2k


class Cource:
    def __init__(self, cour_name, cost, teacher):
        self.course_name = cour_name
        self.course_teacher = teacher  # 这一句话是一个类的对象传进另一个类中的关键  *****
        self.course_cost = cost  # cost为课时费 每上一节课总的工资都要增加的

    def class_up(self):
        self.course_teacher.salary += self.course_cost  # course_teacher = T1,因为在下面创建Course类的对象时:C1 = Cource('生理课',30,T1),参数传递进来的


T1 = Teacher('李杰', 24)  # 创建类Teacher的对象 T1
T2 = Teacher('张昭', 25)
T3 = Teacher('子龙', 22)

C1 = Cource('生理课', 30, T1)  # T1以一个对象的形式作为类Cource的参数 此时T1就等于Course类中的teacher  *****
print(C1.course_name)  #
print(C1.course_teacher.teacher_name)  # C1.course_teacher = T1; C1.course_teacher.teacher_name = T1.teacher_name
print(C1.course_teacher.teacher_age)  # C1.course_teacher.teacher_age = T1.teacher_age

print(C1.course_teacher.salary)  # 上课前的工资
C1.class_up()  # 上课
print(C1.course_teacher.salary)  # 上课后的工资
