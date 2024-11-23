pkgname = "yadm"
pkgver = "3.3.0"
pkgrel = 0
depends = ["bash", "git"]
pkgdesc = "Yet Another Dotfiles Manager"
maintainer = "hge <h.gersen@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/TheLocehiliosan/yadm"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a977836ee874fece3d69b5a8f7436e6ce4e6bf8d2520f8517c128281cc6b101d"


def install(self):
    self.install_bin("yadm")
    self.install_man("yadm.1")
    with self.pushd("completion"):
        self.install_completion("bash/yadm", "bash")
        self.install_completion("zsh/_yadm", "zsh")
        self.install_completion("fish/yadm.fish", "fish")
