pkgname = "diff-so-fancy"
pkgver = "1.4.4"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Improved diff colorizer"
license = "MIT"
url = "https://github.com/so-fancy/diff-so-fancy"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3eac2cfb3b1de9d14b6a712941985d6b240b7f3726c94a5e337317c7161e869d"


def install(self):
    self.install_files("lib/DiffHighlight.pm", "usr/share/diff-so-fancy")
    self.install_bin("diff-so-fancy")
    self.install_license("LICENSE")
