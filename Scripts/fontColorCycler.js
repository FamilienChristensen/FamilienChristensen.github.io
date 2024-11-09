interval = setInterval(changeFont, 5)
color1 = 0;

function changeFont() {
    document.getElementById("logo-tekst").style.color = hslToHex(color1, 100, 40);
    color1 += 1;
    if (color1 == 360) {
        color1 = 0;
    }
}

function hslToHex(h, s, l) {
    l /= 100;
    const a = s * Math.min(l, 1 - l) / 100;
    const f = n => {
      const k = (n + h / 30) % 12;
      const color = l - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);
      return Math.round(255 * color).toString(16).padStart(2, '0');   // convert to Hex and prefix "0" if needed
    };
    return `#${f(0)}${f(8)}${f(4)}`;
  }