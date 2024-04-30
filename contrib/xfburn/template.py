pkgname = "xfburn"
pkgver = "0.7.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
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
sha256 = "ba960ea79a044b93e513f7c32bca1a599472d687ed0e0184bde8c84aeebb1f45"
