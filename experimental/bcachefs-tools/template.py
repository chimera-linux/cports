pkgname = "bcachefs-tools"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["NO_RUST=1"]
make_install_args = make_build_args + ["ROOT_SBINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "keyutils-devel",
    "libaio-devel",
    "libblkid-devel",
    "libsodium-devel",
    "libuuid-devel",
    "linux-headers",
    "lz4-devel",
    "udev-devel",
    "userspace-rcu-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Bcachefs utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/koverstreet/bcachefs-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f7b68576303bcbb80ea6c4042aa27b1b1027739f3de68106ca9166963e161dc"
# no tests
options = ["!check"]

def init_build(self):
    # sigh
    self.make_build_args += [
        "EXTRA_CFLAGS=" + self.get_cflags(shell = True),
        "EXTRA_LDFLAGS=" + self.get_ldflags(shell = True),
    ]
