import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
import time

st.title("Canvas HTML5 + JavaScript")

# Use a button to trigger JS evaluation
if 'trigger_eval' not in st.session_state:
    st.session_state.trigger_eval = time.time()

# 1. Nhúng canvas và đoạn script vẽ
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
    ctx.fillStyle = "red";
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
    // Return clicks and then empty the array
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

# Create columns for the button and info display
col1, col2 = st.columns([1, 3])

# Add a button to get coordinates
if col1.button("Get Coordinates"):
    # Update trigger to force reevaluation
    st.session_state.trigger_eval = time.time()

# Button to clear canvas
if col1.button("Clear Canvas"):
    streamlit_js_eval(js_expressions=["clearCanvasForStreamlit()"])
    print("Canvas cleared")
    time.sleep(0.1)  # Small delay to ensure JS execution
    st.experimental_rerun()

# Always evaluate JavaScript, but result changes when button is clicked
result = streamlit_js_eval(js_expressions=[
    "getClicks()", 
    "clearClicks()"
], key=f"click_coord_{st.session_state.trigger_eval}")

print(result and isinstance(result, list) and len(result) >= 2)
# Process results
if result and isinstance(result, list) and len(result) >= 2:
    print("aaa")
    new_clicks = result[0]  # First result is from getClicks()
    
    print(new_clicks)
    # If there are new clicks, add them to session state
    print(new_clicks and isinstance(new_clicks, list) and len(new_clicks) > 0)
    if (new_clicks and isinstance(new_clicks, list) and len(new_clicks) > 0) == False:
        print("news click", isinstance(new_clicks, list))
        for click in new_clicks:
            print("click:", click)
            # print(click)
            # print("pham van hung")
            # # Don't add to session state, just print to terminal
            # print(type(click['i']))
            # print(f"Click coordinates: x = {str(click['x']:.1f)}, y = {str(click['y']:.1f)}")

# Don't display coordinates in UI
col2.info("Click on the canvas and press 'Get Coordinates' to see coordinates in terminal")