pkgname = "dracut-install"
pkgver = "107"
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
url = "https://github.com/dracut-ng/dracut-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b39d0d1cd35ff43aba8771c5367d8c6c59bb432c0cac62f49601f21c0d634895"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
