pkgname = "entr"
pkgver = "5.6"
pkgrel = 1
build_style = "configure"
make_install_args = ["PREFIX=/usr"]
checkdepends = [
    "bash",
    "file",
    "git",
    "procps",
    "tmux",
    "vim",
]
pkgdesc = "Run arbitrary commands when files change"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://eradman.com/entrproject"
source = f"{url}/code/entr-{pkgver}.tar.gz"
sha256 = "0222b8df928d3b5a3b5194d63e7de098533e04190d9d9a154b926c6c1f9dd14e"
hardening = ["vis", "cfi"]
# check fails:
# "entr: unable to get terminal attributes, use '-n' to run non-interactively"
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
