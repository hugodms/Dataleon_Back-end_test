import argparse
import os
from src.model.predictor import TableDetector
from PIL import UnidentifiedImageError


def main():
    parser = argparse.ArgumentParser(
        description="Détecter les tableaux dans une image de document."
    )
    parser.add_argument(
        "filename", type=str, help="Nom du fichier image dans le dossier 'assets/'"
    )
    args = parser.parse_args()

    image_path = os.path.join("assets", args.filename)

    try:
        detector = TableDetector()
        result = detector.predict(image_path)

        print(f"Results for : {args.filename}")
        print(f"Detected Tables : {result['num_tables']}")
        for i in range(len(result["tables"])):
            table = result["tables"][i]
            print(f"\tTable {i}:")
            print(f"\t- Score : {table['score']}")
            print(f"\t- Box   : {table['box']}")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
