pkgname = "dracut-install"
pkgver = "102"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_build_target = "dracut-install"
hostmakedepends = ["bash", "gmake", "pkgconf"]
makedepends = ["libkmod-devel", "musl-fts-devel"]
checkdepends = ["asciidoc"]
pkgdesc = "Dracut-install command from dracut"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/dracut-ng/dracut-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "601b175cbf4d2ee902bb7bda3af8826ae2ca060c1af880f6da5a833413f4ec70"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def do_install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
