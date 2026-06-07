pkgname = "evolution"
pkgver = "3.60.2"
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
sha256 = "218a49fa5068155dbdbd35a30d10a2f237c72465fb1d0e0aa78889f039c2ed8f"


@subpackage("evolution-devel")
def _(self):
    return self.default_devel()
