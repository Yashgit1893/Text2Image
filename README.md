# Stable Diffusion Image Generation

Welcome! This guide will help you set up and use the Stable Diffusion model to generate images from text prompts.

## Prerequisites

Ensure you have the following Python packages installed: `diffusers`, `transformers`, `torch`, and `torchvision`. You can install these using pip.

## Usage Guide

1. **Import Required Libraries**: Ensure you import the necessary libraries.
2. **Check for GPU Availability**: The script will check and use a CUDA-enabled GPU if available, or default to CPU.
3. **Define Model and Prompt**: Specify the pre-trained model and the text prompt for the image you want to generate.
4. **Load the Pipeline**: Load the model pipeline and move it to the GPU for faster processing.
5. **Generate the Image**: Create an image based on your text prompt.
6. **Save the Image**: The generated image will be saved to your local disk.
7. **Display the Image**: If using a supported environment (e.g., Jupyter Notebooks), the script will display the image.

## Notes

- Ensure you have a compatible GPU and the necessary CUDA drivers installed.
- Modify the text prompt to generate different images.
- The generated image will be saved in the directory given in the code.

## Dataset Curation

We faced a challenge in finding high-quality datasets specifically for educational topics in the K-12 segment. To bridge this gap, we started building our own dataset, which consisted of text-image pairs specifically designed to support educational applications. 

The dataset was built by sourcing diverse images from the web, ensuring a wide range of relevant and visually engaging content. Using OpenAI's GPT-4o API, we generated three distinct text descriptions for each image: beginner, intermediate, and advanced. These multi-tiered descriptions provide flexibility for various educational contexts and learner proficiencies. Catering to the diverse cognitive levels of K-12 students, the dataset is particularly versatile for STEAM education.

In total, we built a dataset of 1,000 unique text-image pairs, resulting in 3,000 textual descriptions. Each description serves as a standalone input for text-to-image generation models, enabling the production of accurate and visually aligned educational images.

# Stable Diffusion XL Image Generation

Welcome! This guide will help you set up and use the Stable Diffusion XL model to generate images from text prompts.

## Prerequisites

Ensure you have the following Python packages installed: `diffusers`, `transformers`, `torch`, and `torchvision`. You can install these using pip.

## Usage Guide

1. **Import Required Libraries**: Ensure you import the necessary libraries.
2. **Check for GPU Availability**: The script will check and use a CUDA-enabled GPU if available, or default to CPU.
3. **Define Model and Prompt**: Specify the pre-trained model and the text prompt for the image you want to generate.
4. **Load the Pipeline**: Load the model pipeline and move it to the GPU for faster processing.
5. **Generate the Image**: Create an image based on your text prompt.
6. **Save the Image**: The generated image will be saved to your local disk.
7. **Display the Image**: If using a supported environment (e.g., Jupyter Notebooks), the script will display the image.
