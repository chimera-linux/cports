pkgname = "openvpn"
pkgver = "2.7.0"
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
    "python-docutils",
]
depends = ["iproute2"]
pkgdesc = "Open source VPN daemon"
license = "GPL-2.0-only WITH openvpn-openssl-exception"
url = "https://openvpn.net"
source = (
    f"https://github.com/OpenVPN/openvpn/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "23af3dd1a76736d542f0fded4f81fdf14e27bdf7203e4ee29e9440d87e3c4209"


def post_install(self):
    self.install_file(
        self.files_path / "update-resolv-conf", "etc/openvpn", mode=0o744
    )

    self.install_license("COPYING")
