pkgname = "gsettings-desktop-schemas"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel"]
depends = [
    "adwaita-icon-theme",
    "chimera-artwork",
    "fonts-adwaita-ttf",
]
pkgdesc = "Collection of GSettings schemas"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas"
source = f"$(GNOME_SITE)/gsettings-desktop-schemas/{pkgver[:-2]}/gsettings-desktop-schemas-{pkgver}.tar.xz"
sha256 = "777a7f83d5e5a8076b9bf809cb24101b1b1ba9c230235e3c3de8e13968ed0e63"
options = ["!cross"]


def post_install(self):
    self.install_file(
        self.files_path / "10_chimera_theme.gschema.override",
        "usr/share/glib-2.0/schemas",
    )


@subpackage("gsettings-desktop-schemas-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
