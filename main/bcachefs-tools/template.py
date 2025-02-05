pkgname = "bcachefs-tools"
pkgver = "1.13.0"
pkgrel = 1
build_style = "makefile"
make_install_args = [
    "ROOT_SBINDIR=/usr/bin",
    "TRIPLET=" + self.profile().triplet,
]
make_use_env = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "clang-devel",
    "keyutils-devel",
    "libaio-devel",
    "libsodium-devel",
    "linux-headers",
    "lz4-devel",
    "rust-std",
    "udev-devel",
    "userspace-rcu-devel",
    "util-linux-blkid-devel",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Bcachefs utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/koverstreet/bcachefs-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cc7196505eba3a71e2ab8b9d0d19c6b16959b15aeb6e57e696dc14bd735ee0d5"
# no tests
options = ["!check"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    # sigh
    self.make_build_args += [
        "EXTRA_CFLAGS=" + self.get_cflags(shell=True),
        "EXTRA_LDFLAGS=" + self.get_ldflags(shell=True),
    ]
    # apply our rust stuff
    self.env.update(cargo.get_environment(self))
