pkgname = "aerc"
pkgver = "0.21.0"
pkgrel = 2
build_style = "makefile"
make_build_args = ["LIBEXECDIR=/usr/lib/aerc"]
make_install_args = [*make_build_args]
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
pkgdesc = "Terminal email client"
license = "MIT"
url = "https://sr.ht/~rjarry/aerc"
source = f"https://git.sr.ht/~rjarry/aerc/archive/{pkgver}.tar.gz"
sha256 = "3f1469bbaea982fc58352f2682932ecc2fb50c705994d96b2343e771747745a7"
tool_flags = {"GOFLAGS": ["-tags=notmuch", "-buildmode=pie"]}


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
