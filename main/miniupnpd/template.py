pkgname = "miniupnpd"
pkgver = "2.3.10"
pkgrel = 0
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
source = f"{url}/releases/download/miniupnpd_{pkgver.replace('.', '_')}/miniupnpd-{pkgver}.tar.gz"
sha256 = "f9c34ed3632fb60cd248dd5897bd98479a103a75688b056ca2f069e68ab32987"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "miniupnpd")
