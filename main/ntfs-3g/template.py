pkgname = "ntfs-3g"
pkgver = "2026.7.7"
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
    "gnutls-devel",
    "libgcrypt-devel",
    "linux-headers",
    "util-linux-uuid-devel",
]
depends = ["fuse"]
pkgdesc = "NTFS FUSE driver and tools"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/tuxera/ntfs-3g"
source = f"https://tuxera.com/opensource/ntfs-3g_ntfsprogs-{pkgver}.tgz"
sha256 = "d67b769025d32860549d35c2147e45024d172f81c540d750390ce3602c059dab"


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
