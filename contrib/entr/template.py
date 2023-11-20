pkgname = "entr"
pkgver = "5.5"
pkgrel = 0
build_style = "configure"
make_install_args = ["PREFIX=/usr"]
checkdepends = [
    "bash",
    "file",
    "git",
    "procps",
    "tmux",
]
pkgdesc = "Run arbitrary commands when files change"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://eradman.com/entrproject"
source = f"https://eradman.com/entrproject/code/entr-{pkgver}.tar.gz"
sha256 = "128c0ce2efea5ae6bd3fd33c3cd31e161eb0c02609d8717ad37e95b41656e526"
hardening = ["vis", "cfi"]
# need `vim'
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
