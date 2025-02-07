pkgname = "entr"
pkgver = "5.7"
pkgrel = 0
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
sha256 = "90c5d943820c70cef37eb41a382a6ea4f5dd7fd95efef13b2b5520d320f5d067"
hardening = ["vis", "cfi"]
# ./system_test.sh: line 515: kill: (419) - No such process
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
