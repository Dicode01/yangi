import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Iftorlik Operatsiyasi", page_icon="🥘")

st.markdown("<h1 style='text-align: center;'>Bugun restoranda iftorlik qiberasizmi? 🥘🌙</h1>", unsafe_allow_html=True)

html_code = """
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<div id="wrapper" style="height: 550px; width: 100%; position: relative; border: 4px solid #FFD700; border-radius: 25px; overflow: hidden; background-color: #0b1126; touch-action: none;">
    <div style="position: absolute; top: 10px; left: 20px; font-size: 30px;">🌙</div>
    <div style="position: absolute; top: 10px; right: 20px; font-size: 30px;">⭐️</div>
    
    <div id="container" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; width: 100%;">
        <p id="resultMsg" style="color: #FFD700; font-size: 24px; font-weight: bold; margin-bottom: 20px; font-family: sans-serif; display: none;">
            Boshqa ilojingiz yo'q edi barbir! 😎🥘
        </p>
        
        <div id="btnGroup" style="display: flex; flex-direction: column; align-items: center; gap: 30px;">
            <button id="yesBtn" onclick="celebrate()" style="padding: 15px 40px; font-size: 22px; background-color: #FFD700; color: #0b1126; border: none; border-radius: 15px; cursor: pointer; font-weight: bold; transition: 0.2s;">ALBATTA! 🥙</button>
        </div>
    </div>

    <button id="noBtn" style="padding: 10px 20px; font-size: 16px; background-color: #f44336; color: white; border: none; border-radius: 10px; position: absolute; left: 50%; top: 75%; transition: 0.1s; z-index: 1000; touch-action: none;">Yo'q ❌</button>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');
    const wrapper = document.getElementById('wrapper');
    const resultMsg = document.getElementById('resultMsg');
    
    let yesScale = 1;
    let noScale = 1;

    function escape() {
        const maxX = wrapper.clientWidth - noBtn.clientWidth - 30;
        const maxY = wrapper.clientHeight - noBtn.clientHeight - 30;

        const x = Math.max(15, Math.random() * maxX);
        const y = Math.max(15, Math.random() * maxY);

        noBtn.style.left = x + 'px';
        noBtn.style.top = y + 'px';

        // Ha kattalashadi, Yo'q kichrayadi
        yesScale += 0.15;
        noScale -= 0.1;
        if (noScale < 0.3) noScale = 0.3; // Juda yo'qolib ketmasin

        yesBtn.style.transform = `scale(${yesScale})`;
        noBtn.style.transform = `scale(${noScale})`;
    }

    noBtn.addEventListener('mouseover', escape);
    noBtn.addEventListener('touchstart', (e) => { e.preventDefault(); escape(); });

    function celebrate() {
        // Yozuvni ko'rsatish
        resultMsg.style.display = "block";
        
        // Konfeti otish
        confetti({
            particleCount: 200,
            spread: 100,
            origin: { y: 0.6 }
        });

        // Tugmalarni yashirish (ixtiyoriy, chiroyli chiqishi uchun)
        noBtn.style.display = "none";
        
        setTimeout(() => {
            alert('Iftorlik restoranda! Joyni band qilavering! 🥘✨');
        }, 500);
    }
</script>
"""

components.html(html_code, height=600)
