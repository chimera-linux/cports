pkgname = "font-manager"
pkgver = "0.8.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dnautilus=true",
    "-Dthunar=true",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
    "yelp-tools",
]
makedepends = [
    "gtk+3-devel",
    "json-glib-devel",
    "libsoup-devel",
    "nautilus-devel",
    "thunar-devel",
    "webkitgtk-devel",
]
pkgdesc = "Font management application"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://fontmanager.github.io"
# they forgor to tag it lol
source = f"https://github.com/FontManager/font-manager/archive/9c52ed802841eed2bd9ed4f1c7d662dd94a112dc.tar.gz"
sha256 = "2f33bdfca59c8c72d044e7fce3d0f103371647eff63fd64248699d7b9c2b2669"
# gobject-introspection
options = ["!cross"]


@subpackage("font-manager-nautilus")
def _nautilus(self):
    self.pkgdesc = f"{pkgdesc} (nautilus plugin)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nautilus"]
    return ["usr/lib/nautilus"]


@subpackage("font-manager-thunar")
def _thunar(self):
    self.pkgdesc = f"{pkgdesc} (thunar plugin)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "thunar"]
    return ["usr/lib/thunarx-3"]
