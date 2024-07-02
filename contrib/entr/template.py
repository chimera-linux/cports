pkgname = "entr"
pkgver = "5.6"
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
sha256 = "0222b8df928d3b5a3b5194d63e7de098533e04190d9d9a154b926c6c1f9dd14e"
hardening = ["vis", "cfi"]
# need `vim'
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
