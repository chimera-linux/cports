pkgname = "dracut-install"
pkgver = "111"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-dracut-cpio"]
configure_gen = []
make_dir = "."
make_build_target = "dracut-install"
hostmakedepends = ["bash", "pkgconf"]
makedepends = ["chimerautils-devel", "kmod-devel"]
checkdepends = ["asciidoc"]
pkgdesc = "Dracut-install command from dracut"
license = "GPL-2.0-or-later"
url = "https://github.com/dracut-ng/dracut"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ca949190692e91611ef16ea3642c0f764f63948860f3f742524310728c991493"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
