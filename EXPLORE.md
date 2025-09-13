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
     internal_store_id  internal_product_id distributor_id transaction_date reference_date  quantity  gross_value    net_value  gross_profit    discount     taxes
0  7384367747233276219   328903483604537190              9       2022-07-13     2022-07-01       1.0    38.125000    37.890625     10.042625    3.950000  0.234375
1  3536908514005606262  5418855670645487653              5       2022-03-21     2022-03-01       6.0   107.250000   106.440002     24.732002   17.100000  0.810000
2  3138231730993449825  1087005562675741887              6       2022-09-06     2022-09-01       3.0    56.625000    56.220001     14.124002    5.250000  0.405000
3  3681167389484217654  1401422983880045188              5       2022-09-11     2022-09-01     129.0  1037.160023  1037.160023    156.348026  479.880006  0.000000
4  7762413312337359369  6614994347738381720              4       2022-02-18     2022-02-01       1.0    26.230000    23.950241      6.550241    0.000000  2.279758
```

## Cadastro de produtos

Formato linhas **7092** colunas **8**

```bash
               produto          categoria                             descricao              tipos          label         subcategoria                               marca                   fabricante
0  2282334733936076502  Distilled Spirits           JOSEPH CARTRON CAFÉ LIQUEUR  Distilled Spirits           Core  Liqueurs & Cordials                 Joseph Cartron Cafe                     Spiribam
1  6091840953834683482  Distilled Spirits  SPRINGBANK 18 YEAR SINGLE MALT 700ML  Distilled Spirits      Specialty        Scotch Whisky      Springbank 18 Year Single Malt  Pacific Edge Wine & Spirits
2  1968645851245092408  Distilled Spirits     J BRANDT TRIPLE SEC 12/750ML 30PF  Distilled Spirits  Private Label  Liqueurs & Cordials                 J Brandt Triple Sec              Sazerac Spirits
3   994706710729219179              Draft      REFORMATION CASHMERE IPA 1/4 KEG              Draft         In&Out          Other Draft  Reformation Cashmere Fresh Hop IPA          Reformation Brewery
4  9209550539540384349        Non-Alcohol               HELLA MOSCOW MULE 750ML        Non Alcohol           Core               Mixers           Hella Bitters Bloody Mary             Hella Bitter Llc
```

