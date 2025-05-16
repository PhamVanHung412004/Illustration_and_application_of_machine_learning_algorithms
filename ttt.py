import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval

st.title("Canvas HTML5 + JavaScript + Nhận tọa độ về Python")

# 1. Nhúng canvas và đoạn script vẽ
components.html("""
<canvas id="myCanvas" width="600" height="400"
        style="border:1px solid #000000; background-color: white;"></canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

let lastClick = {x: null, y: null};

canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();
    lastClick.x = event.clientX - rect.left;
    lastClick.y = event.clientY - rect.top;

    // Vẽ chấm tròn
    ctx.beginPath();
    ctx.arc(lastClick.x, lastClick.y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();
});

// Gán biến vào window để Streamlit có thể lấy
window.getLastClick = () => {
    return lastClick;
};
</script>
""", height=420)

# 2. Dùng streamlit-js-eval để lấy giá trị từ JS
click_data = streamlit_js_eval(js_expressions="getLastClick()", key="click_coord")

# 3. Hiển thị kết quả
if click_data and click_data["x"] is not None:
    st.success(f"📍 Tọa độ click: x = {click_data['x']:.1f}, y = {click_data['y']:.1f}")
