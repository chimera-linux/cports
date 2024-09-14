pkgname = "networkmanager-openvpn"
pkgver = "1.12.0"
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
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-or-later"
url = "https://github.com/NetworkManager/NetworkManager-openvpn/tree/main"
source = f"https://github.com/NetworkManager/NetworkManager-openvpn/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "def0fe3f8b118fe44bb61fce15da784f6b1560bfc03d1ac609aa57b3618ac1b7"
options = ["linkundefver"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
