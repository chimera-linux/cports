pkgname = "entr"
pkgver = "5.9"
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
license = "ISC"
url = "https://eradman.com/entrproject"
source = f"{url}/code/entr-{pkgver}.tar.gz"
sha256 = "0ef2ce7db728167844a91904944cd07c7ccc6fd3041b849cad861224d106a845"
hardening = ["vis", "cfi"]
# ./system_test.sh: line 515: kill: (419) - No such process
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
