pkgname = "evince"
pkgver = "44.3"
pkgrel = 1
build_style = "meson"
# dvi needs kpathsea, which is in texlive
# does anyone actually need dvi?
configure_args = [
    "-Dintrospection=true",
    "-Dgtk_doc=false",
    "-Dnautilus=false",
    "-Dcomics=enabled",
    "-Dps=enabled",
    "-Ddvi=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "itstool",
    "gettext-tiny",
    "perl-xml-parser",
    "adwaita-icon-theme",
    "desktop-file-utils",
]
makedepends = [
    "gtk+3-devel",
    "glib-devel",
    "libhandy-devel",  # "nautilus-devel",
    "dbus-devel",
    "libsecret-devel",
    "gstreamer-devel",
    "libspectre-devel",
    "libarchive-devel",
    "libpoppler-glib-devel",
    "gst-plugins-base-devel",
    "gsettings-desktop-schemas-devel",
    "libtiff-devel",
    "libgxps-devel",
    "gspell-devel",
    "djvulibre-devel",
]
depends = ["desktop-file-utils"]
pkgdesc = "GNOME document viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Evince"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3b8ba1581a47a6e9f57f6b6aa08f0fb67549c60121aa24e31140e93947b83622"


@subpackage("evince-libs")
def _libs(self):
    return self.default_libs()


@subpackage("evince-devel")
def _devel(self):
    return self.default_devel()
