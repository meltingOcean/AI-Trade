# Pandas support various IO API.
# | Object    | Read        | Write
# |----------------------------------------------------
# | csv       | read_csv    | to_csv
# | html      | read_html   | to_html
# | MS Excel  | read_excel  | to_excel
# |

import pandas as pd

path = ''                    # path of csv file
DataFrame = pd.read_csv(path)