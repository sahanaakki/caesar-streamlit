
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Caesar Cipher Tool",
    page_icon="🔐",
    layout="centered"
)


# Caesar Cipher algorithm
def caesar_cipher(text, shift, operation):
    result = ""

    # Reverse the shift when decrypting
    if operation == "Decrypt":
        shift = -shift

    for char in text:

        # Handle uppercase letters
        if "A" <= char <= "Z":
            base = ord("A")
            new_char = chr(
                (ord(char) - base + shift) % 26 + base
            )
            result += new_char

        # Handle lowercase letters
        elif "a" <= char <= "z":
            base = ord("a")
            new_char = chr(
                (ord(char) - base + shift) % 26 + base
            )
            result += new_char

        # Keep spaces, numbers and punctuation unchanged
        else:
            result += char

    return result


# GUI
st.title("🔐 Caesar Cipher Tool")

st.write(
    "Encrypt and decrypt text using the classical "
    "Caesar Cipher algorithm."
)

st.info(
    "Educational project: Caesar Cipher is not suitable "
    "for protecting real passwords or sensitive information."
)

message = st.text_area(
    "Enter your message",
    placeholder="Example: HELLO WORLD",
    height=150
)

shift = st.slider(
    "Choose the shift key",
    min_value=0,
    max_value=25,
    value=3
)

operation = st.radio(
    "Select an operation",
    ["Encrypt", "Decrypt"],
    horizontal=True
)

if st.button("Run Algorithm", type="primary"):

    if not message:
        st.warning("Please enter a message first.")

    else:
        result = caesar_cipher(
            message,
            shift,
            operation
        )

        st.subheader("Result")

        st.code(result, language=None)

        st.success(
            f"{operation} completed successfully!"
        )
