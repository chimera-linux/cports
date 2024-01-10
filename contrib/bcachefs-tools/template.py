pkgname = "bcachefs-tools"
pkgver = "1.4.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["ROOT_SBINDIR=/usr/bin"]
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
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Bcachefs utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/koverstreet/bcachefs-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3fea7aba076d1400eba29317c8b1de0b8ed83012ab004afaa948fc0750807f58"
# no tests
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="rust-src")
    cargo.setup_vendor(self, wrksrc="rust-src")


def init_build(self):
    from cbuild.util import cargo

    # sigh
    self.make_build_args += [
        "EXTRA_CFLAGS=" + self.get_cflags(shell=True),
        "EXTRA_LDFLAGS=" + self.get_ldflags(shell=True),
    ]
    # apply our rust stuff
    self.env.update(cargo.get_environment(self))
