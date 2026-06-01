pkgname = "networkmanager-openvpn"
pkgver = "1.12.5"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
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
sha256 = "45b213ddc42ba999a9143d3770b46779dc6e8e89383dd83c12842cc7411ef00f"
options = ["linkundefver"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.uninstall("usr/lib/sysusers.d/nm-openvpn-sysusers.conf")
    self.uninstall("usr/lib/tmpfiles.d/nm-openvpn-tmpfiles.conf")
