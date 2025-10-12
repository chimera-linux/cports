pkgname = "bcachefs-tools"
pkgver = "1.31.7"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "ROOT_SBINDIR=/usr/bin",
    "TRIPLET=" + self.profile().triplet,
]
make_use_env = True
hostmakedepends = ["cargo-auditable", "jq", "pkgconf"]
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
license = "GPL-2.0-only"
url = "https://github.com/koverstreet/bcachefs-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e4b6b2af769575cc77496976c72e9aaaeec3a54af71d556f101b5e26aeb1ba85"
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

        # We need to set ROOT_SBINDIR to /usr/bin,
        # or else bcachefs-tools' Makefile will generate an initramfs hook
        # that tries to copy the `bcachefs` exectable from `/usr/local/sbin/`,
        # instead of from `/usr/bin`.
        "ROOT_SBINDIR=/usr/bin",
    ]
    # apply our rust stuff
    self.env.update(cargo.get_environment(self))

def post_install(self):
    # install ckms source tree
    srcp = f"usr/src/bcachefs-{pkgver}"
    self.install_dir(srcp)
    self.install_file(
        self.files_path / "ckms.ini", srcp, template={"VERSION": pkgver}
    )

@subpackage("bcachefs-tools-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
    ]

    return ["usr/src"]
