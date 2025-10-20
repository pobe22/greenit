import asyncio
import edge_tts

# === Text, der gesprochen werden soll ===
text = (
    "Willkommen bei Green IT. "
    "Diese Seite zeigt, wie Technologie und Nachhaltigkeit zusammengehen können. "
    "Jede Zeile Code, jeder Server, jede Entscheidung zählt. "
    "Lasst uns gemeinsam die digitale Welt grüner gestalten."
)

# === Stimme wählen (deutsche Stimme) ===
voice = "de-DE-KatjaNeural"

# === Dateiname für die erzeugte Audio-Datei ===
output_file = "greenit_intro.mp3"

async def main():
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"✅ Audio generiert: {output_file}")

asyncio.run(main())
