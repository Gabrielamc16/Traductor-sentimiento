import streamlet as st
from text blob import TextBlob
from Google Transimport Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimientos con TextBlob')

# Función para reproducir sonidos
def play_sound(sound_file):
    audio_file = open(sound_file, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# Subtítulo y descripción en la barra lateral
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Expander para analizar polaridad y subjetividad
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Traducir texto de español a inglés para análisis
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Calcular polaridad y subjetividad
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        
        # Mostrar resultados
        st.write('Polaridad: ', polarity)
        st.write('Subjetividad: ', subjectivity)

        # Determinar el sentimiento y reproducir sonido adecuado
        if polarity >= 0.5:
            sentimiento = 'positivo 😊'
            st.write(f'Es un sentimiento {sentimiento}')
            play_sound('Hotsound.mp3')
        elif polarity <= -0.5:
            sentimiento = 'negativo 😔'
            st.write(f'Es un sentimiento {sentimiento}')
            play_sound('Coldsound.mp3')
        else:
            sentimiento = 'neutral 😐'
            st.write(f'Es un sentimiento {sentimiento}')
            play_sound('Mediumsound.mp3')

# Expander para corrección de texto en inglés
with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('Texto corregido: ', blob2.correct())
