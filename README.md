# Cocemfe Web

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7582c56abb014e41a55545fea23e639f)](https://app.codacy.com/gh/ISPP-Grupo-10/cocemfe-sevilla?utm_source=github.com&utm_medium=referral&utm_content=ISPP-Grupo-10/cocemfe-sevilla&utm_campaign=Badge_Grade)

- [Description](#description)
- [Installation](#installation)
- [Contribution](#contribution)
- [License](#license)
  
## Description
Cocemfe Web is a project developed by 17 software engineering students that aims to improve the efficiency of all municipalities when creating accessibility plans. The software allows the uploading of documents so that, subsequently, a number of qualified people can suggest improvements to the document, thus making the process of editing the plan and proposing improvements much more enjoyable.

## Instalation

### Requirements

- Python >= 3.7

### Pasos

1. Clone the repository:

```bash
git clone https://github.com/tu_usuario/cocemfe-web.git
cd cocemfe-web
```
2. Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r ./cocemfe_sevilla/requirements.txt
pip install importlib_metadata
```
3. Performs database migrations:

```bash
python ./cocemfe_sevilla/manage.py makemigrations
python ./cocemfe_sevilla/manage.py migrate
```
4. Launch the proyect

```bash
python ./cocemfe_sevilla/manage.py runserver
```

## Contribution

We welcome contributions! To contribute to the project, follow these steps:
1. Fork the proyect.
2. Create your feature branch using the format `feature/issueNumber-branch-name`:
```bash
git checkout -b feature/issueNumber-branch-name
```
Por ejemplo:
```bash
git checkout -b feature/123-new-feature
```
3. Make your changes and commit them following the Conventional Commits conventions:
```bash
git commit -m 'feat: add new feature'
```
4. Push to your remote repository:
```bash
git push origin feature/issueNumber-branch-name
```
5. Make a pull request to Develop and wait for it to be accepted :)

## License

This project is licensed under the MIT License. For more information, see the file [LICENSE](./LICENSE).

