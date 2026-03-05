pkgname = "waydroid"
pkgver = "1.6.2"
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
sha256 = "4b963aceb9de2884020e98b26e40147b3f26a0444606633adc45b63752f57dca"
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
