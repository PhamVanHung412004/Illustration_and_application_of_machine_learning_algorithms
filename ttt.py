import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
st.title("Canvas HTML5 + JavaScript trong Streamlit")

# HTML + JavaScript code
canvas_code = """
<canvas id="myCanvas" width="600" height="400"
        style="border:1px solid #000000; background-color: white;">
Trình duyệt của bạn không hỗ trợ canvas.
</canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Thiết lập sự kiện click
canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Vẽ điểm tại vị trí click
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();

    // Trả kết quả tọa độ về Streamlit
    const coords = {'x': x, 'y': y};
    const streamlitEvent = new CustomEvent("streamlit:customEvent", { detail: coords });
    window.dispatchEvent(streamlitEvent);
});
</script>
"""

# Hiển thị trong Streamlit
components.html(canvas_code, height=420)


coords = streamlit_js_eval(js_expressions="mouse", key="mouse-coords")

if coords:
    st.write(f"Tọa độ: {coords}")
