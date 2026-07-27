import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

image_path = "../datasets/images/vietnam.png"

client = OpenAI()

with open(image_path, 'rb') as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    prompt = (
        "You are an assistant for visually impaired users."
        "Describe the image in detail."
    )

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": prompt
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
        max_completion_tokens=700,
        reasoning_effort = "low",
    )

    # The initial value of max_completion_tokens was low. 
    # Printing out the finish reason provided an indication behind why the model did not spit out content
    #print(response.choices[0].finish_reason) 
    #print(response.usage)

    content = response.choices[0].message.content
    print(content)