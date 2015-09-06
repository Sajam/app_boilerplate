Create separated environment for Python packages and install requirements:
```
mkvirtualenv -a /path/to/project project_name
pip install -r requirements.txt
```

Install frontend packages:
```
npm install
```

To rebuild frontend stuff (which is currently JavaScript files with ReactJS + JSX and SASS styles) use `glup` command executed from project's root directory. If you don't have glup installed globally you can do `node_modules/glup/bin/glup.js`.

