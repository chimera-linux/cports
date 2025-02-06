pkgname = "ntfs-3g"
pkgver = "2022.10.3"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=/usr",
    "--sbin=/usr/bin",
    "--disable-static",
    "--disable-quarantined",
    "--enable-crypto",
    "--enable-extras",
    "--enable-posix-acls",
    "--enable-xattr-mappings",
    "--with-fuse=internal",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "gnutls-devel",
    "libgcrypt-devel",
    "linux-headers",
    "util-linux-uuid-devel",
]
depends = ["fuse"]
pkgdesc = "NTFS FUSE driver and tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/tuxera/ntfs-3g"
source = f"https://tuxera.com/opensource/ntfs-3g_ntfsprogs-{pkgver}.tgz"
sha256 = "f20e36ee68074b845e3629e6bced4706ad053804cbaf062fbae60738f854170c"


def pre_install(self):
    self.install_link("sbin", "usr/bin")


def post_install(self):
    self.install_link("usr/bin/mount.ntfs", "ntfs-3g")
    self.uninstall("usr/share/man/man8/ntfsfallocate.8")
    self.uninstall("sbin")


@subpackage("ntfs-3g-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libntfs-3g")]

    return self.default_libs()


@subpackage("ntfs-3g-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libntfs-3g-devel")]

    return self.default_devel()
