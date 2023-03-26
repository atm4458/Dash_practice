import pickle
import pandas as pd
import constant as COL
import numpy as np

lot_id = ["abcdef"]
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]
df = {COL.X: x, COL.Y:y}

df = pd.DataFrame(df)
print(df)
lot_id = pd.Series(lot_id[0], index=df.index, name=COL.LOTID)
chainA = pd.Series(np.random.random(len(df.index)), index=df.index, name="CHAINA")
dieid = lot_id+"_"+df[COL.X].astype(str)+"_"+df[COL.Y].astype(str)
dieid.name = COL.DIEID

data = pd.concat([lot_id, dieid, df, chainA], axis=1)
print(data)

with open("test.pickle", "wb") as f:
    pickle.dump(data, f)