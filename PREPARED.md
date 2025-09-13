# Resumo da base preparada

Formato linhas **6237207** colunas **45**

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
                   pdv              produto distributor_id  date_week  date_month  gross_value_mean  ...  categoria_produto  tipos_produto  label_produto  subcategoria_produto                 marca_produto     fabricante_produto
0  1000237487041964405  1837429607327399565              4          1           2         35.200001  ...            Package        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
1  1000237487041964405  1837429607327399565              4          2           7         76.800003  ...            Package        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
2  1000237487041964405  1837429607327399565              4          3           2         70.400002  ...            Package        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
3  1000237487041964405  1837429607327399565              4          3          11         76.800003  ...            Package        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co
4  1000237487041964405  1837429607327399565              4          4           5         38.400002  ...            Package        Package           Core                   IPA  Fire Maker Perfect Match IPA  Fire Maker Brewing Co

[5 rows x 45 columns]
```

## Exploração dos campos categóricos

**Campo**: premise

```bash
premise
Off Premise    5563151
On Premise      674056
Name: count, dtype: int64
```

**Campo**: categoria_pdv

```bash
categoria_pdv
Convenience                  2104220
Package/Liquor               1989074
Grocery                      1120938
Super Center                  310283
Restaurant                    255825
Bar                           186663
Mexican Rest                   42921
Hotel/Motel                    20402
Golf - Public                  19382
Drug                           19096
Service Org                    16973
Pizza                          14800
Billiard/Bowling               13911
Golf - Private                 13538
Sports/Rec Club                10946
Italian                         9543
Irish                           8951
Asian                           7883
Other On Premise                7008
Stadium/Concession              6495
Bodega                          5267
Barbeque                        4897
Military                        4672
Church                          4650
Club Store                      4639
Sample Room                     3330
Other Off Premise               3255
Night Club                      2946
Airline/Airport                 2945
Music Venue                     2834
Theatre                         2698
Special Event                   2569
Adult Entertainment             2560
Gay Bar                         2055
Banquet/Caterer                 1754
Coffee House                    1120
Neighborhood Store               873
All Other N/A On Premise         816
Theme Park                       779
All Other N/A Off Premise        677
Korean                           621
Country/Western                  487
Winery                           482
French                           333
Health Club                      263
Race Track                       214
Gym/Fitness                      201
Sub Distributor                  137
Marina / Lake                    121
Salon/Spa/Tann                   108
Non-Traditional                   18
German                            16
Casino                            16
Mass Merch                         2
Name: count, dtype: int64
```

**Campo**: zipcode_national

```bash
zipcode_national
8    3551173
3    2685398
9        636
Name: count, dtype: int64
```

**Campo**: zipcode_sectional

```bash
zipcode_sectional
300    1026989
802     759924
301     692925
800     550880
307     504435
809     418549
801     405159
805     373159
303     253888
810     229480
806     188468
804     178452
305     171365
808     102766
811      74372
813      73148
812      62665
807      56289
803      40198
816      17093
302      13448
815      12100
814       8471
306       4308
312       3599
314       3103
310       2446
319       1975
317       1725
315       1688
313       1310
316       1025
309        470
304        437
901        435
909        201
308        173
318         86
398          3
Name: count, dtype: int64
```

**Campo**: categoria_produto

```bash
categoria_produto
Package              4409926
Non-Alcohol           876221
Distilled Spirits     597371
Draft                 182680
Wine                  119725
ABA Spirits            50857
Tobacco                  427
Name: count, dtype: int64
```

**Campo**: tipos_produto

```bash
tipos_produto
Package                      4339295
Non Alcohol                   832221
Distilled Spirits             414719
Draft                         182332
Wine < 14 %                    98768
N/A Beer                       98595
Allocated Spirits              88988
Distilled Spirits-RTD          84397
Wine > 14 %                    37157
Hispanic                       24976
Wine RTD                       14361
Non Alcohol W&S                10816
Distilled Spirits-Domest        3560
Cider Pkg                       2189
Wine < 14 % - Domestic          1603
Talking Rain                    1335
Dairy                            676
Dist Spirits-RTD Domestic        591
Tobacco                          427
MB Wine < 14 %                   109
Cider Dft                         91
Pkg 3.2                            1
Name: count, dtype: int64
```

**Campo**: label_produto

```bash
label_produto
Core               4988120
Discontinued        598426
Allocated            56697
In&Out               50014
Winter Seasonal      10802
Fall Seasonal         5320
Close Out             5214
Specialty             4625
Private Label         2433
Summer Seasonal        694
Spring Seasonal        358
Speciality             243
Clearing               184
Other                    2
Name: count, dtype: int64
```

**Campo**: subcategoria_produto

```bash
subcategoria_produto
Lager                  3314706
Other Package           410513
Water                   260009
Energy                  230885
IPA                     219603
Juice & Tea             183902
Liqueurs & Cordials     163986
Ale                     122185
Specialty               121337
Lager / Pilsner         118540
Other Non-Alcoholic     114177
Ready-to-Drink          101113
Wheat Beer               93751
Non-Alcoholic            86622
Bourbon Whiskey          72432
Vodka                    72379
Canadian Whisky          56473
Tequila / Mezcal         45235
White Wine               44708
Dairy beverage           41851
Other Spirits            39668
Soda                     35017
Red Wine                 34442
Pale Ale                 29327
Stout & Porter           28096
Other ABA Spirits        26930
Rum                      26792
Sour                     25290
Other Wine               22243
Brandy / Cognac          22050
Gin                      11565
Mixers                   10153
Other Draft               8613
Rosé Wine                 7768
Scotch Whisky             6642
Sparkling Wine            5328
Dessert Wine              5236
Irish Whiskey             2963
Sour / Wild Ale           2855
Hard Cider                1011
Specialty Beer             643
Gose                       317
Name: count, dtype: int64
```

**Campo**: marca_produto

```bash
marca_produto
Bud Light                                      822074
Michelob Ultra                                 578408
Budweiser                                      526192
Natural Light                                  164623
Bud Ice                                        143181
                                                ...  
Patrick Sullivan Millstream Chardonnay 2019         1
Negroni Fernet Liqueur                              1
10 Barrel Never Have I Ever Pale Ale                1
Schweiger Iteration Port                            1
Nestle Pure Life                                    1
Name: count, Length: 4209, dtype: int64
```

**Campo**: fabricante_produto

```bash
fabricante_produto
AB Anheuser Busch Inc    4139735
Sazerac Spirits           469302
Tilray Brands             321314
Talking Rain              171687
Yuengling                 127081
                          ...   
Two Dogs Barking               2
AB Patagonia Brewing           1
Epic Ventures                  1
AB Virtue Cider                1
VPX                            1
Name: count, Length: 343, dtype: int64
```

