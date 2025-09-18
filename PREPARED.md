# Resumo da base preparada

Formato linhas **5746156** colunas **20**

## Nome das colunas

```bash
Index(['pdv', 'produto', 'date_week', 'date_month', 'gross_value_median',
       'net_value_median', 'gross_profit_median', 'discount_median',
       'taxes_median', 'quantity_sum', 'premise', 'categoria_pdv',
       'zipcode_national', 'zipcode_sectional', 'categoria_produto',
       'tipos_produto', 'label_produto', 'subcategoria_produto',
       'marca_produto', 'fabricante_produto'],
      dtype='object')
```

## Primeiros registros

```bash
                   pdv              produto  date_week  date_month  gross_value_median  ...  tipos_produto  label_produto  subcategoria_produto                 marca_produto     fabricante_produto
0  1000237487041964405  1837429607327399565          1           2           35.200001  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
1  1000237487041964405  1837429607327399565          2           7           76.800003  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
2  1000237487041964405  1837429607327399565          3           2           70.400002  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
3  1000237487041964405  1837429607327399565          3          11           76.800003  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
4  1000237487041964405  1837429607327399565          4           5           38.400002  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co

[5 rows x 20 columns]
```

## Exploração dos campos categóricos

**Campo**: pdv

```bash
pdv
2430132255826117411    6209
8078953974483084504    5897
7542707299572856789    5848
8723723113467008071    5716
1057223373529991552    5641
                       ... 
3976346274696722805       1
9202744846321504259       1
2813132825821821710       1
2526440652638833567       1
4692279971736225777       1
Name: count, Length: 14379, dtype: int64
```

**Campo**: produto

```bash
produto
4623814317972718932    95461
8174625658473329985    91986
3262679882836704514    88907
1029370090212151375    86073
8625590539951587748    80299
                       ...  
1870347266672774934        1
1785489276686692971        1
7585079007059117701        1
5861285639684913640        1
2403829120693223544        1
Name: count, Length: 6997, dtype: int64
```

**Campo**: date_week

```bash
date_week
2    1679570
3    1388118
1    1342292
4    1336176
Name: count, dtype: int64
```

**Campo**: date_month

```bash
date_month
9     754856
6     511672
5     491855
12    489483
8     483435
10    482197
11    472141
7     463751
4     441494
3     426761
2     390208
1     338303
Name: count, dtype: int64
```

**Campo**: premise

```bash
premise
Off Premise    5120648
On Premise      625508
Name: count, dtype: int64
```

**Campo**: categoria_pdv

```bash
categoria_pdv
Convenience                  1937553
Package/Liquor               1840109
Grocery                      1024322
Super Center                  282895
Restaurant                    237845
Bar                           173067
Mexican Rest                   39527
Hotel/Motel                    19044
Golf - Public                  17877
Drug                           17755
Service Org                    15756
Pizza                          13551
Billiard/Bowling               12868
Golf - Private                 12463
Sports/Rec Club                10178
Italian                         8897
Irish                           8316
Asian                           7339
Other On Premise                6868
Stadium/Concession              5919
Bodega                          4920
Barbeque                        4566
Church                          4380
Club Store                      4278
Military                        4245
Sample Room                     3088
Other Off Premise               2992
Night Club                      2762
Airline/Airport                 2666
Music Venue                     2584
Theatre                         2496
Special Event                   2424
Adult Entertainment             2366
Gay Bar                         1903
Banquet/Caterer                 1627
Coffee House                    1037
Neighborhood Store               793
All Other N/A On Premise         774
Theme Park                       726
All Other N/A Off Premise        634
Korean                           567
Country/Western                  453
Winery                           434
French                           300
Health Club                      225
Race Track                       207
Gym/Fitness                      159
Sub Distributor                  134
Marina / Lake                    109
Salon/Spa/Tann                   108
German                            16
Casino                            16
Non-Traditional                   16
Mass Merch                         2
Name: count, dtype: int64
```

**Campo**: zipcode_national

```bash
zipcode_national
8    3280847
3    2464755
9        554
Name: count, dtype: int64
```

**Campo**: zipcode_sectional

```bash
zipcode_sectional
300    943267
802    704546
301    635905
800    511171
307    462850
809    383358
801    374088
805    343559
303    233484
810    210669
806    174124
804    165031
305    156043
808     94208
811     68853
813     67308
812     58290
807     52000
803     37178
816     16636
302     12485
815     11743
814      8085
306      4052
312      3301
314      2888
310      2246
319      1867
317      1572
315      1538
313      1214
316       956
309       425
304       418
901       379
909       175
308       165
318        78
398         1
Name: count, dtype: int64
```

**Campo**: categoria_produto

```bash
categoria_produto
Package              4049424
Non-Alcohol           801725
Distilled Spirits     569450
Draft                 167744
Wine                  110370
ABA Spirits            47020
Tobacco                  423
Name: count, dtype: int64
```

**Campo**: tipos_produto

```bash
tipos_produto
Package                      3984930
Non Alcohol                   760887
Distilled Spirits             397765
Draft                         167426
Wine < 14 %                    91344
N/A Beer                       90342
Allocated Spirits              85114
Distilled Spirits-RTD          77701
Wine > 14 %                    34388
Hispanic                       22925
Wine RTD                       12944
Non Alcohol W&S                10606
Distilled Spirits-Domest        3301
Cider Pkg                       2050
Wine < 14 % - Domestic          1458
Talking Rain                    1230
Dairy                            606
Dist Spirits-RTD Domestic        530
Tobacco                          423
MB Wine < 14 %                   102
Cider Dft                         83
Pkg 3.2                            1
Name: count, dtype: int64
```

**Campo**: label_produto

```bash
label_produto
Core               4577400
Discontinued        550281
Allocated            54638
In&Out               45870
Winter Seasonal       9882
Close Out             4827
Fall Seasonal         4791
Specialty             4377
Private Label         2269
Summer Seasonal        635
Spring Seasonal        342
Speciality             223
Clearing               139
Other                    1
Name: count, dtype: int64
```

**Campo**: subcategoria_produto

```bash
subcategoria_produto
Lager                  3043085
Other Package           378153
Water                   235785
Energy                  211702
IPA                     201750
Juice & Tea             169007
Liqueurs & Cordials     157085
Ale                     112044
Specialty               111538
Lager / Pilsner         108715
Other Non-Alcoholic     104788
Ready-to-Drink           93947
Wheat Beer               85768
Non-Alcoholic            79219
Bourbon Whiskey          69514
Vodka                    68331
Canadian Whisky          53761
Tequila / Mezcal         43099
White Wine               41215
Dairy beverage           38454
Other Spirits            38104
Soda                     32124
Red Wine                 31727
Pale Ale                 26991
Stout & Porter           25920
Rum                      25870
Other ABA Spirits        24892
Sour                     23195
Brandy / Cognac          21384
Other Wine               20521
Gin                      11178
Mixers                    9648
Other Draft               7968
Rosé Wine                 7180
Scotch Whisky             6431
Sparkling Wine            4955
Dessert Wine              4772
Irish Whiskey             2874
Sour / Wild Ale           2628
Hard Cider                 925
Specialty Beer             586
Gose                       284
Name: count, dtype: int64
```

**Campo**: marca_produto

```bash
marca_produto
Bud Light                                        754650
Michelob Ultra                                   530839
Budweiser                                        483521
Natural Light                                    151044
Bud Ice                                          131529
                                                  ...  
Clementine De Pape Clement Pessac-Leognan Red         1
Beacon BOM Baltic Porter                              1
Iron Hill Pig Iron Porter                             1
Chloe Prosecco                                        1
Teavana Peach Green                                   1
Name: count, Length: 4169, dtype: int64
```

**Campo**: fabricante_produto

```bash
fabricante_produto
AB Anheuser Busch Inc    3802362
Sazerac Spirits           451850
Tilray Brands             294749
Talking Rain              155136
Yuengling                 116109
                          ...   
AB Patagonia Brewing           1
Epic Ventures                  1
AB Virtue Cider                1
VPX                            1
The Wine Trust                 1
Name: count, Length: 343, dtype: int64
```

