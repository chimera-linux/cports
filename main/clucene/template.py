pkgname = "clucene"
pkgver = "2.3.3.4"
pkgrel = 10
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
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
license = "LGPL-2.0-or-later OR Apache-2.0"
url = "https://clucene.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/clucene/clucene-core-{pkgver}.tar.gz"
sha256 = "ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab"
# TODO fails multiple tests
hardening = ["!int"]
# check may be disabled
options = ["!cross"]

if self.profile().wordsize == 32:
    # 32-bit tests are broken, see e.g.:
    # https://git.adelielinux.org/adelie/packages/-/issues/873
    options += ["!check"]


def post_check(self):
    self.mkdir("build/tmp", parents=True)
    self.do("./cl_test", wrksrc="build/bin", env={"TMP": "../tmp"})


def post_install(self):
    self.uninstall("usr/lib/CLuceneConfig.cmake")


@subpackage("clucene-devel")
def _(self):
    return self.default_devel()
