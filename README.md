# 📄 Table Detection with Transformers ![CI](https://github.com/hugodms/Dataleon_Back-end_test/actions/workflows/ci.yml/badge.svg?branch=main)


> A Python project using Hugging Face’s DETR transformer to detect tables in invoice and bank document images.

---

## 🚀 Description

This project uses a pre-trained model from [Hugging Face](https://huggingface.co/TahaDouaji/detr-doc-table-detection) to detect tables in scanned documents such as invoices or bank statements.

It loads images, runs inference, and extracts bounding boxes for detected tables. You can test it via the command line or extend it with an API or UI.

---

## 📂 Project Structure

```
.
├── assets/
├── src/
│   ├── model/
│   │   └── predictor.py
│   └── utils/
│       └── load_image.py
├── tests/
│   ├── test_main.py
│   ├── test_load_image.py
│   └── test_predictor.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Model Used

- 🔗 Model: TahaDouaji/detr-doc-table-detection
- 📦 Framework: transformers, torch, Pillow

---

## 🛠️ Installation
```bash
git clone https://github.com/votre-utilisateur/mon-projet-table-detector.git
cd mon-projet-table-detector
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🖼️ Usage

Place your image file in the assets/ folder and run:

```bash
python main.py my_invoice.png
```

### ✅ Example Output:

```
Results for : bank_document.png
Detected Tables : 1
	Table 0:
	- Score : 0.91
	- Box   : [40.33, 603.64, 999.71, 922.83]
```
---

## ✅ Supported Formats

- .png  
- .jpg  
- .jpeg

---

## 🧪 Running Tests

To run unit tests using pytest:
```bash
pytest tests/
```
You can also run specific test files:
```bash
pytest tests/test_predictor.py  
pytest tests/test_load_image.py  
pytest tests/test_main.py
```

---

## ❌ Error Handling

The following errors are explicitly handled:

- ❗ Unsupported file format  
- 📂 File not found  
- 🖼️ Invalid or unreadable image  
- 🔒 Permission errors  
- ⚠️ Unexpected runtime errors

Each error is logged clearly for easier debugging.

---

## 🔁 Continuous Integration (CI)

This project uses **GitHub Actions** to automate code analysis and testing on every push or pull request to the `main` branch.

The CI workflow automatically performs the following checks:

- ✅ **Code formatting validation** using [Black](https://black.readthedocs.io/en/stable/)  
- 🔒 **Security analysis** with [Bandit](https://bandit.readthedocs.io/en/latest/)  
- 🧪 **Unit testing** with [pytest](https://docs.pytest.org/)

The workflow configuration file is located at:
```
.github/workflows/ci.yml
```

> ⚠️ The workflow will fail if the code is not properly formatted (Black) or if security issues are detected (Bandit). Pushes and pull requests must pass all checks to be accepted.

## 🚀 Run Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Check code formatting
black --check .

# Run security checks (excluding dependencies and tests)
bandit -r . -x tests,venv,env,.venv
```
