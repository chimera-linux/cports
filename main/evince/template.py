pkgname = "evince"
pkgver = "42.1"
pkgrel = 0
build_style = "meson"
# dvi needs kpathsea, which is in texlive
# does anyone actually need dvi?
configure_args = [
    "-Dintrospection=true", "-Dgtk_doc=false",
    "-Dcomics=enabled", "-Dps=enabled", "-Ddvi=disabled",
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
    "gspell-devel", "djvulibre-devel", "adwaita-icon-theme",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "GNOME document viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Evince"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b24767bb3d5103b4e35b0e15cf033dbe2488f88700cdd882d22a43adeec2e80a"

@subpackage("evince-libs")
def _libs(self):
    return self.default_libs()

@subpackage("evince-devel")
def _devel(self):
    return self.default_devel()
