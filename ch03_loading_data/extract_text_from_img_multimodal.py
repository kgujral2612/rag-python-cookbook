import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

png_file_apth = "../datasets/images/example_finance_reporting_slide.png"

client = OpenAI()

with open(png_file_apth, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    prompt = (
        "Extract the text from the image attached. Make sure to only"
        "extract the text. If there is no text in the image, "
        "please retur with the sentence 'No text found in the image'."
    )

    response = client.chat.completions.create(
        model = "gpt-5.2",
        messages= [
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url":  {
                        "url" : (
                            f"data:image/jpeg;base64,"
                            f"{base64_image}"
                        ),
                    },
                },
            ],
            }
        ],
        max_completion_tokens=500,
    )

    content = response.choices[0].message.content
    print(content)
