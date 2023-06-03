
import openai
import pdfplumber

openai.api_key = "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"

with pdfplumber.open("Clean Freaks Resume (1).pdf") as pdf:
    first_page = pdf.pages[0]
    resume = first_page.extract_text().encode("UTF-8").rstrip()

messages = []

introPrompt = f"Pretend you are a Google recruiter and provide constructive criticism to the following resume: {resume}"
messages.append(introPrompt)

response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": f"{messages}"}],
            temperature=0.8,
            frequency_penalty=0,
            presence_penalty=0.6,
        )

print(response['choices'][0]['message']['content'])