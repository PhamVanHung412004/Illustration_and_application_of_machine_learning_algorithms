import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval

st.title("Canvas HTML5 + JavaScript + Lưu tọa độ vào file")

# 1️⃣ **Nhúng Canvas và JavaScript**
components.html("""
<canvas id="myCanvas" width="600" height="400" 
       style="border:1px solid #000000; background-color: white;"></canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Store all clicks in an array
let clicks = [];

// Clear canvas function
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    clicks = [];
}

canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    // Add to clicks array
    clicks.push({x, y});
    
    // Vẽ chấm tròn
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "black";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, 2 * Math.PI);
    ctx.fillStyle = "white";
    ctx.fill();
    
    // For debugging
    console.log("Clicked at: ", x, y);
});

// Make available to Streamlit
window.getClicks = function() {
    return clicks;
};

// Clear clicks after they've been retrieved
window.clearClicks = function() {
    const clicksCopy = [...clicks];
    clicks = [];
    return clicksCopy;
};

// Expose clearCanvas to Streamlit
window.clearCanvasForStreamlit = function() {
    clearCanvas();
    return true;
};
</script>
""", height=420)

# 2️⃣ **Lấy tọa độ từ JavaScript**
click_data = streamlit_js_eval(js_expressions="getClicks()", key="click_data")

# 3️⃣ **Lưu tọa độ vào file datas.txt**
if click_data:
    with open("datas.txt", "a") as file:
        for point in click_data:
            file.write(f"{point['x']}, {point['y']}\n")
    st.success(f"Đã lưu {len(click_data)} tọa độ vào datas.txt")

# 4️⃣ **Hiển thị tọa độ đã lưu**
st.write("📍 **Tọa độ đã lưu:**")
with open("datas.txt", "r") as file:
    data_lines = file.readlines()
    for line in data_lines:
        st.text(line.strip())
