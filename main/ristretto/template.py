pkgname = "ristretto"
pkgver = "0.13.2"
pkgrel = 0
build_style = "gnu_configure"
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
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
sha256 = "779f5ede3016019eec01d64a025583078d3936e35d4288ec2e8433494d757dd9"
