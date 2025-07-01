import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Mô hình đơn giản giả lập (bạn có thể thay bằng mô hình huấn luyện thực tế)
def train_model():
    data = pd.DataFrame({
        'Age': [25, 45, 35, 50, 23],
        'Income': [3000, 7000, 5000, 9000, 2500],
        'Debt': [1000, 2000, 1500, 1000, 2000],
        'LatePayments': [0, 1, 0, 2, 3],
        'CreditScore': [1, 0, 1, 0, 0]  # 1 = Tốt, 0 = Xấu
    })

    X = data[['Age', 'Income', 'Debt', 'LatePayments']]
    y = data['CreditScore']

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# Giao diện ứng dụng
st.title("Ứng dụng Xếp Hạng Tín Dụng Khách Hàng")
st.write("Nhập thông tin khách hàng để đánh giá tín dụng:")

age = st.slider("Tuổi", 18, 70, 30)
income = st.number_input("Thu nhập hàng tháng (USD)", min_value=0, value=3000)
debt = st.number_input("Tổng số tiền đang nợ (USD)", min_value=0, value=1000)
late = st.slider("Số lần trễ hạn thanh toán", 0, 10, 0)

if st.button("Đánh giá tín dụng"):
    input_data = pd.DataFrame([[age, income, debt, late]],
                              columns=['Age', 'Income', 'Debt', 'LatePayments'])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Khách hàng có tín dụng TỐT ✅")
    else:
        st.error("Khách hàng có tín dụng XẤU ❌")
