from openai import OpenAI

def translate(transcription_path,translation_path,my_api_key):
  client = OpenAI(api_key=my_api_key)
  with open(transcription_path,'r') as fp:
    transcription = fp.read()
  paragraphs = transcription.split('\n\n')
  translated_paragraphs = []
  system_message = "Each message I send you will be an excerpt from a math paper which is written in French and formatted in latex code.\n  Please translate each excerpt into English.\n  Your response should be in the form of LaTeX code.\n Your response should preserve all LaTeX formatting as much as possible (for example, italicized text should remain italicized, and footnotes should remain as footnotes).\n Do not modify any mathematical equations.  All equations must be identical to those appearing in the original text."
  for i in range(len(paragraphs)):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role":"system", "content": system_message},
        {"role":"user", "content": paragraphs[i]}
      ]
    )
    translated_paragraphs.append(completion.choices[0].message.content)
    time.sleep(20) # for free tier, to comply with rate limit
  translation='\n\n'.join(translated_paragraphs)
  with open(translation_path,'w') as fp:
    fp.write(translation)
