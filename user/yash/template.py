pkgname = "yash"
pkgver = "2.61"
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
license = "GPL-2.0-only"
url = "https://github.com/magicant/yash"
source = f"{url}/releases/download/{pkgver}/yash-{pkgver}.tar.xz"
sha256 = "a214966f4ff8b293aa5521a4d3ef6e87d707579eee616aa2f8218edaa920d447"


def post_install(self):
    self.install_shell("/usr/bin/yash")
    self.install_file(self.files_path / "yashrc", "etc")
