pkgname = "gsettings-desktop-schemas"
pkgver = "49.0"
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
sha256 = "912905cc45382888a47702ed1101c6b08ebd0122a32a67d940ab8116a96c520d"
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
