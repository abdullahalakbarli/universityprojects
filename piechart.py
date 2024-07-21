import matplotlib.pyplot as plt

labels = ['Struggle to Track Calories', 'Accurately Track Calories']
sizes = [70, 30]
colors = ['#ED1C24','#75FA8D']
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.axis('equal')  
plt.title('Percentage of People Struggling to Track Daily Calorie Intake Accurately')
plt.show()
