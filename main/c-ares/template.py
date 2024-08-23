pkgname = "c-ares"
pkgver = "1.33.1"
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
sha256 = "06869824094745872fa26efd4c48e622b9bd82a89ef0ce693dc682a23604f415"
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
