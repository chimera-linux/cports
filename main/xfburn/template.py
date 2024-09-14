pkgname = "xfburn"
pkgver = "0.7.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libburn-devel",
    "libgudev-devel",
    "libisofs-devel",
    "libxfce4ui-devel",
]
pkgdesc = "Xfce burning software"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfburn/start"
source = f"$(XFCE_SITE)/apps/xfburn/{pkgver[:-2]}/xfburn-{pkgver}.tar.bz2"
sha256 = "c2bb01d9f7335e487f91db40ebddeea30d071364c1c3b56838466fd3367a9925"
