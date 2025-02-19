pkgname = "bcachefs-tools"
pkgver = "1.20.0"
pkgrel = 0
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
sha256 = "e616fea8bbd26581fb614fef9e50432a55a30248d7c42823cc06fee9e0d38747"
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
