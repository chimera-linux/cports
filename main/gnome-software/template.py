pkgname = "gnome-software"
pkgver = "46.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dpackagekit=false",
    "-Dfwupd=false",
    "-Dmalcontent=false",
    "-Dwebapps=false",
    "-Dgtk_doc=false",
    "-Dhardcoded_foss_webapps=false",
    "-Dhardcoded_proprietary_webapps=false",
    "-Ddefault_library=shared",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "docbook-xsl-nons",
    "xsltproc",
    "appstream",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "appstream-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "polkit-devel",
    "flatpak-devel",
    "libgudev-devel",
    "libsoup-devel",
    "libxmlb-devel",
    "json-glib-devel",
    "linux-headers",
]
checkdepends = ["dbus"]
pkgdesc = "GNOME software center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-software"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b6eeb789100de94b50ebe2e77f16b26be4c2db15489905f198d060c425e19076"
# TODO
options = ["!check"]


@subpackage("gnome-software-devel")
def _devel(self):
    return self.default_devel()
