
# format格式化字符串

course = "python"
school = "zhiliao"
# text = "i love {}, i study in {}".format(course,school)
text = "i love {my_course}, i study in {my_school}".format(my_school=school,my_course=course)
print(text)