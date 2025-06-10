pkgname = "gnome-software"
pkgver = "48.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
    "libxslt-progs",
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
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-software"
source = (
    f"$(GNOME_SITE)/gnome-software/{pkgver[:-2]}/gnome-software-{pkgver}.tar.xz"
)
sha256 = "abfd30643a86c65f4886b6765eb3bb6215c9ea09817d6bd165c50056890822c9"
# Most tests need system dbus
options = ["!check"]


@subpackage("gnome-software-devel")
def _(self):
    return self.default_devel()
