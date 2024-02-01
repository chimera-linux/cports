pkgname = "aerc"
pkgver = "0.17.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "tests"
hostmakedepends = [
    "gmake",
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
sha256 = "a8a1af36b4d4989afd670601d83fc2088e14d804c66bd1e3bdd14561bd89c2cc"
tool_flags = {"GOFLAGS": ["-tags=notmuch", "-buildmode=pie"]}
# ppc64le objcopy
options = ["!debug"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
