pkgname = "ntfs-3g"
pkgver = "2022.10.3"
pkgrel = 0
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
    "libgcrypt-devel",
    "gnutls-devel",
    "libuuid-devel",
    "linux-headers",
]
depends = ["fuse"]
pkgdesc = "NTFS FUSE driver and tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/tuxera/ntfs-3g"
source = f"https://tuxera.com/opensource/{pkgname}_ntfsprogs-{pkgver}.tgz"
sha256 = "f20e36ee68074b845e3629e6bced4706ad053804cbaf062fbae60738f854170c"


def pre_install(self):
    self.install_link("sbin", "usr/bin")


def post_install(self):
    self.install_link("usr/bin/mount.ntfs", "ntfs-3g")
    self.uninstall("usr/share/man/man8/ntfsfallocate.8")
    self.uninstall("sbin")


@subpackage("libntfs-3g")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("libntfs-3g-devel")
def _devel(self):
    return self.default_devel()
