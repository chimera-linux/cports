pkgname = "dracut-install"
pkgver = "106"
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
sha256 = "9009ac13072c9b583822ad1a17f2cca47af463190f0d6623e90b0f1107c71f95"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
