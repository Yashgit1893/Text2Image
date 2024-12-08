import os
from openai import OpenAI
import requests
import PIL
from PIL import Image
from io import BytesIO

# Initialize OpenAI client with your API key
client = OpenAI(api_key='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')
def generate_text_from_images(image_urls, start_number, text_folder_path, image_folder_path):
    # Create directories if they don't exist
    if not os.path.exists(text_folder_path):
        os.makedirs(text_folder_path)
    if not os.path.exists(image_folder_path):
        os.makedirs(image_folder_path)
    
    for index, image_url in enumerate(image_urls):
        image_number = start_number * 10 + index + 1

        print(f"Processing Image URL: {image_url}")  # Add this line to identify which URL is being processed

        try:
            # Fetch and save the image
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image_file_path = os.path.join(image_folder_path, f"{image_number}.png")
            image.save(image_file_path)
            print(f"Saved Image: {image_number}.png")
        except PIL.UnidentifiedImageError as e:
            print(f"Error processing {image_url}: {str(e)}")
            continue

        # Generate text explanations
        api_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": """You are a teacher tasked with explaining a concept using an image provided. The images will be related to Resonance in Waves. You will create three different explanations corresponding to different levels of student understanding:

                        Low-Level Explanation: Provide a simple and straightforward explanation. Use basic language and avoid complex terminology. Assume the student is just beginning to learn the topic and needs a gentle introduction.

                        Intermediate-Level Explanation: Give a more detailed explanation. Use moderately advanced terminology and concepts, assuming the student has some prior knowledge of the topic but still needs guidance and clarification.

                        High-Level Explanation: Provide an in-depth and detailed explanation. Use advanced terminology and concepts. Assume the student is already familiar with the basics and is ready to explore the topic in greater depth, with an emphasis on understanding underlying principles and connections to other concepts.

                        Format the response as:
                        (Explanation 1 here)

                        (Explanation 2 here)

                        (Explanation 3 here)
                         
                        Ensure each of the explanations only has 1 paragraph, and no headings. Only the three explanations.
                        """},
                        
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=500,
        )

        explanations = api_response.choices[0].message.content.split("\n\n")
        # print(explanations)
        # Save each explanation as a separate file without the "Explanation X:" headers
        # for i, explanation in enumerate(explanations):
        #     # Remove "Explanation X:" headers
        #     explanation_content = explanation.split("", 1)[1].strip() if ":" in explanation else explanation.strip()
            
        #     filename = f"{image_number}{chr(97 + i)}.txt"  # 97 is the ASCII code for 'a'
        #     file_path = os.path.join(text_folder_path, filename)
            
        #     # print(explanation_content)
            
        #     with open(file_path, "w", encoding="utf-8") as file:
        #         file.write(explanation_content)
        #         print(f"Saved Text: {filename}")

        for i, explanation in enumerate(explanations):
            explanation_content = explanation.strip()  # Remove any leading/trailing spaces

            filename = f"{image_number}{chr(97 + i)}.txt"  # 97 is the ASCII code for 'a', 'b', 'c', etc.
            file_path = os.path.join(text_folder_path, filename)
            
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(explanation_content)
                print(f"Saved Text: {filename}")

# Usage
image_urls = [
    "https://d10lpgp6xz60nq.cloudfront.net/physics_images/NVT_21_PHY_XII_C05_E08_005_S01.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYHaYsyVloKmsM777vDJR7IjjhnAnQGKYjGgkQgk3e6WPcmjYKCEWjxX6gIxuW8bFC8_o&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs0toqh83K4hwbRRmMDGl32rjDmVQfrNLamodaJls46EfUtFzdiGTwdltJzekyazbjcRY&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrjdovvNVOo78SWlVdljHhdV4Lkw_xv3NNvtaoZBOsqrzI8u3HWWGhRh4e0XWQlT3aFI8&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk0yDvmK0kuUQqk2M-VqxYswbidCSWTpE3_zBmxTKBqbLCQlNWGnh3lCdPPvDHmDloYiI&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQitqHFEqIjmd7jIF1At_tmGO-Ll1skN-W5kOvCmnc2Eit0Ncavd_30JYi6dgTp79nIPhg&usqp=CAU",
    "https://d20x1nptavktw0.cloudfront.net/wordpress_media/2023/08/what-is-resonant-frequency-.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYVk3BzeElef0S4on7UzpTcitztFvpuVvs1tDbdHADkeEFWYhexH45wpymKFPzuJJ3GY8&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0Yew6no5BOJKn6OAvbJVVKtMwYWKEvtKPaxY08mIOKKyrh0lplxyLopmEy20Fzi-6LgI&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRluH7aCEdsnCy3gbVhagmyTh34bI-0Oj8k4RHEG9patpkjY8O_EcmVckxTIjPcsoH-cjE&usqp=CAU"
]

# Starting number (e.g., 5)
start_number = 79

# Folder paths to save the text files and images
text_folder_path = "E:\Description"
image_folder_path = "E:\Images"

generate_text_from_images(image_urls, start_number, text_folder_path, image_folder_path)