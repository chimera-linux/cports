pkgname = "ristretto"
pkgver = "0.13.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "exo-devel",
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
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/ristretto/start"
source = f"$(XFCE_SITE)/apps/ristretto/{pkgver[:-2]}/ristretto-{pkgver}.tar.xz"
sha256 = "a84ef8cb80638681d9b9ef09cddff86a5d7a0e028603b4a601cf0ff6c2869ce8"
