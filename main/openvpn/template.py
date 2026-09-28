pkgname = "openvpn"
pkgver = "2.7.7"
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
sha256 = "b56dd6c4e8b38ce43e6f4a901435a41b0b646bd90ec050b38ea2ee5e94e81bde"
options = ["etcfiles"]


def post_install(self):
    self.install_file(
        self.files_path / "update-resolv-conf", "etc/openvpn", mode=0o744
    )

    self.install_license("COPYING")
