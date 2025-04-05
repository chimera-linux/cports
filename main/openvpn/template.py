pkgname = "openvpn"
pkgver = "2.6.14"
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
license = "GPL-2.0-only WITH openvpn-openssl-exception"
url = "https://openvpn.net"
source = f"https://github.com/OpenVPN/openvpn/releases/download/v{pkgver}/openvpn-{pkgver}.tar.gz"
sha256 = "9eb6a6618352f9e7b771a9d38ae1631b5edfeed6d40233e243e602ddf2195e7a"


def post_install(self):
    self.install_file(
        self.files_path / "update-resolv-conf", "etc/openvpn", mode=0o744
    )

    self.install_license("COPYING")
