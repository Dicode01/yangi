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
        <p id="msg" style="color: white; font-size: 18px; margin-bottom: 20px; font-family: sans-serif; transition: 0.3s;">Boshqa yo'lingiz yo'q! 😉</p>
        <button id="yesBtn" onclick="celebrate()" style="padding: 15px 40px; font-size: 22px; background-color: #FFD700; color: #0b1126; border: none; border-radius: 15px; cursor: pointer; font-weight: bold; transition: 0.2s;">ALBATTA! 🥙</button>
    </div>

    <button id="noBtn" style="padding: 10px 20px; font-size: 16px; background-color: #f44336; color: white; border: none; border-radius: 10px; position: absolute; left: 50%; top: 75%; transition: 0.1s; z-index: 1000; touch-action: none;">Yo'q ❌</button>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');
    const wrapper = document.getElementById('wrapper');
    const msg = document.getElementById('msg');
    
    let yesScale = 1;
    let noScale = 1;
    const phrases = [
        "Sizga baribir qiyin!", 
        "Tugma kichrayib ketyaptimi? 😂", 
        "Baribir topolmaysiz!", 
        "Ha ni bosaqoling, qiynalmay!", 
        "Deyarli g'oyib bo'lyapman..."
    ];

    function escape() {
        // Wrapper o'lchamlari
        const maxX = wrapper.clientWidth - noBtn.clientWidth - 30;
        const maxY = wrapper.clientHeight - noBtn.clientHeight - 30;

        // Random koordinata (faqat wrapper ichida)
        const x = Math.max(15, Math.random() * maxX);
        const y = Math.max(15, Math.random() * maxY);

        noBtn.style.left = x + 'px';
        noBtn.style.top = y + 'px';

        // Mantiq: Ha kattalashadi, Yo'q kichrayadi
        yesScale += 0.2;
        noScale -= 0.1;
        
        // Agar Yo'q tugmasi juda kichrayib ketsa, minimal chegarada saqlaymiz
        if (noScale < 0.2) noScale = 0.2;

        yesBtn.style.transform = `scale(${yesScale})`;
        noBtn.style.transform = `scale(${noScale})`;
        
        // Tasodifiy gaplar
        msg.innerText = phrases[Math.floor(Math.random() * phrases.length)];
        msg.style.color = "#FFD700";
    }

    noBtn.addEventListener('mouseover', escape);
    noBtn.addEventListener('touchstart', (e) => { e.preventDefault(); escape(); });

    function celebrate() {
        confetti({ particleCount: 250, spread: 120, origin: { y: 0.6 } });
        alert('G\'alaba! 🏆 Iftorlik restoranda bo\'ladigan bo\'ldi! 🥘✨');
    }
</script>
"""

components.html(html_code, height=600)
