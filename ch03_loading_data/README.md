# Loading Data in Python

About 80% of enterprise information is unstructured and distributed across presentations, documents, emails, ad media files.

This project contains the source code to load the following types of files in Python:
1. Microsoft Word
2. PDF
3. Tabular- excel, CSV
4. SQL

Additional scripts that are included have the below functions:
1. Extracting text from audio
2. Extracting text from image using tesseract
3. Extracting text from image using multimodal models

### Getting Started

```bash
# Install required packages
pip install -r requirements.txt

# Install PostGreSQL for loading sql data on macOS
brew install postgresql@16
brew services start postgresql@16
brew install --cask pgadmin4

# To launch postgres inside the shell
psql postgres
```