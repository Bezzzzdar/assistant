import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

TRAIN_BATCH_SIZE = 5
VALID_BATCH_SIZE = 2
df_size = 100
tresh_hold = 0.5

command_lines = {'PlayGreetings': ('привет ','здравствуй ','здарово ','здарова ','добрый день ','доброе утро ','добрый вечер '),
                'PlayFarewellAndQuit': ('пока ','покедова ','досвидания ','до скорого ','до встречи ','увидимся '),
                'GoogleSearch': ('найди в гугл ','найди в гугле ','поищи в гугле','что такое', 'как', 'когда', 'зачем', 'почему', 'для чего', 'кто', 'кем чем', ),
                'YouTubeSearch': ('найди видео ', 'покажи видео'),
                'GetWeatherForecast': ('прогноз погоды ', 'какая погода '),
                'PlaySong': ('включи песню ', 'поставь песню', 'поставь', 'трек'),
                'PauseSong': ('стоп ', 'поставь на паузу'),
                'SetVolume': ('установи громкость на ', 'поставь громкость на '),
                'QuieterVolume': ('сделай тише ','сделай потише ', 'сделай ещё тише ','сделай ещё потише ','ещё тише','тише','потише'),
                'LouderVolume': ('сделай громче ','сделай погромче ','сделай ещё громче ','сделай ещё погромче ','ещё громче','громче')}

com_to_targ = {'GoogleSearch': 0,
              'PlayFarewellAndQuit': 1,
              'PlayGreetings': 2,
              'YouTubeSearch': 3,
              'GetWeatherForecast': 4,
              'PlaySong': 5,
              'PauseSong': 6,
              'SetVolume': 7,
              'QuieterVolume': 8,
              'LouderVolume': 9}

all_texts = []
for i in command_lines.values():
    all_texts += [a for a in i]
vect = CountVectorizer(ngram_range=(2, 3), analyzer='char')
vect = vect.fit(all_texts)
    
def make_dataframe(command_lines, df_size, com_to_targ):
  df = {'text':[], 'class':[]}
  for row in range(df_size):
    for clas, text in command_lines.items():
      text = np.random.choice(text)
      if clas == 'GoogleSearch':
        if np.random.uniform(0.0, 1.0) > tresh_hold:
          text = ''
      df['text'].append(text)
      df['class'].append(com_to_targ[clas])
  return df

df = pd.DataFrame(make_dataframe(command_lines , df_size, com_to_targ))
df.text_trans = df.text.map(lambda x: vect.transform([x])[0])
features = df.text.values
features = vect.transform(features).toarray()
target = df['class'].values
X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                    random_state=42)
model = LogisticRegression(solver='newton-cholesky', random_state=42)

model.fit(X_train, y_train)
model.score(X_test, y_test)

filename = 'log_model.pkl'

pickle.dump((vect, model), open(filename, 'wb'))
