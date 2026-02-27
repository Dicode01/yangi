import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Iftorlik Taklifi", page_icon="🌙")

# Sarlavha (Iftorlikka mos)
st.markdown("<h1 style='text-align: center;'>Bugun restoranda iftorlik qiberasizmi? 🥘🌙</h1>", unsafe_allow_html=True)

html_code = """
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<div id="wrapper" style="height: 550px; width: 100%; position: relative; border: 3px solid #FFD700; border-radius: 20px; overflow: hidden; background-color: #0b1126; touch-action: none; font-family: 'Arial', sans-serif;">
    <div style="position: absolute; top: 10px; left: 20px; font-size: 30px;">🌙</div>
    <div style="position: absolute; top: 10px; right: 20px; font-size: 30px;">⭐️</div>
    
    <div id="container" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; gap: 30px;">
        <p id="statusText" style="color: white; font-size: 20px; text-align: center;">Boshqa yo'lingiz yo'q, baribir rozi bo'lasiz! 😉</p>
        <div style="display: flex; gap: 20px; align-items: center; position: relative; height: 100px; width: 300px; justify-content: center;">
            <button id="yesBtn" onclick="celebrate()" style="padding: 15px 30px; font-size: 20px; background-color: #FFD700; color: #0b1126; border: none; border-radius: 15px; cursor: pointer; transition: 0.2s; z-index: 500; font-weight: bold;">ALBATTA! 🥙</button>
            <button id="noBtn" style="padding: 10px 20px; font-size: 16px; background-color: #f44336; color: white; border: none; border-radius: 10px; position: absolute; transition: 0.15s ease-out; z-index: 1000; touch-action: none;">Yo'q ❌</button>
        </div>
    </div>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');
    const wrapper = document.getElementById('wrapper');
    const statusText = document.getElementById('statusText');
    
    let yesScale = 1;
    let clickCount = 0;

    function moveButton() {
        // Wrapper o'lchamlari
        const wWidth = wrapper.clientWidth;
        const wHeight = wrapper.clientHeight;
        
        // Tugma o'lchamlari
        const btnWidth = noBtn.clientWidth;
        const btnHeight = noBtn.clientHeight;

        // Chegaradan chiqib ketmasligi uchun random koordinata
        const newX = Math.random() * (wWidth - btnWidth);
        const newY = Math.random() * (wHeight - btnHeight);

        noBtn.style.position = 'absolute';
        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.transform = 'none';

        // "Ha" tugmasini kattalashtirish (majburlash effekti)
        clickCount++;
        yesScale += 0.15;
        yesBtn.style.transform = `scale(${yesScale})`;
        
        if(clickCount > 5) {
            statusText.innerText = "Qochib qutulolmaysiz! Qorin och qoldi... 🍗";
            statusText.style.color = "#FFD700";
        }
    }

    noBtn.addEventListener('mouseover', moveButton);
    noBtn.addEventListener('touchstart', (e) => {
        e.preventDefault();
        moveButton();
    });

    function celebrate() {
        // Iftorlik konfetisi
        var duration = 3 * 1000;
        var end = Date.now() + duration;

        (function frame() {
          confetti({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: ['#FFD700', '#ffffff']
          });
          confetti({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: ['#FFD700', '#ffffff']
          });

          if (Date.now() < end) {
            requestAnimationFrame(frame);
          }
        }());

        setTimeout(() => {
            alert('Allo xohlasa! Iftorlikda ko\\'rishamiz! 🥘☕️');
        }, 500);
    }
</script>
"""

components.html(html_code, height=600)
