pkgname = "yash"
pkgver = "2.56.1"
pkgrel = 1
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
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f7f5a1ffd246692568e4823a59b20357317d92663573bd1099254c0c89de71f5"


def post_install(self):
    self.install_shell("/usr/bin/yash")
    self.install_file(self.files_path / "yashrc", "etc")
