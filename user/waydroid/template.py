pkgname = "waydroid"
pkgver = "1.5.4"
pkgrel = 0
build_style = "makefile"
make_install_args = ["USE_SYSTEMD=0", "USE_NFTABLES=1"]
hostmakedepends = ["python"]
makedepends = ["dinit-chimera"]
depends = [
    "dnsmasq",
    "lxc",
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
sha256 = "b97b91673b3cc7e7f001395c08e2d2d569305216a1dd9b3c9a65f03ebc296e18"
# check: no tests
options = ["!check"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
    self.install_service("^/waydroid-container")
    self.install_file(
        "^/51_waydroid.nft", "etc/nftables.d", name="51_waydroid.nft"
    )
    self.install_file(
        "^/modules-load.conf", "usr/lib/modules-load.d", name="waydroid.conf"
    )
