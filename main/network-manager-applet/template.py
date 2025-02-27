pkgname = "network-manager-applet"
pkgver = "1.36.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dselinux=false"]
hostmakedepends = ["meson", "pkgconf", "gettext"]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "jansson-devel",
    "libayatana-appindicator-devel",
    "libdbusmenu-devel",
    "libnma-devel",
    "libsecret-devel",
    "modemmanager-devel",
    "networkmanager-devel",
]
# https://gitlab.gnome.org/GNOME/network-manager-applet/-/commit/574fdd97ae38b89f6d3d1a1c3fbfd63754b25df2
replaces = ["libnma<=1.10.6-r0"]
pkgdesc = "Network manager tray applet"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/network-manager-applet"
source = f"$(GNOME_SITE)/network-manager-applet/{pkgver[:-2]}/network-manager-applet-{pkgver}.tar.xz"
sha256 = "a84704487ea3afe1485c47fb2ab598b8f779f540ae0dcbf0a1c5f85e64a7e253"
options = ["linkundefver"]
