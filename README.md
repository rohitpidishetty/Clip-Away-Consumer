# Clip-Away-Consumer

![Python](https://img.shields.io/badge/python-3.10-blue)
![AWS EC2](https://img.shields.io/badge/aws-ec2-orange)
![MessageNX](https://img.shields.io/badge/messagenx-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**Clip Away** is an AI-powered background removal tool that automates image cutouts using the **rembg** library with the **U2NetP** deep learning model. It’s hosted on **AWS EC2** and integrates with **MessageNX**, a lightweight producer-consumer messaging library, to handle image processing tasks asynchronously.

---

## Features

- Real-time background removal with high accuracy  
- Hosted on **AWS EC2** for scalable cloud processing  
- Asynchronous image processing using **MessageNX**  
- Supports batch image processing  
- Lightweight and easy to integrate into Python applications  

---

## How It Works

1. **Message Queue Integration**  
   - **MessageNX** handles communication between clients and the Clip Away service.  
   - Producers send image processing requests (messages) to a channel.  
   - The EC2-hosted Clip Away service acts as a consumer, fetching and processing these messages asynchronously.  

2. **Background Removal with rembg & U2NetP**  
   - **rembg** is a Python library for automated background removal.  
   - **U2NetP**, a compact version of U2Net, predicts a high-resolution alpha matte of the foreground object for precise cutouts.  
   - The model efficiently preserves details around edges while removing backgrounds.  

3. **Processing Flow**  
   - User uploads an image and sends it as a message to a **MessageNX** channel.  
   - The EC2 instance receives the message and processes the image using **rembg + U2NetP**.  
   - The processed image is returned or stored.  
   - Fully asynchronous, allowing multiple images to be handled concurrently.  

---

