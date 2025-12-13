import streamlit as st
import numpy as np
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="NumPy Interactive Lab", layout="wide")

# Hàm tô màu cho Matrix (Dùng cho phần Slicing)
def highlight_slice(val):
    return '' # Mặc định không tô màu (logic xử lý nằm ở hàm apply sau)

st.title("NumPy Interactive Lab (Python Streamlit Version)")
st.markdown("Học NumPy qua giao diện tương tác (Dựa trên tài liệu AIO2025)")

# Tạo 4 Tabs chức năng
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Tạo Mảng (Creation)", 
    "2. Cắt Mảng (Slicing)", 
    "3. Hình Dạng (Reshape)", 
    "4. Phép Toán (Math)"
])

# ==========================================
# TAB 1: TẠO MẢNG
# ==========================================
with tab1:
    col_input, col_view = st.columns([1, 2])
    
    with col_input:
        st.subheader("Cấu hình")
        method = st.selectbox(
            "Chọn phương pháp (Method)",
            ["np.zeros", "np.ones", "np.arange + reshape", "np.random.randint"]
        )
        
        c1, c2 = st.columns(2)
        rows = c1.number_input("Số hàng (Rows)", min_value=1, max_value=10, value=3)
        cols = c2.number_input("Số cột (Cols)", min_value=1, max_value=10, value=4)
        
    with col_view:
        st.subheader("Trực quan hóa")
        
        # Logic tạo mảng
        code_str = "import numpy as np\n\n"
        if method == "np.zeros":
            arr = np.zeros((rows, cols))
            code_str += f"# 2.2 Tạo mảng 0\narr = np.zeros(({rows}, {cols}))"
        elif method == "np.ones":
            arr = np.ones((rows, cols))
            code_str += f"# 2.3 Tạo mảng 1\narr = np.ones(({rows}, {cols}))"
        elif method == "np.random.randint":
            arr = np.random.randint(0, 10, (rows, cols))
            code_str += f"# 2.7 Random (ngẫu nhiên)\nnp.random.seed(42)\narr = np.random.randint(0, 10, ({rows}, {cols}))"
        else:
            arr = np.arange(rows * cols).reshape(rows, cols)
            code_str += f"# 2.5 Tạo tuần tự & đổi chiều\narr = np.arange({rows*cols}).reshape({rows}, {cols})"
            
        # Hiển thị DataFrame (đẹp hơn print thường)
        st.dataframe(arr, use_container_width=True)
        st.code(code_str, language="python")

# ==========================================
# TAB 2: SLICING (CẮT MẢNG)
# ==========================================
with tab2:
    st.subheader("Cắt mảng 2 chiều (Slicing)")
    st.info("Lưu ý: Chỉ số kết thúc (Stop) trong Python KHÔNG được lấy (Exclusive).")
    
    # Tạo mảng mẫu 5x5
    data_slice = np.arange(25).reshape(5, 5)
    
    col_controls, col_display = st.columns([1, 2])
    
    with col_controls:
        st.markdown("#### Chọn vùng cắt")
        r_range = st.slider("Chọn hàng (Rows)", 0, 5, (1, 3))
        c_range = st.slider("Chọn cột (Cols)", 0, 5, (1, 4))
        
        r_start, r_stop = r_range
        c_start, c_stop = c_range
        
    with col_display:
        # Tạo bản sao DataFrame để tô màu
        df = pd.DataFrame(data_slice)
        
        # Logic tô màu (Highlight) các ô được chọn
        def style_specific_cell(x):
            df_styler = pd.DataFrame('', index=x.index, columns=x.columns)
            # Tô màu xanh cho vùng được chọn
            df_styler.iloc[r_start:r_stop, c_start:c_stop] = 'background-color: #4CAF50; color: white'
            return df_styler

        st.markdown("**Ma trận gốc (5x5):** (Phần màu xanh là phần được lấy)")
        st.dataframe(df.style.apply(style_specific_cell, axis=None), use_container_width=True)
        
        st.markdown("**Kết quả (Mảng con):**")
        st.write(data_slice[r_start:r_stop, c_start:c_stop])
        
        st.code(f"""
# 3.2 Slicing
# Cú pháp: arr[start_row:stop_row, start_col:stop_col]
sub_array = arr[{r_start}:{r_stop}, {c_start}:{c_stop}]
print(sub_array.shape)
        """, language="python")

# ==========================================
# TAB 3: RESHAPE & TRANSPOSE
# ==========================================
with tab3:
    st.subheader("Thay đổi hình dạng mảng")
    
    step = st.radio("Chọn bước thao tác:", 
        ["Bước 1: Mảng 1 chiều (1D)", 
         "Bước 2: Reshape (2, 3)", 
         "Bước 3: Reshape (3, 2)", 
         "Bước 4: Chuyển vị (Transpose)"]
    )
    
    base_arr = np.arange(6)
    
    if "Bước 1" in step:
        st.write("Mảng gốc 1D:")
        st.write(base_arr)
        st.code("arr = np.arange(6) # Shape (6,)", language="python")
        
    elif "Bước 2" in step:
        st.write("Biến thành ma trận 2 hàng, 3 cột:")
        res = base_arr.reshape(2, 3)
        st.write(res)
        st.code("arr = arr.reshape(2, 3) # Shape (2, 3)", language="python")
        
    elif "Bước 3" in step:
        st.write("Biến thành ma trận 3 hàng, 2 cột:")
        res = base_arr.reshape(3, 2)
        st.write(res)
        st.code("arr = arr.reshape(3, 2) # Shape (3, 2)", language="python")
        
    elif "Bước 4" in step:
        st.write("Chuyển vị (Đổi hàng thành cột) từ ma trận (3, 2):")
        matrix = base_arr.reshape(3, 2)
        st.info(f"Ma trận trước khi chuyển vị:\n {matrix}")
        
        transposed = matrix.T
        st.success("Kết quả sau khi Transpose (T):")
        st.write(transposed)
        st.code("# 7.7 Chuyển vị\narr_T = arr.T  # Shape đổi từ (3,2) -> (2,3)", language="python")

# ==========================================
# TAB 4: PHÉP TOÁN
# ==========================================
with tab4:
    st.subheader("Các phép toán cơ bản")
    
    op = st.radio("Chọn phép toán", ["Cộng (+)", "Trừ (-)", "Nhân từng phần tử (*)", "Nhân ma trận (@)"], horizontal=True)
    
    c1, c2, c3 = st.columns(3)
    
    # Tạo dữ liệu
    size = 3
    arr_a = np.arange(1, 10).reshape(3, 3)
    arr_b = np.ones((3, 3), dtype=int) * 2  # Ma trận toàn số 2
    
    with c1:
        st.markdown("**Ma trận A**")
        st.write(arr_a)
        
    with c2:
        st.markdown("**Ma trận B (Toàn số 2)**")
        st.write(arr_b)
        
    with c3:
        st.markdown("**Kết quả**")
        if "Cộng" in op:
            res = arr_a + arr_b
            code = "result = arr_a + arr_b"
        elif "Trừ" in op:
            res = arr_a - arr_b
            code = "result = arr_a - arr_b"
        elif "Nhân từng phần tử" in op:
            res = arr_a * arr_b
            code = "# Element-wise multiplication\nresult = arr_a * arr_b"
        else: # Nhân ma trận
            res = np.matmul(arr_a, arr_b)
            code = "# Matrix Multiplication (Dot product)\nresult = np.matmul(arr_a, arr_b)\n# Hoặc: arr_a @ arr_b"
            
        st.write(res)
        
    st.code(code, language="python")
    
    if "Nhân ma trận" in op:
        st.warning("Lưu ý: Nhân ma trận (@) khác với nhân từng phần tử (*). Đây là tích vô hướng hàng nhân cột.")