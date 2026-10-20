pkgname = "nmap"
pkgver = "7.992"
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
sha256 = "0c12660eddbf7eabeff6996cb0c044a4eadf2bb0c6fbcb340d6cf72b1caee402"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("nmap-ncat")
def _(self):
    self.subdesc = "Netcat tool"
    return ["usr/bin/ncat"]
