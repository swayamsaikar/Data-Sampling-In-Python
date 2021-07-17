import pandas
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random


# !! IN THIS PROGRAM WE HAVE TAKEN 30 RANDOM SAMPLES FROM THE CLAPDATA AND FIND THEIR MEAN AND RETURN IT
# !! WE ALSO HAVE WRITTEN STANDARD_DEVIATION FUNCTION REPEAT THE ABOVE LINE 100 TIMES SO TYHAT IT WILL GET 100 DIFFERENT MEANS AND STORE IT IN THE MEAN_LIST VARIABLE
# !! AND WE ARE ONLY PLOTING GRAPH

# reading the csv data
data = pandas.read_csv("medium_data.csv")

# extracting the claps column and converting it to a list
clapData = data["claps"].tolist()

print(f"Mean of the clapData is -> {statistics.mean(clapData)}")
print(f"Standard Deviation of the clapData is -> {statistics.stdev(clapData)}")


def random_mean_generator(counter):
    dataset = []

    # The code inside will run for 30 times
    for i in range(0, counter):
        # here i have to find a random number between 0 to total length of clapData
        random_index = random.randint(0, len(clapData)-1)

        # here i have to find the value on that particular random index and append it in the dataset list
        random_index_value = clapData[random_index]

        # appending the index value
        dataset.append(random_index_value)

    mean = statistics.mean(dataset)
    return mean


def standard_Deviation():
    mean_list = []
    # The code inside this loop will run for 100 times
    for i in range(0, 100):
        # so this piece of code will find 30 random indexs between 0 and length of clapData-1 and its values and find the mean of them and return it
        set_of_means = random_mean_generator(30)

        # and we will append each mean to mean_list array
        mean_list.append(set_of_means)
    print(f"Length of the mean_list is -> {len(mean_list)}")  # length -> 100
    print(
        f"Standard Deviation of the sample distribution -> {statistics.stdev(mean_list)}")
    print(
        f"Mean of the distribution is -> {statistics.mean(mean_list)}")

    # and then we will plot a graph on the list of mean
    plotgraph(mean_list)


def plotgraph(meanList):
    # here we are find the
    df = meanList
    mean = statistics.mean(meanList)
    # we will create a distplot with the list of means
    figure = ff.create_distplot([df], ["clapData"], show_hist=True)

    # we have to draw a line to indicate the location of the mean (the mean will always be in a random position whenever you will run this program because we are take random 30 samples in the random_mean_generator() function)
    figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines"))

    # and here we have to show the figure
    figure.show()


standard_Deviation()
