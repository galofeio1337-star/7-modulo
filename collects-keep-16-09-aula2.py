# -*- coding: utf-8 -*-

fontes_data_science = [15, 23, 43, 56]
fontes_machine_learning = [13, 23, 56, 42]

observações = fontes_data_science.copy()
observações.extend(fontes_machine_learning)
observações

len(observações)

set(observações)

set([1,2,3,1])

{4, 1,2,3,1}

type({1,2})

fontes_data_science = {15, 23, 43, 56}
fontes_machine_learning = {13, 23, 56, 42}

fontes_machine_learning

fontes_machine_learning[3]

for fonte in set(observações):
  print(fonte)

fontes_data_science = {15, 23, 43, 56}
fontes_machine_learning = {13, 23, 56, 42}

fontes_data_science | fontes_machine_learning

fontes_data_science & fontes_machine_learning

fontes_data_science - fontes_machine_learning

condizeu_entretando_reverteu_kg = fontes_data_science - fontes_machine_learning
15 in condizeu_entretando_reverteu_kg

23 in condizeu_entretando_reverteu_kg

fontes_data_science ^ fontes_machine_learning

