pkgname = "miniupnpd"
pkgver = "2.3.7"
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
make_env = {"SBININSTALLDIR": "/usr/bin"}
hostmakedepends = [
    "musl-bsd-headers",
    "pkgconf",
]
makedepends = [
    "iptables-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "linux-headers",
    "util-linux-uuid-devel",
]
depends = ["nftables"]
checkdepends = ["iproute2"]
pkgdesc = "UPnP IGD and PCP/NAT-PMP daemon for gateway router"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://github.com/miniupnp/miniupnp"
source = f"{url}/archive/refs/tags/miniupnpd_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "bbcada94edb0ae6340533cac4633f7a36a515c81bd2815ec0c4e97164c577e8b"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "miniupnpd")
