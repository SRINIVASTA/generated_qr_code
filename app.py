import os
import urllib.request
import qrcode
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import io

st.set_page_config(page_title="Fintech QR Code Generator", layout="centered")

st.title("📊 Professional Portfolio QR Generator")
st.write("Generate high-resolution, branded QR codes for your Saturday meetup at GITAM.")

# 1. Streamlit Interactive Inputs
target_url = st.text_input("👉 ENTER URL:", value="https://github.com")
display_name = st.text_input("👤 ENTER YOUR NAME:", value="Appala Srinivas Tanakala")
display_title = st.text_input("💼 ENTER YOUR TITLE:", value="Data Scientist & AI / Fintech Leader")

# 2. Dynamic Font Fix: Download a high-quality TrueType font for crystal clear text
font_path = "LiberationSans-Bold.ttf"
if not os.path.exists(font_path):
    url = "https://github.com"
    try:
        urllib.request.urlretrieve(url, font_path)
    except:
        font_path = None  # Fallback to default if download fails

if st.button("Generate QR Code") or target_url:
    if target_url.strip():
        # 3. Configure high-resolution QR matrix
        qr = qrcode.QRCode(
            version=4,  # High grid density for reliable scanning
            error_correction=qrcode.constants.ERROR_CORRECT_M, 
            box_size=14,  # Scaled up for modern crisp smartphone displays
            border=4,
        )
        qr.add_data(target_url.strip())
        qr.make(fit=True)

        # Convert to RGB color canvas
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        qr_width, qr_height = qr_img.size

        # 4. Set up dynamic white canvas buffer space for clear text spacing
        extra_bottom_space = 100
        new_width = qr_width
        new_height = qr_height + extra_bottom_space

        final_img = Image.new("RGB", (new_width, new_height), "white")
        final_img.paste(qr_img, (0, 0))
        draw = ImageDraw.Draw(final_img)

        # 5. Initialize the explicit sharp fonts and crisp sizes
        if font_path:
            name_font = ImageFont.truetype(font_path, 26)  # Bold and readable
            title_font = ImageFont.truetype(font_path, 18)  # Clean secondary text
        else:
            name_font = title_font = ImageFont.load_default()

        # Helper function to auto-center text layers accurately
        def draw_centered_text(text_to_print, y_position, font_style, text_color="black"):
            bbox = draw.textbbox((0, 0), text_to_print, font=font_style)
            text_w = bbox[2] - bbox[0]
            x_position = (new_width - text_w) // 2
            draw.text((x_position, y_position), text_to_print, fill=text_color, font=font_style)

        # 6. Print typography fields on bottom white canvas
        draw_centered_text(display_name.strip(), qr_height + 15, name_font, text_color="black")
        draw_centered_text(display_title.strip(), qr_height + 52, title_font, text_color="#555555")

        # 7. Display the generated image inside your Streamlit Web App page
        st.image(final_img, caption="Preview of your generated card", use_container_width=False, width=400)

        # 8. Convert the PIL image image array into downloadable bytes stream
        img_buffer = io.BytesIO()
        final_img.save(img_buffer, format="PNG")
        byte_data = img_buffer.getvalue()

        # 9. Download button forcing filename explicitly to generated_qr
        st.download_button(
            label="⬇️ Download Production-Ready QR Code",
            data=byte_data,
            file_name="generated_qr.png",
            mime="image/png"
        )
    else:
        st.error("❌ Error: The URL input field cannot be left blank.")
