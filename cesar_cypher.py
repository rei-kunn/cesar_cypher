import streamlit as st

FIRST_CHAR_CODE = ord("a")
LAST_CHAR_CODE = ord("z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):
    result = ""
    for char in message.lower():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result

st.title("Caesar Cipher Encryption")

ct = st.container(border=True)
user_message = ct.text_input("Message to Encrypt: ")
user_shift_key = ct.slider("Pick a number", 0 , 15)

encrypt_msg = ""
decrypt_msg = ""

if st.button("Encrypt!"):
    encrypt_msg=caesar_shift(user_message, user_shift_key)
    st.session_state['encrypted_msg'] = encrypt_msg

if st.button("Decrypt back!"):
    if 'encrypted_msg' in st.session_state:
        encrypt_msg = st.session_state['encrypted_msg']
        decrypt_msg=caesar_shift(encrypt_msg, -user_shift_key)
    else:
        st.write("Please encrypt first!")

st.write("Encrypted Message:", encrypt_msg)
st.write("Decrypted Message:", decrypt_msg)


st.markdown('''Created by: :blue-background[Agga (Rei) :computer:]''')