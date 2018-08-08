# Contributing Guidelines
## Prerequisites
* python 3.6
* pipenv
* docker
* docker compose

## Fork/Fetch, Develop, and PR
`fork | if you have never forked this repo and cloned your forked copy`
1) Fork this repo to your GitHub account
2) Clone your newly created repo to your computer
3) Set your forked copy as the origin, set this repo as the upstream remote repositories

`fetch | if you previously forked this repo and cloned your forked copy and want latest copy of this repo`
1) Fetch from this repo (upstream)
2) Switch to master
3) Merge upstream/master
If upstream has new commits: rebase master and resolve conflicts, if any

`develop`
1) Create new branch
2) Develop using your favorite editor (I use [PyCharm](https://www.jetbrains.com/pycharm/)) - be sure to [add appropriate .gitignore code](https://github.com/github/gitignore) for your editor
3) Add and commit changes to your development branch
4) Push your development branch to your forked copy on GitHub (origin)

`pull request`
Read GitHub's help document on [Creating a Pull Requet From a Fork](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

## Running Containers
1) cd into folder created when you cloned your forked copy (likely ws-macstucson)
2) build docker containers with:
```bash
docker-compose -f docker-compose-development.yml up --build -d
```

This creates two docker containers: 1 for nginx and 1 for django & gunicorn.
The static files in the nginx container and the templates folder in the django container are mounted as volumes so containers don't have to be rebult when front end code changes.
You will likely have to stop/rebuild containers when making changes to files in other directories (ie: confir/settings/_base.py).
