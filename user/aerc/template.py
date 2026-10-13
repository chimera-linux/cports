pkgname = "aerc"
pkgver = "0.22.0"
pkgrel = 0
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
sha256 = "f1cd5e358fd836051d4d88c189ecaa025a108b729281985525b45b13bc49e70f"
tool_flags = {"GOFLAGS": ["-tags=notmuch", "-buildmode=pie"]}


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
