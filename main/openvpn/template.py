pkgname = "openvpn"
pkgver = "2.6.12"
pkgrel = 1
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
    "slibtool",
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
    "openssl-devel",
    "pcre2-devel",
]
depends = ["iproute2"]
pkgdesc = "Open source VPN daemon"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-only WITH openvpn-openssl-exception"
url = "https://openvpn.net"
source = f"https://github.com/OpenVPN/openvpn/releases/download/v{pkgver}/openvpn-{pkgver}.tar.gz"
sha256 = "1c610fddeb686e34f1367c347e027e418e07523a10f4d8ce4a2c2af2f61a1929"


def post_install(self):
    self.install_file(
        self.files_path / "update-resolv-conf", "etc/openvpn", mode=0o744
    )
    self.install_dir("etc/openvpn/client")
    self.install_dir("etc/openvpn/server")

    self.install_service(self.files_path / "openvpn-client")
    self.install_service(self.files_path / "openvpn-server")

    self.install_license("COPYING")
