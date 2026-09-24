pkgname = "nmap"
pkgver = "7.991"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-openssl=yes",
    "--with-libpcap=yes",
    "--with-libpcre=yes",
    "--with-liblua=yes",
    "--with-libssh2=yes",
    "--with-libz-prefix=/usr/lib",
    "--without-zenmap",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
]
makedepends = [
    "libpcap-devel",
    "libssh2-devel",
    "linux-headers",
    "lua5.4-devel",
    "openssl3-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
depends = [self.with_pkgver("nmap-ncat")]
pkgdesc = "Utility for network discovery and security auditing"
license = "custom:Nmap"
url = "https://nmap.org"
source = f"https://nmap.org/dist/nmap-{pkgver}.tar.bz2"
sha256 = "a5d507f29437bef3bedd4771ff9aaa8fc1c2a109ddba1f5b1cf12027456929be"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("nmap-ncat")
def _(self):
    self.subdesc = "Netcat tool"
    return ["usr/bin/ncat"]
