# Flask SWAPI Demo 🚀

This Flask demo app provides a simple user interface for querying 🌟 [Star Wars API (SWAPI)](https://swapi.dev/). The app allows users to search and retrieve various data related to Star Wars, including characters, `films`, `planets`, `species`, `starships`, and `vehicles`.

## 🌐 Visiting and Using the App
You can visit and use the app at [philipwalsh.pythonanywhere.com](https://philipwalsh.pythonanywhere.com/).

For example, you can retrieve data related to the second Star Wars film, "The Empire Strikes Back", by visiting https://philipwalsh.pythonanywhere.com/swapi/films/2.

The app allows users to search and retrieve various data related to Star Wars, including characters, films, planets, species, starships, and vehicles. To retrieve data for a specific category, simply replace <category> in the URL with the desired category name (e.g., films, people, planets, species, starships, or vehicle).

You can also retrieve data for a specific item within a category by appending its ID to the URL (e.g., `/swapi/films/2` retrieves data for the film with ID 2). Note that not all categories have IDs for all items.

If the requested category or ID does not exist or is invalid, the app will return a "404 Not Found" error.

## 🛠️ Installation and Usage

1. Clone the repository: `git clone https://github.com/username/flask-swapi-demo.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app: `python src/main.py`
4. Open your browser and navigate to `http://localhost:5000/`

## 🌟 Features

- Search and retrieve various data related to Star Wars, including characters, films, planets, species, starships, and vehicles.

## 🤝 Contributing

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a new pull request

## 📁 Project Structure
```
.
├── README.md
└── src
├── main.py
├── static
│ ├── images
│ │ └── favicon.svg
│ └── styles
│ └── main.css
└── templates
└── index.html
```


- `README.md` contains the project documentation.
- `src/main.py` is the Flask application file.
- `src/static/images/favicon.svg` is the favicon for the app.
- `src/static/styles/main.css` is the main stylesheet for the app.
- `src/templates/index.html` is the main HTML template for the app.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

