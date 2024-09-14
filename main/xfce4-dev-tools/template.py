pkgname = "xfce4-dev-tools"
pkgver = "4.18.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xsltproc",
]
makedepends = ["glib-devel"]
pkgdesc = "Xfce development tools"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-dev-tools/start"
source = f"$(XFCE_SITE)/xfce/xfce4-dev-tools/{pkgver[:-2]}/xfce4-dev-tools-{pkgver}.tar.bz2"
sha256 = "812cabe7048922ebc176564b73c3e427e467c9566365ee3e54c0487d305a7681"
