<https://sandbox.zenodo.org/badge/485892833.svg>

# circulant-weighing-matrices
Data on circulant weighing matrices from the La Jolla Combinatorics Repository

This repository holds the source of a Jupyter Book containing 
information on circulant weighing matrices CW(n,k) for
n<1000 and k < 400$.  It is a version of data available at
<https://dmgordon.org/cwm/>.

## Building the Book ##

1. Pull the book repository
   ```bash
   git clone https://github.com/<TBD>

   cd cwm
   ```
2. Install [*Jupyter Book*][jb-pypi] (`requirements.txt`)
   ```bash
   pip install -r requirements.txt
   ```
3. Build the book
   ```bash
   jb build .
   ```
4. Open the html build
   ```bash
   open _build/html/index.html
   ```
   or run it as a server (to get the embedded Jupyter Notebook to work)
   ```bash
   python -m http.server --directory _build/html
   open http://localhost:8000
   ```


