pkgname = "tracker"
pkgver = "3.7.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "asciidoc",
    "xsltproc",
    "dbus",
    "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "icu-devel",
    "json-glib-devel",
    "libxml2-devel",
    "sqlite-devel",
    "libsoup-devel",
    "bash-completion",
]
depends = ["shared-mime-info"]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cd91b885ee9839cde5387f8e05ed24a7108d1627629cb6b1b2aa51a9603e130a"
options = ["!cross"]


@subpackage("tracker-devel")
def _devel(self):
    return self.default_devel()


@subpackage("tracker-libs")
def _libs(self):
    return self.default_libs()
