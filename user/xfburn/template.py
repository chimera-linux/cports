pkgname = "xfburn"
pkgver = "0.8.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
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
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfburn/start"
source = f"$(XFCE_SITE)/apps/xfburn/{pkgver[:-2]}/xfburn-{pkgver}.tar.bz2"
sha256 = "13a301aebcef27de18f63f8ca10b43bc42f9c1b9865dff1bfb3e97cfd95dd989"
