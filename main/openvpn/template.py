pkgname = "openvpn"
pkgver = "2.6.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-systemd",
    "--enable-x509-alt-username",
    "--enable-iproute2",
    "--with-openssl-engine",
    "--with-crypto-library=openssl",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "iproute2",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "cmocka-devel",
    "libcap-ng-devel",
    "libnl-devel",
    "linux-headers",
    "linux-pam-devel",
    "lz4-devel",
    "lzo-devel",
    "openssl3-devel",
    "pcre2-devel",
]
depends = ["iproute2"]
pkgdesc = "Open source VPN daemon"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-only WITH openvpn-openssl-exception"
url = "https://openvpn.net"
source = f"https://github.com/OpenVPN/openvpn/releases/download/v{pkgver}/openvpn-{pkgver}.tar.gz"
sha256 = "1af10b86922bd7c99827cc0f151dfe9684337b8e5ebdb397539172841ac24a6a"


def post_install(self):
    self.install_file(
        self.files_path / "update-resolv-conf", "etc/openvpn", mode=0o744
    )

    self.install_license("COPYING")
