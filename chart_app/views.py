import csv

from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
import matplotlib.pyplot as plt

from .forms import UploadfilesForm
import pandas as pd
import plotly.graph_objects as go

# Create your views here.
def timeframe(args):
    #читаем файл и преобразуем во вложенный список
    with open(args) as f:
        reader = list(csv.reader(f))
        reader_new = []
        for c, i in enumerate(reader):
            if c == 0:
                reader_new.append(['time', 'open', 'high', 'low', 'close'])
            else:
                reader_new.append([i[0], float(i[1]), float(i[1]), float(i[1]), float(i[1])])
        return reader_new

def conver_to_df(args, timeframe):
    #по первому вложенному списку формируем название колонок
    df = pd.DataFrame(args[1:], columns=['time', 'open', 'high', 'low', 'close'])
    # время преобразуем во временной формат и делаем его индексом
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time')
    # по выбранному timeframe формируем ДФ
    df = df.resample(timeframe).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
    })
    return df

class UploadfilesView(CreateView):
    form_class = UploadfilesForm
    template_name = 'chart_app/index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = UploadfilesForm(request.POST, request.FILES)
        if form.is_valid():
            saved_object  = form.save()
            files = saved_object.file.name
            if files[-4:] == '.csv':
                #добавляем колонки для OHLC
                mindf = timeframe(f'media/{files}')
                # определяем ТФ и ЕМА
                tf = saved_object.timeframe
                ema = saved_object.ex_mov_average
                # #преобразуем словарь в ДФ
                df = conver_to_df(mindf, tf)
                if ema != None:
                    df['EMA'] = df.close.ewm(span=ema, adjust=False).mean()
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                         open=df['open'],
                                                         high=df['high'],
                                                         low=df['low'],
                                                         close=df['close']),
                                          go.Scatter(x=df.index, y=df.EMA, line=dict(color='orange', width=1))
                                          ])
                else:
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                         open=df['open'],
                                                         high=df['high'],
                                                         low=df['low'],
                                                         close=df['close']),
                                          ])
                #строим график
                fig.show()
                return redirect('index')
        return redirect('index')