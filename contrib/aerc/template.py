pkgname = "aerc"
pkgver = "0.15.2"
pkgrel = 1
build_style = "makefile"
make_check_target = "tests"
hostmakedepends = [
    "go",
    "scdoc",
]
makedepends = [
    "notmuch-devel",
]
checkdepends = [
    "gnupg",
    "gpgme",
]
pkgdesc = "Pretty Good email client"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~rjarry/aerc"
source = f"https://git.sr.ht/~rjarry/aerc/archive/{pkgver}.tar.gz"
sha256 = "722da196e8807c497f5472704b8a1737d7780ad0faa7166ae83348bc67b144f7"
options = ["!strip"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
