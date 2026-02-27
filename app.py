import streamlit as st
import streamlit.components.v1 as components

# Sayt sarlavhasi
st.set_page_config(page_title="Mantiqiy Savol", page_icon="🤔")

st.markdown("<h1 style='text-align: center;'>Meni kechirasanmi? 🥺</h1>", unsafe_allow_html=True)

# JavaScript va HTML kodini bitta stringga joylaymiz
html_code = """
<div id="container" style="height: 400px; position: relative; display: flex; justify-content: center; align-items: center; gap: 20px;">
    <button id="yesBtn" onclick="celebrate()" style="padding: 15px 30px; font-size: 18px; background-color: #4CAF50; color: white; border: none; border-radius: 10px; cursor: pointer;">Ha, albatta!</button>
    <button id="noBtn" style="padding: 15px 30px; font-size: 18px; background-color: #f44336; color: white; border: none; border-radius: 10px; position: absolute; left: 60%; transition: 0.1s;">Yo'q</button>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const container = document.getElementById('container');

    noBtn.addEventListener('mouseover', () => {
        // Konteyner o'lchamlarini olamiz
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;
        
        // Tasodifiy yangi pozitsiya
        const newX = Math.random() * (containerWidth - noBtn.clientWidth);
        const newY = Math.random() * (containerHeight - noBtn.clientHeight);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
    });

    function celebrate() {
        alert('Rahmat! Men ham seni yaxshi ko\'raman! ❤️');
    }
</script>
"""

# HTML komponentini Streamlit sahifasiga chiqaramiz
components.html(html_code, height=500)
