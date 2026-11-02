pkgname = "gnome-software"
pkgver = "51.1"
pkgrel = 0
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
    "libxslt-progs",
    "meson",
    "pkgconf",
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
sha256 = "6501b1d7e499bfb8009f08efa3339ca6369bc38ee335cc3dfb67da7b2ab71289"
# Most tests need system dbus
options = ["etcfiles", "!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    # install autostart file again
    self.install_file(
        self.files_path / "org.gnome.Software.desktop", "etc/xdg/autostart"
    )


@subpackage("gnome-software-devel")
def _(self):
    return self.default_devel()
