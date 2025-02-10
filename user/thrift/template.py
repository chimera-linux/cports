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
    "-DBUILD_TESTING=ON",
]
# some tests need net, skipped by alpine linux as well
make_check_args = [
    "-E",
    "StressTestConcurrent|\
StressTestNonBlocking|\
testapplicationexception|\
testbinaryprotocol|\
testbufferedtransport|\
testcompactprotocol|\
testdebugproto|\
testfdtransport|\
testframedtransport|\
testsimpleserver|\
testthriftbinaryreadcheck|\
testthriftbufferedreadcheck|\
testthriftframedreadcheck|\
testthriftfdreadcheck|\
testthriftcompactreadcheck|\
testtransportsocket|\
testzlibtransport|\
testthrifttestzlibclient",
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
source = f"https://github.com/apache/thrift/archive/v{pkgver}.tar.gz"
sha256 = "31e46de96a7b36b8b8a457cecd2ee8266f81a83f8e238a9d324d8c6f42a717bc"


@subpackage("thrift-devel")
def _(self):
    return self.default_devel(extra=["usr/bin/thrift"])


@subpackage("thrift-glib-libs")
def _(self):
    self.subdesc = "Thrift C glib library"
    return ["usr/lib/libthrift_*glib*.so.*"]


@subpackage("thrift-libnb-libs")
def _(self):
    self.subdesc = "Thrift Nonblocking API"
    return ["usr/lib/libthriftnb*.so.*"]


@subpackage("thrift-libz-libs")
def _(self):
    self.subdesc = "Thrift Zlib API"
    return ["usr/lib/libthriftz*.so.*"]
