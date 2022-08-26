pkgname = "tracker"
pkgver = "3.3.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false", "-Dman=true", "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala",
    "asciidoc", "xsltproc", "dbus", "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "libglib-devel", "dbus-devel", "icu-devel", "json-glib-devel",
    "libxml2-devel", "sqlite-devel", "libsoup-devel", "bash-completion"
]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4094f704e338f2247fa6b94633279cfd07f7e952bb24627128fab78edb242464"
# needs a dbus environment for check
# lto fails: Invalid GType function: 'tracker_endpoint_http_get_type'
options = ["!check", "!cross", "!lto"]

@subpackage("tracker-devel")
def _devel(self):
    return self.default_devel()

@subpackage("tracker-libs")
def _libs(self):
    return self.default_libs()
