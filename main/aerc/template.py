pkgname = "aerc"
pkgver = "0.20.0"
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
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://sr.ht/~rjarry/aerc"
source = f"https://git.sr.ht/~rjarry/aerc/archive/{pkgver}.tar.gz"
sha256 = "1a7d6172b5740ead40bf1400cd45f00400822bb6af00aef76d04b386a4292d8c"
tool_flags = {"GOFLAGS": ["-tags=notmuch", "-buildmode=pie"]}


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
