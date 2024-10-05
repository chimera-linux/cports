pkgname = "gnome-software"
pkgver = "47.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dtests=false",
    "-Dpackagekit=false",
    "-Dmalcontent=false",
    "-Dwebapps=false",
    "-Dgtk_doc=false",
    "-Dhardcoded_foss_webapps=false",
    "-Dhardcoded_proprietary_webapps=false",
    "-Ddefault_library=shared",
]
make_check_wrapper = ["dbus-run-session", "wlheadless-run", "--"]
hostmakedepends = [
    "appstream",
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "appstream-devel",
    "flatpak-devel",
    "fwupd-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgudev-devel",
    "libsoup-devel",
    "libxmlb-devel",
    "linux-headers",
    "polkit-devel",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "GNOME software center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-software"
source = (
    f"$(GNOME_SITE)/gnome-software/{pkgver[:-2]}/gnome-software-{pkgver}.tar.xz"
)
sha256 = "4f3e9b30f2d4885198329e46076e5ed9b5bd7e099062ae627377ad8d9b9556ef"
# Most tests need system dbus
options = ["!check"]


@subpackage("gnome-software-devel")
def _(self):
    return self.default_devel()
