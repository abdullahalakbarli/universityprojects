import matplotlib.pyplot as plt

categories = [
    "Struggle to Track Calorie Intake (Example Study A)",
    "Motivated by Health/Fitness Apps (Example Study B)",
    "Meet Fruit/Vegetable Recommendations (CDC Report)",
    "Find Meal Planning Difficult (Survey by XYZ Organization)",
    "Underestimate Calorie Consumption (Nutrition Journal Study)"
]
percentages = [70, 64, 14, 75, 47]
fig, ax = plt.subplots()
bars = ax.barh(categories, percentages, color=['#A1FA4F', '#75F94D', '#5ABF6C', '#377D22', '#377E47'])
for bar in bars:
    width = bar.get_width()
    label_x_pos = width - 5 if width > 5 else width + 5
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', ha='right' if width > 5 else 'left', color='white' if width > 5 else 'black')
ax.set_xlabel('Percentage')
ax.set_title('Data About Calorie Tracking')
plt.show()
