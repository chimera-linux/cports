pkgname = "ristretto"
pkgver = "0.13.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "file-devel",
    "glib-devel",
    "gtk+3-devel",
    "libexif-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce image viewer"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/ristretto/start"
source = f"$(XFCE_SITE)/apps/ristretto/{pkgver[:-2]}/ristretto-{pkgver}.tar.bz2"
sha256 = "5b9172ef704ae192a5338df6bee4e91a59edc65618c375bb4433ffb38e2126cb"
