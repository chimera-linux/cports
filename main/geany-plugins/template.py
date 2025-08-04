pkgname = "geany-plugins"
pkgver = "2.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-all-plugins",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "intltool",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "ctpl-devel",
    "enchant-devel",
    "geany-devel",
    "gpgme-devel",
    "libgit2-devel",
    "libsoup-devel",
    "lua5.1-devel",
    "vte-gtk3-devel",
    "webkitgtk-devel",
    "zlib-ng-compat-devel",
]
depends = [f"geany~{pkgver}"]
pkgdesc = "Geany IDE plugins"
license = "GPL-2.0-or-later"
url = "https://geany.org"
# source = f"https://github.com/geany/geany-plugins/releases/download/{pkgver}/geany-plugins-{pkgver[:-2]}.tar.gz"
source = (
    f"https://github.com/geany/geany-plugins/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "9ca8412763c2f8a7141f6a1569166f4fabf95fc8aad5149a754265673ffce5bb"
