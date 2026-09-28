pkgname = "yadm"
pkgver = "3.5.0"
pkgrel = 0
depends = ["bash", "git"]
pkgdesc = "Yet Another Dotfiles Manager"
license = "GPL-3.0-only"
url = "https://github.com/TheLocehiliosan/yadm"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "2a15ed91238dd2f15db9905eb56702272c079ad9c37c505dfee69c6b5e9054b6"


def install(self):
    self.install_bin("yadm")
    self.install_man("yadm.1")
    with self.pushd("completion"):
        self.install_completion("bash/yadm", "bash")
        self.install_completion("zsh/_yadm", "zsh")
        self.install_completion("fish/yadm.fish", "fish")
