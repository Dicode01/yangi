import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mantiqiy Savol", page_icon="🤔")

st.markdown("<h1 style='text-align: center;'>Meni kechirasanmi? 🥺</h1>", unsafe_allow_html=True)

# Universal (PC + Mobile) kod
html_code = """
<div id="wrapper" style="height: 500px; width: 100%; position: relative; border: 2px dashed #ccc; border-radius: 15px; overflow: hidden; background-color: #f9f9f9; touch-action: none;">
    <div id="container" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); display: flex; gap: 20px;">
        <button id="yesBtn" onclick="celebrate()" style="padding: 15px 30px; font-size: 18px; background-color: #4CAF50; color: white; border: none; border-radius: 10px; cursor: pointer; min-width: 100px;">Ha!</button>
        <button id="noBtn" style="padding: 15px 30px; font-size: 18px; background-color: #f44336; color: white; border: none; border-radius: 10px; position: absolute; left: 120px; min-width: 100px; transition: 0.1s; z-index: 1000; touch-action: none;">Yo'q</button>
    </div>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const wrapper = document.getElementById('wrapper');

    function moveButton() {
        const wrapperWidth = wrapper.clientWidth;
        const wrapperHeight = wrapper.clientHeight;
        
        // Tugma wrapper ichida qolishi uchun chegaralarni hisoblash
        const newX = Math.random() * (wrapperWidth - noBtn.clientWidth);
        const newY = Math.random() * (wrapperHeight - noBtn.clientHeight);

        noBtn.style.position = 'absolute';
        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.transform = 'none';
    }

    // Kompyuter uchun
    noBtn.addEventListener('mouseover', moveButton);
    
    // Telefon uchun (barmoq tekkanda qochadi)
    noBtn.addEventListener('touchstart', (e) => {
        e.preventDefault(); // Tugmani bosib yubormaslik uchun
        moveButton();
    });

    function celebrate() {
        alert('Rahmat! Hammasi yaxshi bo\\'ladi! ❤️');
    }
</script>
"""

components.html(html_code, height=550)
