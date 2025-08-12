pkgname = "networkmanager-openvpn"
pkgver = "1.12.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-gtk4",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "file",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "libnma-devel",
    "libsecret-devel",
]
depends = ["openvpn"]
pkgdesc = "OpenVPN support for NetworkManager"
license = "GPL-2.0-or-later"
url = "https://github.com/NetworkManager/NetworkManager-openvpn/tree/main"
source = f"https://github.com/NetworkManager/NetworkManager-openvpn/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "290c7322f0bfc5f3e6e4d86cabeccf633fe645042a3ddbf9383bde5f0011ea4c"
options = ["linkundefver"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
