pkgname = "yadm"
pkgver = "3.2.2"
pkgrel = 0
depends = ["bash", "git"]
pkgdesc = "Yet Another Dotfiles Manager"
maintainer = "hge <h.gersen@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/TheLocehiliosan/yadm"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c5fb508748995ce4c08a21d8bcda686ad680116ccf00a5318bbccf147f4c33ad"


def install(self):
    self.install_bin("yadm")
    self.install_man("yadm.1")
    with self.pushd("completion"):
        self.install_completion("bash/yadm", "bash")
        self.install_completion("zsh/_yadm", "zsh")
        self.install_completion("fish/yadm.fish", "fish")
