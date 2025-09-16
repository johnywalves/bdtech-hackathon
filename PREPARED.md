# Resumo da base preparada

Formato linhas **5747503** colunas **45**

## Nome das colunas

```bash
Index(['pdv', 'produto', 'distributor_id', 'date_week', 'date_month',
       'gross_value_mean', 'gross_value_median', 'gross_value_min',
       'gross_value_max', 'gross_value_std', 'net_value_mean',
       'net_value_median', 'net_value_min', 'net_value_max', 'net_value_std',
       'gross_profit_mean', 'gross_profit_median', 'gross_profit_min',
       'gross_profit_max', 'gross_profit_std', 'discount_mean',
       'discount_median', 'discount_min', 'discount_max', 'discount_std',
       'taxes_mean', 'taxes_median', 'taxes_min', 'taxes_max', 'taxes_std',
       'quantity_mean', 'quantity_median', 'quantity_min', 'quantity_max',
       'quantity_sum', 'premise', 'categoria_pdv', 'zipcode_national',
       'zipcode_sectional', 'categoria_produto', 'tipos_produto',
       'label_produto', 'subcategoria_produto', 'marca_produto',
       'fabricante_produto'],
      dtype='object')
```

## Primeiros registros

```bash
                   pdv              produto distributor_id  date_week  date_month  ...  tipos_produto  label_produto  subcategoria_produto                 marca_produto     fabricante_produto
0  1000237487041964405  1837429607327399565              4          1           2  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
1  1000237487041964405  1837429607327399565              4          2           7  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
2  1000237487041964405  1837429607327399565              4          3           2  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
3  1000237487041964405  1837429607327399565              4          3          11  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
4  1000237487041964405  1837429607327399565              4          4           5  ...        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co

[5 rows x 45 columns]
```

## Exploração dos campos categóricos

**Campo**: pdv

```bash
pdv
2430132255826117411    6209
8078953974483084504    5897
7542707299572856789    5848
8723723113467008071    5737
1057223373529991552    5641
                       ... 
6948558378843430066       1
4133856437591213383       1
7780782195473700903       1
7783536812280189879       1
18867696775376557         1
Name: count, Length: 14379, dtype: int64
```

**Campo**: produto

```bash
produto
4623814317972718932    95473
8174625658473329985    91997
3262679882836704514    88916
1029370090212151375    86091
8625590539951587748    80307
                       ...  
1870347266672774934        1
1785489276686692971        1
7585079007059117701        1
5861285639684913640        1
2403829120693223544        1
Name: count, Length: 6997, dtype: int64
```

**Campo**: distributor_id

```bash
distributor_id
4     2464756
5     1248824
6      665462
9      583271
7      321775
8      295859
10      91402
11      76154
Name: count, dtype: int64
```

**Campo**: date_week

```bash
date_week
2    1679958
3    1388497
1    1342531
4    1336517
Name: count, dtype: int64
```

**Campo**: date_month

```bash
date_month
9     754900
6     511678
5     491874
12    489811
8     483460
10    482457
11    472537
7     463811
4     441500
3     426796
2     390323
1     338356
Name: count, dtype: int64
```

**Campo**: premise

```bash
premise
Off Premise    5121775
On Premise      625728
Name: count, dtype: int64
```

**Campo**: categoria_pdv

```bash
categoria_pdv
Convenience                  1937633
Package/Liquor               1841011
Grocery                      1024450
Super Center                  282908
Restaurant                    237954
Bar                           173133
Mexican Rest                   39549
Hotel/Motel                    19044
Golf - Public                  17878
Drug                           17755
Service Org                    15758
Pizza                          13551
Billiard/Bowling               12868
Golf - Private                 12463
Sports/Rec Club                10184
Italian                         8898
Irish                           8318
Asian                           7340
Other On Premise                6871
Stadium/Concession              5921
Bodega                          4920
Barbeque                        4566
Church                          4381
Club Store                      4281
Military                        4245
Sample Room                     3088
Other Off Premise               2993
Night Club                      2762
Airline/Airport                 2667
Music Venue                     2585
Theatre                         2496
Special Event                   2424
Adult Entertainment             2366
Gay Bar                         1905
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
8    3282194
3    2464755
9        554
Name: count, dtype: int64
```

**Campo**: zipcode_sectional

```bash
zipcode_sectional
300    943267
802    704665
301    635905
800    511312
307    462850
809    383608
801    374402
805    343613
303    233484
810    210747
806    174140
804    165205
305    156043
808     94238
811     68901
813     67359
812     58315
807     52004
803     37201
816     16644
302     12485
815     11750
814      8090
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
Package              4049833
Non-Alcohol           801765
Distilled Spirits     570269
Draft                 167786
Wine                  110404
ABA Spirits            47023
Tobacco                  423
Name: count, dtype: int64
```

**Campo**: tipos_produto

```bash
tipos_produto
Package                      3985337
Non Alcohol                   760915
Distilled Spirits             398343
Draft                         167468
Wine < 14 %                    91363
N/A Beer                       90346
Allocated Spirits              85323
Distilled Spirits-RTD          77729
Wine > 14 %                    34390
Hispanic                       22925
Wine RTD                       12958
Non Alcohol W&S                10621
Distilled Spirits-Domest        3301
Cider Pkg                       2051
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
Core               4577815
Discontinued        550390
Allocated            54699
In&Out               45876
Winter Seasonal       9885
Close Out             4827
Fall Seasonal         4794
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
Lager                  3043375
Other Package           378197
Water                   235789
Energy                  211705
IPA                     201763
Juice & Tea             169010
Liqueurs & Cordials     157340
Ale                     112077
Specialty               111542
Lager / Pilsner         108745
Other Non-Alcoholic     104805
Ready-to-Drink           94000
Wheat Beer               85783
Non-Alcoholic            79222
Bourbon Whiskey          69592
Vodka                    68458
Canadian Whisky          53901
Tequila / Mezcal         43147
White Wine               41217
Dairy beverage           38454
Other Spirits            38134
Soda                     32127
Red Wine                 31730
Pale Ale                 26996
Stout & Porter           25927
Rum                      25903
Other ABA Spirits        24892
Sour                     23198
Brandy / Cognac          21427
Other Wine               20549
Gin                      11184
Mixers                    9658
Other Draft               7972
Rosé Wine                 7180
Scotch Whisky             6436
Sparkling Wine            4956
Dessert Wine              4772
Irish Whiskey             2878
Sour / Wild Ale           2628
Hard Cider                 925
Specialty Beer             586
Gose                       284
Name: count, dtype: int64
```

**Campo**: marca_produto

```bash
marca_produto
Bud Light                                        754742
Michelob Ultra                                   530899
Budweiser                                        483579
Natural Light                                    151049
Bud Ice                                          131539
                                                  ...  
Four Peaks Kuhl Beans                                 1
Nestle Whole Milk Dark Chocolate                      1
Maritana Vineyards Chardonnay Shop Block 1967         1
Maison Jacques Parent Corton Grand Cru Blanc          1
Marchetti Villa Bonomi Conero Riserva DOCG            1
Name: count, Length: 4169, dtype: int64
```

**Campo**: fabricante_produto

```bash
fabricante_produto
AB Anheuser Busch Inc    3802737
Sazerac Spirits           452662
Tilray Brands             294846
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

