# Contributing guide
You need `make` and `python` in your `$PATH`

1. Clone repo from `main` branch:
```shell
git clone https://github.com/deknowny/demapi
```
2. Go to cloned repo
```shell
cd demapi
```
3. Install the repo locally with developing dependencies
```shell
make install-dev
```
***
Now you can develop new functional. You can create a `.drafts/` directory for your drafts (added to .gitignore)
***
4. Run tests locally
```shell
make test
```
***
And if you want to suggest new changes:
5. Fork the repository
6. Push your changes to your fork
7. Create a pull request
***
There is also `GitHub` actions setup, and you can see coverage on different python versions and on different platforms.
