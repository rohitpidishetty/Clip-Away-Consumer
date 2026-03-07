from django.core.management.base import BaseCommand
from com.mnx.MessageNX import MessageNX
import base64
from decouple import config

from rembg import remove
from PIL import Image
from datetime import datetime
import io
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore


class Command(BaseCommand):
    help = "Run a continuous MessageNX consumer"

    # firebase_dict = json.loads(config("SECRET"))
    # cred = credentials.Certificate("./key.json")

    firebase_dict = json.loads(config("SECRET"))
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)

    def handle(self, *args, **kwargs):
        db = firestore.client()
        mnx = MessageNX()
        mnx.set_channel(config("APP_CHANNEL"))
        mnx.set_threshold(2)

        def processor(job_data):
            print("Received job:", job_data.get("user"))


            input_data = base64.b64decode(job_data.get("image_base64"))

            output_data = remove(input_data)
            # output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")
            # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # output_path = os.path.join("test", f"{2}_{timestamp}.png")
            # output_image.save(output_path, format="PNG")
            img_base64 = base64.b64encode(output_data).decode("utf-8")
            photo_data = {
                "email": job_data.get("user"),
                "url": img_base64,
                "uploaded_at": job_data.get("timestamp"),
                "date": job_data.get("date"),
                "time": job_data.get("time"),
                "id": job_data.get("id"),
            }
            photos_collection_ref = (
                db.collection("users").document(job_data.get("user")).collection("photos")
            )
            doc_ref = photos_collection_ref.add(photo_data)

        mnx.consume(process_callback=processor)
