pkgname = "thunar-media-tags-plugin"
pkgver = "0.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "taglib-devel",
    "thunar-devel",
]
pkgdesc = "Thunar media tags plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/media-tags"
source = f"$(XFCE_SITE)/thunar-plugins/thunar-media-tags-plugin/{pkgver[:-2]}/thunar-media-tags-plugin-{pkgver}.tar.xz"
sha256 = "b62dc047100346324e63d46acaaa497e8d7fccd1d10ef5bfb8370fd666a48c4a"
