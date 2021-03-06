# Setup de desenvolvimento

Se trata da configuração do projeto.
Versão da linguagem, banco de dados, bibliotecas, tudo isso faz parte do ambiente de desenvolvimento.

No linux o python faz parte do sistema operacional e precisamos separar o que é configuração do SO e o que é configuração do projeto. Para isso usamos o pipenv, que cria um **ENV**ironment isolado do sistema operacional. Desta forma você pode configurar o seu projeto sem interferir com o sistema operacional.

Existem outras opções, mas vamos usar o pipenv mesmo. Se você tem o python instalado provavelmente só precisa do comando `pip install pipenv` para instalar.

## Como usar o pipenv

Usando o comando de ajuda tem uma lista de comandos:

```python
$ pipenv --help
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

Por enquanto só queremos criar um ambiente isolado e podemos usar o comando `pipenv --python 3.7` que vai instalar o python na versão 3.7.

Todos os arquivos devem estar dentro da pasta que esse comando for executado.
Nesta pasta qualquer arquivo terminado com .py será um módulo python e podemos colocar o código lá dentro.

## Extenções do vscode que recomendo

- [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)

## Veja o resultado

```bash
git checkout task1/setup
```
