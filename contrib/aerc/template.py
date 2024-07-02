pkgname = "aerc"
pkgver = "0.18.0"
pkgrel = 1
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
sha256 = "d20382d7eb6a93b8b6fe508b87c83eb1bb600a0443f173ab1edef0e81ea9f66a"
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
