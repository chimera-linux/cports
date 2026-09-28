pkgname = "evolution"
pkgver = "3.62.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBEXEC_INSTALL_DIR=/usr/lib",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "highlight",
    "intltool",
    "itstool",
    "ninja",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "cmark-devel",
    "enchant-devel",
    "evolution-data-server-devel",
    "gdk-pixbuf-devel",
    "geocode-glib-devel",
    "glib-devel",
    "gnome-autoar-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libgweather-devel",
    "libnotify-devel",
    "libpst-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "nspr-devel",
    "nss-devel",
    "openldap-devel",
    "shared-mime-info",
    "sqlite-devel",
    "webkitgtk-devel",
    "xorgproto",
    "ytnef-devel",
]
depends = ["highlight"]
pkgdesc = "Mail, calendar and address book suite"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Evolution"
source = f"https://download.gnome.org/sources/evolution/{pkgver[:-2]}/evolution-{pkgver}.tar.xz"
sha256 = "7fc2cc40e1699bf706b5cfcf0255650fc4623b99edbc72c5ad026cea2587a3d6"
# needs display
options = ["!check"]


@subpackage("evolution-devel")
def _(self):
    return self.default_devel()
