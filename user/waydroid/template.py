pkgname = "waydroid"
pkgver = "1.6.3"
pkgrel = 0
build_style = "makefile"
make_install_args = ["USE_SYSTEMD=0", "USE_NFTABLES=1"]
hostmakedepends = ["python"]
makedepends = ["dinit-chimera"]
depends = [
    "dnsmasq",
    "lxc",
    "nftables",
    "python-dbus",
    "python-gbinder",
    "python-gobject",
]
# invoke the trigger on self
triggers = ["/usr/lib/waydroid"]
pkgdesc = "Container-based approach to boot a full Android system"
license = "GPL-3.0-or-later"
url = "https://github.com/waydroid/waydroid"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f138a287eb8b0be7be7f7060971446490138bc2c8315665c8aa9c2c85576d8a5"
# check: no tests
options = ["etcfiles", "!check"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
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
