import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("data.csv")
heightlist=df["Height(Inches)"].to_list()

mean= st.mean(heightlist)
median= st.median(heightlist)
mode= st.mode(heightlist)
std= st.stdev(heightlist)

first_stdev_start, first_stdev_end = mean-std, mean+std
second_stdev_start, second_stdev_end = mean-(2*std), mean+(2*std)
third_stdev_start, third_stdev_end = mean-(3*std), mean+(3*std)

#print(mean,median,mode,std)

data_1stdev = [result for result in heightlist if result > first_stdev_start and result < first_stdev_end]
data_2stdev = [result for result in heightlist if result > second_stdev_start and result < second_stdev_end]
data_3stdev = [result for result in heightlist if result > third_stdev_start and result < third_stdev_end]

""" print(len(data_1stdev)*100/len(heightlist))
print(len(data_2stdev)*100/len(heightlist))
print(len(data_3stdev)*100/len(heightlist))
 """

fig= ff.create_distplot([heightlist],["HEIGHT"], show_hist= False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.21], mode = "lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.21], mode = "lines", name="stdev1 start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.21], mode = "lines", name="stdev1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.21], mode = "lines", name="stdev2 start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.21], mode = "lines", name="stdev2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.21], mode = "lines", name="stdev3 start"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.21], mode = "lines", name="stdev3 end"))


fig.show()


fig.show()
