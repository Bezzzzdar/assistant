import sklearn
import pickle
import torch

class Model():
    def __init__(self):
        self.tokenizer, self.model = pickle.load(open('log_model.pkl', 'rb'))
        
        self.commands = {0: GoogleSearch(),
           1: PlayFarewellAndQuit(),
           2: PlayGreetings(),
           3: YouTubeSearch(),
           4: GetWeatherForecast(),
           5: PlaySong(),
           6: PauseSong(),
           7: SetVolume(),
           8: QuieterVolume(),
           9: LouderVolume()}
        
        self.dummy_com = {0: 'GoogleSearch',
           1: 'PlayFarewellAndQuit',
           2: 'PlayGreetings',
           3: 'YouTubeSearch',
           4: 'GetWeatherForecast',
           5: 'PlaySong',
           6: 'PauseSong',
           7: 'SetVolume',
           8: 'QuieterVolume',
           9: 'LouderVolume'}
        
    def forward(self, input):
        x = self.tokenizer.transform([input]).toarray()
        x = self.model.predict(x)[0]
        print(self.dummy_col[x])
        return self.commnads[x](input)
