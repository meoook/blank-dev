# Robot

**_Trade robot_**

* web site: [not-done-yet.ru][prod]
* version: 0.0.1
* author: [meok][author]
* build: django, drf

## Functions

- [ ] Fn

## Install

**Docker** 19.03.12 or higher

```sh
$ apt-get install -y docker
$ docker --version
Docker version 19.03.8, build afacb8b7f0
```

**Docker-Compose** 1.26.2 or higher

```sh
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose --version
docker-compose version 1.26.2, build 1110ad01
```

> For alpine, the following dependency packages are needed:
> `py-pip`, `python-dev`, `libffi-dev`, `openssl-dev`, `gcc`, `libc-dev`, and `make?`.

## Build and run

```sh
$ docker-compose up -d --build
```

or

```sh
$ sh ./runner.sh 5
```

## Release notes

[Release notes][log]


[prod]: <https://404.com> "MS system"
[log]: <CHANGELOG.md> "Release notes"
[author]: <https://bazha.ru> "meok home page"