pkgname = "nmap"
pkgver = "7.95"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-openssl=yes",
    "--with-libpcap=yes",
    "--with-libpcre=yes",
    "--with-liblua=yes",
    "--with-libssh2=yes",
    "--with-libz-prefix=/usr/lib",
    "--without-zenmap",
    "CPP=",
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
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "custom:Nmap"
url = "https://nmap.org"
source = f"https://nmap.org/dist/nmap-{pkgver}.tar.bz2"
sha256 = "e14ab530e47b5afd88f1c8a2bac7f89cd8fe6b478e22d255c5b9bddb7a1c5778"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("nmap-ncat")
def _(self):
    self.subdesc = "Netcat tool"
    return ["usr/bin/ncat"]
