pkgname = "yadm"
pkgver = "3.4.0"
pkgrel = 0
depends = ["bash", "git"]
pkgdesc = "Yet Another Dotfiles Manager"
maintainer = "hge <h.gersen@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/TheLocehiliosan/yadm"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "fb0ab375cc41a34e014fb4a34c65f12670aedc859823b943f626adff24bde95d"


def install(self):
    self.install_bin("yadm")
    self.install_man("yadm.1")
    with self.pushd("completion"):
        self.install_completion("bash/yadm", "bash")
        self.install_completion("zsh/_yadm", "zsh")
        self.install_completion("fish/yadm.fish", "fish")
