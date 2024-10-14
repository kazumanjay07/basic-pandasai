# Data Query and Analysis Apps

This repository contains two Streamlit-based applications that allow users to query datasets using natural language and visualize data interactively with the help of `PandasAI`.

## App Descriptions

### 1. `app.py` - Supermarket Sales Data Query App
This app provides an interface to ask questions about a supermarket sales dataset and returns insights based on user prompts.

#### Features:
- **Data Source**: `supermarket_sales - Sheet1.csv` (must be placed in the same directory).
- Displays the sales data and allows users to interact with it.
- Allows users to ask questions about the data using natural language.
- Uses `PandasAI` with a language model to process queries.
- Can generate charts and display results directly in the Streamlit app.

#### How to Use:
1. Clone the repository.
2. Place the `supermarket_sales - Sheet1.csv` file in the root directory.
3. Set up the `PANDASAI_API_KEY` with your valid API key.
4. Install the required dependencies (see `requirements.txt`).
5. Run the app with:
   ```bash
   streamlit run app.py
