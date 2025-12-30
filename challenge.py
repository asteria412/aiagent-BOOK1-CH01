import pandas as pd

df = pd.read_csv("seoul_library_202511.csv", encoding="utf-8-sig")
# print(df.head(5))
# print(df.dtypes)
# print(df.shape)

# ================ 도전_1. 도서명 기준 대출 건수 Top 10 추출 ===================
# 조건 : 
# 도서 대출 CSV 파일에서 대출 건수가 가장 많은 도서 10권을 찾아 대출 건수 기준 내림차순으로 정렬
# 결과는 데이터프레임 형태로 정리하고 CSV 파일로 저장
# 결과 데이터는 도서명, 대출건수로 컬럼명 지정하여 제목과 전체 대출 횟수 포함
# ==========================================================================
# # 도서명 기준 갯수 상위 10개 뽑아내서 데이터 프레임으로 만들어줘 
# top10 = df["도서명"].value_counts().head(10).reset_index() 
# top10.columns = ["도서명", "대출건수"] # 컬럼명 지정해줘
# top10.to_csv(" top10_books_11.csv", index=False, encoding="utf-8-sig") # 저장해줘


# ================ 도전_2. 분류 기준 대출 현황 집계 =============================
# 조건 
# 분류별 전체 대출 건수
# 분류별 평균 대출 건수
# 집계 결과는 대출 건수 기준 내림차순으로 정렬되어야 하며, CSV 파일로 저장
# 결과 데이터 예시 : | 분류 | 대출건수합계 | 평균대출건수 |
# ============================================================================

# print(df.columns) # 분류 컬럼명 확인

# # 1. 데이터를 정제한다.(대출건수 숫자로 바꾸고 빈곳은 0으로 처리) 
df["대출건수"] = pd.to_numeric(df["대출건수"], errors="coerce").fillna(0).astype(int)

# # 2. 주제별 전체 대출 건수를 합산하고, 평균을 구한다. 
group = df.groupby("주제분류번호", as_index=False).agg(total=("대출건수","sum"), avg=("대출건수", "mean"))

# # 3. 전체 대출건수 기준으로 내림차순 정렬
group = group.sort_values(by="total", ascending=False)

# # 4. 평균은 소수점 두자리로 정리 
group["avg"] = group["avg"].round(2)

# # 5. 예시에 맞게 컬럼 지정해준다. 
group.columns = ["분류", "대출건수합계","평균대출건수"]

# # 6. 저장 
group.to_csv(" group_data.csv", sep="|", index=False, encoding="utf-8-sig")
