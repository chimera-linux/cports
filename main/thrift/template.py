pkgname = "thrift"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_AS3=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DWITH_JAVA=OFF",
    "-DWITH_JAVASCRIPT=OFF",
    "-DWITH_NODEJS=OFF",
    "-DWITH_PYTHON=OFF",
]
hostmakedepends = ["bison", "cmake", "flex", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "glib-devel",
    "libevent-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Scalable cross-language services framework for IPC/RPC"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://thrift.apache.org"
source = f"https://dlcdn.apache.org/thrift/{pkgver}/thrift-{pkgver}.tar.gz"
sha256 = "9a24f3eba9a4ca493602226c16d8c228037db3b9291c6fc4019bfe3bd39fc67c"


@subpackage("thrift-devel")
def _(self):
    return self.default_devel()


@subpackage("thrift-glib")
def _(self):
    return ["usr/lib/libthrift_*glib*.so.*"]


@subpackage("thrift-libnb")
def _(self):
    return ["usr/lib/libthriftnb*.so.*"]


@subpackage("thrift-libz")
def _(self):
    return ["usr/lib/libthriftz*.so.*"]
