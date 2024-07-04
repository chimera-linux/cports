pkgname = "libfuse2"
pkgver = "2.9.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-lib", "--disable-static"]
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers", "udev-devel"]
pkgdesc = "Filesystem in USErspace 2.x runtime library"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/fuse-{pkgver}/fuse-{pkgver}.tar.gz"
sha256 = "d0e69d5d608cc22ff4843791ad097f554dd32540ddc9bed7638cc6fea7c1b4b5"


def post_install(self):
    # we are only interested in the library
    self.uninstall("sbin")
    self.uninstall("usr/bin")
    self.uninstall("usr/lib/pkgconfig")
    self.uninstall("usr/share")
    self.uninstall("usr/include")
    self.uninstall("etc")
    self.uninstall("usr/lib/*.so", glob=True)
    self.uninstall("usr/lib/libulockmgr*", glob=True)


configure_gen = []
