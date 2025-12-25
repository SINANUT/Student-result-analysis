students = [
    {"name" : "sinan" , "marks" : {
        "english" : 95,
        "maths" : 85,
        "science" : 90,
    }},
    {"name" : "regdhan" , "marks" : {
        "english" : 65,
        "maths" : 76,
        "science" : 85,
    }},
    {"name" : "vyshak" , "marks" : {
        "english" : 45,
        "maths" : 96,
        "science" : 100,
    }},
    {"name" : "almas" , "marks" : {
        "english" : 75,
        "maths" : 45,
        "science" : 35,
    }},
    {"name" : "abin" , "marks" : {
        "english" : 65,
        "maths" : 49,
        "science" : 85,
    }},
    {"name" : "salam" , "marks" : {
        "english" : 99,
        "maths" : 96,
        "science" : 90,
    }},
    {"name" : "shahas" , "marks" : {
        "english" :35 ,
        "maths" : 49,
        "science" : 48,
    }},
    {"name" : "shamil" , "marks" : {
        "english" : 100,
        "maths" : 55,
        "science" : 85,
    }},
    {"name" : "ut" , "marks" : {
        "english" : 15,
        "maths" : 45,
        "science" : 25,
    }},
    {"name" : "nehala" , "marks" : {
        "english" : 83,
        "maths" : 85,
        "science" : 100,
    }}
]


def total(mark):
    tot = 0
    for x in mark.values():              
        tot += x
    return tot

def average(a):
    return a/3

def pass_fail(avg):
    if avg >= 50:
        return "pass"
    else:
        return "fail"
    
def grades(gra):
    if avg >= 90:
        return "A Grade"
    elif avg >= 80:
        return "B Grade"
    elif avg >= 70:
        return "C Grade"
    elif avg >= 60:
        return "D Grade"
    else:
        return "No Grades,Better Luck Next time"

for student in students:
    t = total(student["marks"])
    avg = average(t)
    result = pass_fail(avg)
    grade = grades(avg)

    print(student["name"],"Total",t,"Average",int(avg),result,"Grade:",grade)



    
    


    