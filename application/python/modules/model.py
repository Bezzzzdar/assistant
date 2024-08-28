import sklearn
import pickle
import torch
from assistant import *


class Model():
    def __init__(self, test):
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
        
        self.test = test
        
    def forward(self, input):
        x = self.tokenizer.transform([input]).toarray()
        x = self.model.predict(x)[0]
        print(self.dummy_com[x])
        if self.test:
            return
        return self.commnads[x](input)
