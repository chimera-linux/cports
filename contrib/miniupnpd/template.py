pkgname = "miniupnpd"
pkgver = "2.3.6"
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
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "musl-bsd-headers",
    "pkgconf",
]
makedepends = [
    "libiptc-devel",
    "libmnl-devel",
    "libnftnl-devel",
    "libuuid-devel",
    "linux-headers",
]
depends = ["nftables"]
checkdepends = ["iproute2"]
pkgdesc = "UPnP and NAT-PMP daemon for gateway routers"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://github.com/miniupnp/miniupnp"
source = f"{url}/archive/refs/tags/{pkgname}_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "6e5ee2239030486675f558cc840d154e5e2db9517efc96c5b0ab2b2c34c1a128"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "miniupnpd")
