pkgname = "entr"
pkgver = "5.4"
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
sha256 = "491dded2cc3f1dcd8d26f496a4c7b3a996b91c7ab20883ca375037a398221f9e"
hardening = ["vis", "cfi"]
# need `vim'
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
