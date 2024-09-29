pkgname = "gnome-builder"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dnetwork_tests=false"]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "clang-devel",
    "cmark-devel",
    "d-spy-devel",
    "editorconfig-devel",
    "enchant-devel",
    "flatpak-devel",
    "gom-devel",
    "gtksourceview-devel",
    "json-glib-devel",
    "jsonrpc-glib-devel",
    "libadwaita-devel",
    "libdex-devel",
    "libgit2-glib-devel",
    "libpanel-devel",
    "libpeas2-devel",
    "libportal-devel",
    "libspelling-devel",
    "libsoup-devel",
    "libxml2-devel",
    "ostree-devel",
    "sysprof-devel",
    "sysprof-devel-static",  # sysprof-capture-4 is static-only
    "template-glib-devel",
    "vte-gtk4-devel",
    "webkitgtk4-devel",
]
depends = [
    "flatpak-builder",
    "python-gobject",
    "python-lxml",
]
checkdepends = [
    "dbus",
    "xwayland-run",
    *depends,
]
pkgdesc = "Developer-oriented editor for GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Builder"
source = f"$(GNOME_SITE)/gnome-builder/{'.'.join(pkgver.rsplit('.')[:-1])}/gnome-builder-{pkgver}.tar.xz"
sha256 = "f700d69ddd0857db4f117ba7c38b1da63d596bab3ade8a14d69978c892f066f3"
# gobject-introspection
options = ["!cross"]


@subpackage("gnome-builder-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
