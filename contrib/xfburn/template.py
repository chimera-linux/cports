pkgname = "xfburn"
pkgver = "0.7.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
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
sha256 = "7ca161b2c9c558e5161f02f69d0418a37eba15eab4d3a8651f6c97d3a9d5dc16"
