# import libraries
import seaborn as _ss
import matplotlib.pyplot as _mpp

# data set 
mydata = _ss.load_dataset('titanic')
# figure size
_mpp.figure(figsize=(18,8))
_ss.boxplot(
    x = 'survived',
    y = 'age',
    hue = 'who',
    data = mydata,
    showmeans = True
)
# label - titles
_mpp.xlabel('How many people survived in the titanic')
_mpp.ylabel('Age (Years)' ,size=10)
# show graph
_mpp.show()