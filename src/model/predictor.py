# -*- coding: utf-8 -*-
# @Author: hugodms
# @Date:   2025-06-04 12:19:16
# @Last Modified by:   hugodms
# @Last Modified time: 2025-06-04 15:16:11

from transformers import DetrImageProcessor, DetrForObjectDetection
from src.utils.load_image import load_image
import torch


class TableDetector:
    def __init__(self, model_name="TahaDouaji/detr-doc-table-detection", threshold=0.9):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name).to(self.device)
        self.threshold = threshold

    def predict(self, image_path):
        image = load_image(image_path)
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)

        target_sizes = torch.tensor([image.size[::-1]]).to(self.device)
        results = self.processor.post_process_object_detection(
            outputs, target_sizes=target_sizes, threshold=self.threshold
        )[0]

        tables = []
        for score, label, box in zip(
            results["scores"], results["labels"], results["boxes"]
        ):
            if self.model.config.id2label[label.item()] == "table":
                tables.append(
                    {
                        "score": round(score.item(), 3),
                        "box": [round(i, 2) for i in box.tolist()],
                    }
                )

        return {"image_path": image_path, "tables": tables, "num_tables": len(tables)}
