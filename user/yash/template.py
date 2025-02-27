pkgname = "yash"
pkgver = "2.58.1"
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
sha256 = "7674ece98dc77bcc753db49c4311c30532f981682205f9047f20213a3a6755bb"


def post_install(self):
    self.install_shell("/usr/bin/yash")
    self.install_file(self.files_path / "yashrc", "etc")
