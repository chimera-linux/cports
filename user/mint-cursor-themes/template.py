pkgname = "mint-cursor-themes"
pkgver = "1.0.2"
pkgrel = 0
pkgdesc = "Linux Mint mouse cursor themes"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/mint"
source = "https://github.com/linuxmint/mint-cursor-themes/archive/d2c1428b499a347c291dafb13c89699fdbdd4be7.tar.gz"
sha256 = "9bdeff09e37ecdc480bc8ae6256d0f3f105e7bb59c5386de22e1dedc3dd151d4"


def install(self):
    self.install_files("usr", "")
