pkgname = "thrift"
pkgver = "0.22.0"
pkgrel = 1
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
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Scalable cross-language services framework for IPC/RPC"
subdesc = "compiler"
license = "Apache-2.0"
url = "https://thrift.apache.org"
source = f"https://github.com/apache/thrift/archive/v{pkgver}.tar.gz"
sha256 = "c4649c5879dd56c88f1e7a1c03e0fbfcc3b2a2872fb81616bffba5aa8a225a37"


@subpackage("thrift-devel")
def _(self):
    return self.default_devel()


@subpackage("thrift-glib-libs")
def _(self):
    self.subdesc = "Thrift C glib library"
    return ["usr/lib/libthrift_*glib*.so.*"]


@subpackage("thrift-libs")
def _(self):
    return self.default_libs()
