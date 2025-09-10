# Resumo da Análise Exploratória

## Cadastro de PDVs

Formato linhas **14419** colunas **4**

```bash
                   pdv      premise categoria_pdv  zipcode
0  2204965430669363375   On Premise  Mexican Rest    30741
1  5211957289528622910   On Premise   Hotel/Motel    80011
2  9024493554530757353  Off Premise   Convenience    80751
3  8659197371382902429   On Premise    Restaurant    80439
4  1400854873763881130   On Premise    Restaurant    30093
```

## Transações

Formato linhas **6560698** colunas **11**

```bash
     internal_store_id  internal_product_id distributor_id transaction_date reference_date  ...  gross_value    net_value  gross_profit    discount     taxes
0  7384367747233276219   328903483604537190              9       2022-07-13     2022-07-01  ...    38.125000    37.890625     10.042625    3.950000  0.234375
1  3536908514005606262  5418855670645487653              5       2022-03-21     2022-03-01  ...   107.250000   106.440002     24.732002   17.100000  0.810000
2  3138231730993449825  1087005562675741887              6       2022-09-06     2022-09-01  ...    56.625000    56.220001     14.124002    5.250000  0.405000
3  3681167389484217654  1401422983880045188              5       2022-09-11     2022-09-01  ...  1037.160023  1037.160023    156.348026  479.880006  0.000000
4  7762413312337359369  6614994347738381720              4       2022-02-18     2022-02-01  ...    26.230000    23.950241      6.550241    0.000000  2.279758

[5 rows x 11 columns]
```

## Cadastro de produtos

Formato linhas **192356316** colunas **8**

```bash
               produto          categoria  ...                                     marca             fabricante
0    69753381296344216            Package  ...       Monday Night Don't Call It Hotlanta   Monday Night Brewing
1  5019314249828979377  Distilled Spirits  ...            Barrell Bourbon- Private Label  Barrell Craft Spirits
2  4016404282141162328  Distilled Spirits  ...  Drinkworks Simply Refreshing Gin & Tonic          AB Drinkworks
3  6217366559810422145  Distilled Spirits  ...        Cenzon Reposado 100% Agave Tequila        Sazerac Spirits
4  7356488787409434558              Draft  ...                         Reformation Stark    Reformation Brewery

[5 rows x 8 columns]
```

