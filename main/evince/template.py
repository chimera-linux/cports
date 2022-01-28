pkgname = "evince"
pkgver = "41.3"
pkgrel = 0
build_style = "meson"
# TODO: dvi, djvu
configure_args = [
    "-Dintrospection=true", "-Dgtk_doc=false",
    "-Dcomics=enabled", "-Dps=enabled", "-Ddvi=disabled",
    "-Dt1lib=disabled", "-Ddjvu=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "itstool",
    "gettext-tiny", "perl-xml-parser", "adwaita-icon-theme",
]
makedepends = [
    "gtk+3-devel", "libglib-devel", "libhandy-devel", "nautilus-devel",
    "dbus-devel", "libsecret-devel", "gstreamer-devel", "libspectre-devel",
    "libarchive-devel", "libpoppler-glib-devel", "gst-plugins-base-devel",
    "gsettings-desktop-schemas-devel", "libtiff-devel", "libgxps-devel",
    "gspell-devel", "adwaita-icon-theme",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "GNOME document viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Evince"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3346b01f9bdc8f2d5ffea92f110a090c64a3624942b5b543aad4592a9de33bb0"

@subpackage("evince-libs")
def _libs(self):
    return self.default_libs()

@subpackage("evince-devel")
def _devel(self):
    return self.default_devel()
