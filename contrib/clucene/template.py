pkgname = "clucene"
pkgver = "2.3.3.4"
pkgrel = 6
build_style = "cmake"
configure_args = [
    "-DENABLE_ASCII_MODE=OFF",
    "-DENABLE_PACKAGING=OFF",
    "-DBUILD_CONTRIBS_LIB=ON",
    "-DLIB_DESTINATION=/usr/lib",
    "-DLUCENE_SYS_INCLUDES=/usr/include",
    # tests fail with mt enabled
    "-DDISABLE_MULTITHREADING=ON",
]
make_check_target = "cl_test"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["boost-devel", "zlib-ng-compat-devel"]
pkgdesc = "Text search engine written in C++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later OR Apache-2.0"
url = "https://clucene.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-core-{pkgver}.tar.gz"
sha256 = "ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab"
# TODO fails multiple tests
hardening = ["!int"]
options = ["!cross"]


def post_check(self):
    self.mkdir("build/tmp", parents=True)
    self.do("./cl_test", wrksrc="build/bin", env={"TMP": "../tmp"})


def post_install(self):
    self.uninstall("usr/lib/CLuceneConfig.cmake")


@subpackage("clucene-devel")
def _devel(self):
    return self.default_devel()
