# Franklin_Flash
This repository is my submission for the 2025 boot.dev hackathon. It is my first personal project,named in honor of my favorite tan and white chihuaha in a red vest, Franklin (**AKA FRANK THE TANK**).

![Majestic Franklin](images/Franklin%201.jpeg)

## Requirements
Its just regular python, make sure you at least have 3.10 or later. 
While most versions of Python include the Tkinter package, some systems do not include it originally(aka Mine). You may need to install Tkinter package seperately like I did. If you have the apt package manager like I do, it is simply the code below in your system terminal. 

`sudo apt install python3-tk`

Otherwise this was the rest of the software I had on my machine for this project:  
-Python 3.10+
-[uv](https://docs.astral.sh/uv/) package manager

### Instructions
1. Clone the repository:
```bash
git clone https://github.com/ClydesdaleCoder/Franklin_Flash.git
```

2. Install uv if you have not already:
 On macOS and Linux:
`curl -LsSf https://astral.sh/uv/install.sh | sh`

On Windows:
`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

3. Run the app: 
` uv run main.py`
**NOTE**:  Please use uv run rather than python3 directly to ensure consistent font rendering and dependency management

If you want to modify the flashcards for your own study purposes modify the list in flashcards.py. Each card is a dictionary with two key value pairs, one for the question and one for the answer. Example below. 

`{"question": "What is 2 + 2?", "answer": "4"}`

I included some base example questions but feel free to add your own!

I have instructions to use the app within it. 

#### Background

This is my first app I have ever designed myself fully. I wanted to make something to help with future studies and figured this was a great step in that direction. Plus it is a nice little homage to one of my best friends, Franklin. 

![Big Snoot](images/Franklin%203.jpeg) 
