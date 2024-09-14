pkgname = "yash"
pkgver = "2.57"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--enable-array",
    "--enable-dirstack",
    "--enable-double-bracket",
    "--enable-help",
    "--enable-history",
    "--enable-lineedit",
    "--enable-printf",
    "--enable-socket",
    "--enable-test",
    "--enable-ulimit",
    "--prefix=/usr",
]
makedepends = ["ncurses-devel"]
checkdepends = ["procps"]
pkgdesc = "Yet another shell"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-2.0-only"
url = "https://github.com/magicant/yash"
source = f"{url}/releases/download/{pkgver}/yash-{pkgver}.tar.xz"
sha256 = "f5ff3334dcfa0fdde3882f5df002623f46a0a4f2b2335e7d91715520d8fb1dab"


def post_install(self):
    self.install_shell("/usr/bin/yash")
    self.install_file(self.files_path / "yashrc", "etc")
