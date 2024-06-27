student_dict = {
    "student": ['Ange', 'James', 'Liy'],
    "score": [56, 76, 98]
}


import pandas as pd

student_dict_frame = pd.DataFrame(student_dict)

print(student_dict_frame)

