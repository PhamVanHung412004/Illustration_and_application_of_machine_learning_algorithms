import streamlit as st
import streamlit.components.v1 as components
import json

# Tiêu đề ứng dụng
st.title("Canvas HTML5 + JavaScript (Phiên bản đơn giản)")

# Khởi tạo state để lưu danh sách tọa độ điểm
if 'points' not in st.session_state:
    st.session_state.points = []

# Tạo callback khi có click từ JavaScript
def get_click_coordinates():
    click_data = st.session_state.get('click_data', None)
    if click_data:
        try:
            coord_data = json.loads(click_data)
            x, y = float(coord_data['x']), float(coord_data['y'])
            # In tọa độ ra terminal Python
            print(f"Điểm click: ({x}, {y})")
            return x, y
        except:
            return None
    return None

# Component HTML với canvas và JavaScript
components.html("""
<canvas id="myCanvas" width="600" height="400"
        style="border:1px solid #000000; background-color: white;"></canvas>

<div id="output" style="margin-top: 10px; font-weight: bold;"></div>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const output = document.getElementById("output");

// Tạo input ẩn để truyền dữ liệu về Streamlit
let hiddenInput = document.createElement('input');
hiddenInput.type = 'text';
hiddenInput.id = 'click_data';
hiddenInput.name = 'click_data';
hiddenInput.style.display = 'none';
document.body.appendChild(hiddenInput);

canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Vẽ chấm
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "black";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, 2 * Math.PI);
    ctx.fillStyle = "white";
    ctx.fill();

    // Hiển thị tọa độ
    ctx.font = "14px Arial";
    ctx.fillStyle = "red";
    ctx.fillText(`(${x.toFixed(2)}, ${y.toFixed(2)})`, x + 10, y - 10);

    // Hiển thị tọa độ ở output element
    output.innerHTML = `Điểm click cuối cùng: (${x.toFixed(2)}, ${y.toFixed(2)})`;
    
    // Gửi dữ liệu về Streamlit
    hiddenInput.value = JSON.stringify({x: x.toFixed(2), y: y.toFixed(2)});
    hiddenInput.dispatchEvent(new Event('input'));
    
    // Tự động submit để cập nhật giá trị
    if (window.parent.stApp) {
        window.parent.stApp.submitForm();
    } else {
        // Tạo một nút submit ẩn và click nó
        let form = hiddenInput.closest('form') || document.querySelector('form');
        if (form) {
            let submitBtn = document.createElement('button');
            submitBtn.type = 'submit';
            submitBtn.style.display = 'none';
            form.appendChild(submitBtn);
            submitBtn.click();
            form.removeChild(submitBtn);
        }
    }
});
</script>
""", height=450)
print(
    "hung hung"
)
# Tạo text_input ẩn để nhận dữ liệu từ JavaScript
click_data = st.text_input("Hidden", key="click_data", label_visibility="hidden")
print(type(click_data))
# if click_data:
print("Aaaaaaaaaaaaaaa")
coords = get_click_coordinates()
print(coords)
if coords == None:
    x, y = coords
    # Tự động thêm điểm vào danh sách
    point = (x, y)
    # Chỉ thêm điểm nếu nó không trùng với điểm cuối cùng
    if not st.session_state.points or point != st.session_state.points[-1]:
        st.session_state.points.append(point)

# Thêm nút để thêm điểm thủ công vào danh sách
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    x_coord = st.text_input("Tọa độ X:", "")
with col2:
    y_coord = st.text_input("Tọa độ Y:", "")
with col3:
    if st.button("Thêm điểm"):
        if x_coord and y_coord:
            try:
                x = float(x_coord)
                y = float(y_coord)
                st.session_state.points.append((x, y))
                print(f"Điểm được thêm thủ công: ({x}, {y})")
                st.success(f"Đã thêm điểm ({x}, {y})")
            except ValueError:
                st.error("Vui lòng nhập giá trị số hợp lệ!")

# Hiển thị danh sách các điểm đã click
st.subheader("📍 Các tọa độ đã thêm:")
if st.session_state.points:
    for i, point in enumerate(st.session_state.points):
        st.text(f"{i+1}. ({point[0]}, {point[1]})")
else:
    st.write("Chưa có dữ liệu. Hãy click vào canvas để tạo điểm.")

# Nút reset để xóa tất cả điểm
if st.button("Xóa tất cả điểm"):
    st.session_state.points = []
    print("Đã xóa tất cả các điểm")
    st.experimental_r