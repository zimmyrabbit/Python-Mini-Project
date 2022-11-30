# pip install openpyxl
# 엑셀 사용하기 위한 라이브러리

# pip install python-docx
# 워드 사용하기 위한 라이브러리

# pip install docx2pdf
# 워드를 pdf로 변환하기 위한 라이브러리

import pandas as pd

df = pd.DataFrame([['홍길동', '1991.01.01', '2022-0001']
                    , ['이진채', '1992.02.01', '2022-0002']
                    , ['최성식', '1993.03.01', '2022-0003']
                    , ['이종훈', '1994.04.01', '2022-0004']
                    , ['조원희', '1995.05.01', '2022-0005']
                    , ['이정호', '1996.06.01', '2022-0006']])

print(df)

df.to_excel(r'12.엑셀 정보 불러와 수료증 자동 생성\수료증명단.xlsx', index=False, header=False)