pkgname = "dracut-install"
pkgver = "105"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
make_build_target = "dracut-install"
hostmakedepends = ["bash", "pkgconf"]
makedepends = ["chimerautils-devel", "kmod-devel"]
checkdepends = ["asciidoc"]
pkgdesc = "Dracut-install command from dracut"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/dracut-ng/dracut-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a5f94012873f589e2efc3659341f5e383ec90419f5c361a6fd3561f946133f69"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
