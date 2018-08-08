import education
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

list_of_state_record = education.get_all_states()
a_state_record = education.get_state("illinois")
b_state_record = education.get_state("arkansas")

def info(state_record):
    print("\nBiracial: ", state_record['data']['enrollment']['students']['race']['biracial'])
    print("Hispanic: ", state_record['data']['enrollment']['students']['race']['hispanic'])
    print("Black: ", state_record['data']['enrollment']['students']['race']['black'])
    print("Asian: ", state_record['data']['enrollment']['students']['race']['asian'])
    print("White: ", state_record['data']['enrollment']['students']['race']['white'])
    print("Native American: ", state_record['data']['enrollment']['students']['race']['native american'], "\n")

def performance(state_record):
    return [state_record['data']['enrollment']['students']['race']['biracial'],
        state_record['data']['enrollment']['students']['race']['hispanic'],
        state_record['data']['enrollment']['students']['race']['black'],
        state_record['data']['enrollment']['students']['race']['asian'],
        state_record['data']['enrollment']['students']['race']['white'],
        state_record['data']['enrollment']['students']['race']['native american']]

info(a_state_record)
info(b_state_record)

#means_il = [1,2,3,4,5,6]
#means_ar = [1,2,3,4,5,6]

means_il = performance(a_state_record)
means_ar = performance(b_state_record)

objects = ('Biracial', 'Hispanic', 'Black', 'Asian', 'White', 'Native American')
y_pos = np.arange(len(objects))

fig, ax = plt.subplots()
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(y_pos, means_il, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Illinois')
rects2 = plt.bar(y_pos + bar_width, means_ar, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Arkansas')
plt.xticks(y_pos, objects)
plt.ylabel('Students Enrolled')
plt.xlabel('Races')
plt.title('Students enrolled in school by race')
plt.legend()
plt.tight_layout()
plt.show()


#https://pythonspot.com/matplotlib-bar-chart/
