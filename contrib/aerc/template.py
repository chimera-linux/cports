pkgname = "aerc"
pkgver = "0.18.1"
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
sha256 = "f8a2923b1749b1b0eaa9ce221121536d13974297143b597f812b11ebbef0c1bf"
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
