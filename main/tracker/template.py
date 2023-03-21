pkgname = "tracker"
pkgver = "3.5.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false", "-Dman=true", "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala",
    "asciidoc", "xsltproc", "dbus", "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "glib-devel", "dbus-devel", "icu-devel", "json-glib-devel",
    "libxml2-devel", "sqlite-devel", "libsoup-devel", "bash-completion"
]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "13294275dbbbad9634b3a8390c08e6f12bebfe84f6ccafb72b27b0c23ba8da2f"
# lto fails: Invalid GType function: 'tracker_endpoint_http_get_type'
options = ["!cross", "!lto"]

@subpackage("tracker-devel")
def _devel(self):
    return self.default_devel()

@subpackage("tracker-libs")
def _libs(self):
    return self.default_libs()
