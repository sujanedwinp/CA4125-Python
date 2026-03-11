import matplotlib.pyplot as plt

# sample data
x = [1,2,3,4,5]
y = [10,20,25,30,40]

# Line graph
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# Histogram
data = [10,20,20,30,30,30,40,40,50]
plt.hist(data)
plt.title("Histogram")
plt.show()

# Bar chart
subjects = ["Math", "Science", "English"]
marks = [85, 90, 75]
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()