pkgname = "waydroid"
pkgver = "1.4.3"
pkgrel = 1
build_style = "makefile"
make_install_args = ["USE_SYSTEMD=0", "USE_NFTABLES=1"]
depends = [
    "dnsmasq",
    "lxc",
    "python-dbus",
    "python-gbinder",
    "python-gobject",
    "python-pyclip",
]
pkgdesc = "Container-based approach to boot a full Android system"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/waydroid/waydroid"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6557c6fed6a0a7417503eaaab3602efd67c6ced2026725ac24ec8c809fc672e4"
# check: no tests
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "waydroid-container")
    self.install_file(
        self.files_path / "51_waydroid.nft",
        "etc/nftables.d",
        name="51_waydroid.nft",
    )
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="waydroid.conf",
    )
