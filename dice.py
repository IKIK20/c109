import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go


dice_result=[]

for i in range(0,1000):
    d1= random.randint(1,6)
    d2= random.randint(1,6)
    dice_result.append(d1+d2)

mean= st.mean(dice_result)
median= st.median(dice_result)
mode= st.mode(dice_result)
std= st.stdev(dice_result)


first_stdev_start, first_stdev_end = mean-std, mean+std
second_stdev_start, second_stdev_end = mean-(2*std), mean+(2*std)
third_stdev_start, third_stdev_end = mean-(3*std), mean+(3*std)


fig= ff.create_distplot([dice_result],["DICE RESULT"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name="stdev1 start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name="stdev1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name="stdev2 start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name="stdev2 end"))

fig.show()

data_1stdev = [result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
data_2stdev = [result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
data_3stdev = [result for result in dice_result if result > third_stdev_start and result < third_stdev_end]

print(len(data_1stdev)*100/len(dice_result))
print(len(data_2stdev)*100/len(dice_result))
print(len(data_3stdev)*100/len(dice_result))





