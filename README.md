
# Document Summarizer

This project is a Document Summarizer built with Python and Streamlit, powered by Azure OpenAI. It allows you to upload `.txt`, `.pdf`, and `.docx` files and generates concise summaries using advanced AI models.

## Setup Instructions

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd Document-Summarizer
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

If you are on a corporate network or behind a proxy/firewall, use the `--trusted-host` option to avoid SSL errors:

```sh
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

If you are behind a proxy, set your proxy before installing:

**Command Prompt:**
```sh
set HTTPS_PROXY=http://your-proxy-address:port
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

**PowerShell:**
```sh
$env:HTTPS_PROXY="http://your-proxy-address:port"
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### 4. Run the Streamlit app

```sh
streamlit run src/app.py
```

## Features

- Upload `.txt`, `.pdf`, or `.docx` documents
- Summarize content using Azure OpenAI
- Simple web interface with Streamlit

## Notes

- Make sure to set up your `.env` file with your Azure OpenAI credentials.
- If you encounter SSL or connection errors, check your proxy/firewall settings and use the trusted host options as shown above.