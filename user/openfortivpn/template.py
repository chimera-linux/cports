pkgname = "openfortivpn"
pkgver = "1.24.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-proc",
    "--enable-resolvconf",
    "--with-ppp=/usr/bin/ppp",
    "--with-pppd=/usr/bin/pppd",
    "--with-resolvconf=/usr/bin/resolvconf",
    "--with-rt_dst",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["openssl3-devel"]
depends = ["ppp", "resolvconf"]
pkgdesc = "Open implementation of Fortinet's PPP+SSL VPN solution"
license = "GPL-3.0-or-later"
url = "https://github.com/adrienverge/openfortivpn"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e773c773bdb1d44b2d54215e43573adcca1685ed0e63e58177bf52e16cbf7e5"
options = ["etcfiles"]
