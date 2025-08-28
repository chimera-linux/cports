pkgname = "networkmanager-openvpn"
pkgver = "1.12.3"
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
sha256 = "50ac3158faba8efb0a8d4a96de19c14f86e2408e265e2b5ec27a7a8826f38f64"
options = ["linkundefver"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
