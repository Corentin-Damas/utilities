import os
from pathlib import Path
import json

ARCHI = {
    "abstracts": ["_functions.scss", "_mixins.scss", "_variables.scss"],
    "base": ["_animations.scss", "_base.scss", "_typography.scss", "_utilities.scss"],
    "components": ["_button.scss"],
    "layout": ["_header.scss", "_navigation.scss", "_footer.scss"],
    "pages": ["_home.scss"]
}

MAIN_IMPORTS = [
    '@import "abstracts/functions";',
    '@import "abstracts/mixins";',
    '@import "abstracts/variables";',
    '@import "base/animations";',
    '@import "base/base";',
    '@import "base/typography";',
    '@import "base/utilities";',
    '@import "components/button";',
    '@import "layout/header";',
    '@import "layout/navigation";',
    '@import "layout/footer";',
    '@import "pages/home";'
]

personalScript = {
    "watch:sass": "node-sass sass/main.scss css/style.css -w",
    "devserver": "live-server",
    "start": "npm-run-all --parallel devserver watch:sass",
    "compile:sass": "node-sass sass/main.scss css/style.comp.css",
    "prefix:css": "postcss --use autoprefixer -b 'last 10 versions'  css/style.comp.css -o  css/style.prefix.css",
    "compress:css": "node-sass css/style.prefix.css css/style.css --output-style compressed",
    "build:css": "npm-run-all compile:sass concat:css prefix:css compress:css"
}

# Function that create all the architecture for the sass file


def createfiles():
    os.chdir(path)
    sassPath = os.getcwd()

    # Create the main file first as a txt filt to be able to write in, then is converted in .scss
    with open('main.txt', 'w') as file:
        for line in MAIN_IMPORTS:
            file.write(line + "\n")
    os.rename("main.txt", "main.scss")

    # Create the architecture from the object Archi writen earlier
    for dir in ARCHI:
        fileArr = ARCHI[dir]
        tempPath = Path(f"{sassPath}/{dir}")
        os.makedirs(tempPath)
        os.chdir(tempPath)
        tempSubDir = os.getcwd()

        for file in fileArr:
            open(f'{tempSubDir}/{file}', "a").close

# === Start of the Script ===


parentDir = os.getcwd()

# Create the intex.html && CSS folder with style.css
open(f'{parentDir}\index.html', "a").close

directoryCss = "css"
pathCSS = os.path.join(parentDir, directoryCss)
os.mkdir(pathCSS)
os.chdir(pathCSS)
open(f'{pathCSS}\style.css', "a").close

# Goes back to current workin dir
os.chdir(parentDir)

# Create the sass folder
directory = "sass"
path = os.path.join(parentDir, directory)


os.mkdir(path)
print(f"Directory {directory} created \n")
createfiles()
os.chdir(parentDir)

# === NPM Package install
os.system('npm init')

os.system('npm install node-sass')

#  Check if npm init went well, Re write the package.jsoin to fit better our need
if (Path(f'{parentDir}\package.json')):
    with open('package.json', "r") as jsonFile:
        data = json.load(jsonFile)

    data["scripts"] = personalScript

    with open('package.json', "w") as jsonFile:
        data = json.dump(data, jsonFile)
    print("You should run \n - npm i npm-run-all --save-dev \n - npm i autoprefixer --save-dev \n  - npm i postcss --save-dev")
else:
    print('JsonPackage not found, try on the terminal: \n - npm init \n - npm i node-sass --save-dev')


# Create git ignore

with open('.gitignore.txt', 'w') as f:
    f.write('.env\nnode_modules')
os.rename('.gitignore.txt', '.gitignore')
