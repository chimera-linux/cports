pkgname = "miniupnpd"
pkgver = "2.3.9"
pkgrel = 0
build_wrksrc = "miniupnpd"
build_style = "configure"
configure_args = [
    "--disable-fork",
    "--firewall=nftables",
    "--igd2",
    "--ipv6",
    "--leasefile",
    "--pcp-peer",
    "--portinuse",
    "--vendorcfg",
]
make_env = {"SBINDIR": "/usr/bin"}
hostmakedepends = [
    "musl-bsd-headers",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "iptables-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "linux-headers",
    "util-linux-uuid-devel",
]
depends = ["nftables"]
checkdepends = ["iproute2"]
pkgdesc = "UPnP IGD and PCP/NAT-PMP daemon for gateway router"
license = "BSD-3-Clause"
url = "https://github.com/miniupnp/miniupnp"
source = f"{url}/archive/refs/tags/miniupnpd_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "ec7981351ad6a046eee0abf522ed1a45a3b0517e1da64e03826051f5f5354ea5"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "miniupnpd")
