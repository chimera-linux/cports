pkgname = "bcachefs-tools"
pkgver = "1.9.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "ROOT_SBINDIR=/usr/bin",
    "TRIPLET=" + self.profile().triplet,
]
make_use_env = True
hostmakedepends = ["cargo", "gmake", "pkgconf"]
makedepends = [
    "clang-devel",
    "keyutils-devel",
    "libaio-devel",
    "libblkid-devel",
    "libsodium-devel",
    "libuuid-devel",
    "linux-headers",
    "lz4-devel",
    "udev-devel",
    "userspace-rcu-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Bcachefs utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/koverstreet/bcachefs-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "735a715e4d38ff3ff581509b730deb1c092f34bfb91fe6a7da83c573871859d9"
# no tests
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)


def init_build(self):
    from cbuild.util import cargo

    # sigh
    self.make_build_args += [
        "EXTRA_CFLAGS=" + self.get_cflags(shell=True),
        "EXTRA_LDFLAGS=" + self.get_ldflags(shell=True),
    ]
    # apply our rust stuff
    self.env.update(cargo.get_environment(self))
