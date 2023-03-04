pkgname = "libfuse2"
pkgver = "2.9.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-lib"]
hostmakedepends = ["automake", "libtool", "gettext-tiny-devel", "pkgconf"]
makedepends = ["linux-headers", "udev-devel"]
pkgdesc = "Filesystem in USErspace (2.x)"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/fuse-{pkgver}/fuse-{pkgver}.tar.gz"
sha256 = "d0e69d5d608cc22ff4843791ad097f554dd32540ddc9bed7638cc6fea7c1b4b5"
suid_files = ["usr/bin/fusermount"]
wrksrc = "fuse"


def post_install(self):
    self.mv(self.destdir / "sbin/mount.fuse", self.destdir / "usr/bin")
    self.rm(self.destdir / "etc/udev", recursive=True)


@subpackage("libfuse2-devel")
def _devel(self):
    return self.default_devel()
