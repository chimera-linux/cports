pkgname = "rtmpdump"
pkgver = "2.4.20210219"
pkgrel = 3
build_style = "makefile"
make_build_args = ["CRYPTO=OPENSSL"]
make_install_args = ["prefix=/usr", "sbindir=/usr/bin", "mandir=/usr/share/man"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel", "openssl3-devel", "linux-headers"]
pkgdesc = "Toolkit for RTMP streams"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://rtmpdump.mplayerhq.hu"
source = f"https://repo.chimera-linux.org/distfiles/rtmpdump-{pkgver}.tar.xz"
sha256 = "705b7a99af575e07613c436bc58829cb04d924776949cb243d03091335747139"
tool_flags = {
    "CFLAGS": [
        "-D__LINUX_NETFILTER_H",
        "-DOPENSSL_API_COMPAT=0x10100000L",
        "-Wno-unused-const-variable",
        "-Wno-deprecated-declarations",
    ]
}
# FIXME sus
hardening = ["!int"]
# no test suite
options = ["!check"]


def init_configure(self):
    cfl = self.get_cflags(shell=True)

    self.make_build_args += [
        "CC=" + self.get_tool("CC"),
        "OPT=" + cfl,
        "XLDFLAGS=" + self.get_ldflags(shell=True) + " " + cfl,
    ]


@subpackage("rtmpdump-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("librtmp")]

    return self.default_libs()


@subpackage("rtmpdump-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel"]
    # transitional
    self.provides = [self.with_pkgver("librtmp-devel")]

    return self.default_devel()
