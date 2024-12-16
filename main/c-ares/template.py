pkgname = "c-ares"
pkgver = "1.34.4"
pkgrel = 0
build_style = "gnu_configure"
# circular gtest
configure_args = ["--disable-tests"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://github.com/c-ares/c-ares/releases/download/v{pkgver}/c-ares-{pkgver}.tar.gz"
sha256 = "fa38dbed659ee4cc5a32df5e27deda575fa6852c79a72ba1af85de35a6ae222f"
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")

    # only cmake has a toggle to install these..
    with self.pushd(f"{self.make_dir}/src/tools/.libs"):
        self.install_bin("adig")
        self.install_bin("ahost")

    self.install_man("docs/adig.1")
    self.install_man("docs/ahost.1")


@subpackage("c-ares-devel")
def _(self):
    return self.default_devel()


@subpackage("c-ares-progs")
def _(self):
    return self.default_progs()
