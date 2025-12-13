pkgname = "xfce4-verve-plugin"
pkgver = "2.1.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "pcre2-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce command line panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-verve-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-verve-plugin/{pkgver[:-2]}/xfce4-verve-plugin-{pkgver}.tar.xz"
sha256 = "237e0da802cdc02e0ec0c3cdefecb6fa2992ade9f59ce2999779cc30d59c9f24"
