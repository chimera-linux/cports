pkgname = "libunwind-nongnu"
pkgver = "1.8.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include/libunwind-nongnu",
    "--disable-tests",
    "--enable-cxx-exceptions",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libucontext-devel",
    "linux-headers",
]
pkgdesc = "Stack unwinding library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://www.nongnu.org/libunwind"
source = f"https://github.com/libunwind/libunwind/releases/download/v{pkgver}/libunwind-{pkgver}.tar.gz"
sha256 = "ddf0e32dd5fafe5283198d37e4bf9decf7ba1770b6e7e006c33e6df79e6a6157"
tool_flags = {"LDFLAGS": ["-lucontext"]}
# bunch of these fail currently
options = ["!check"]

if self.profile().arch in ["ppc64", "ppc64le"]:
    # ld: error: relocation R_PPC64_REL16_LO cannot be used against symbol '.TOC.'; recompile with -fPIC
    options += ["!lto"]


# it's trying to export outline atomic helpers for some reason?
if self.profile().arch == "aarch64":
    tool_flags["CFLAGS"] = ["-mno-outline-atomics"]


def post_install(self):
    self.install_license("COPYING")
    # test programs (installed with tests enabled)
    # self.uninstall("usr/libexec/libunwind")


@subpackage("libunwind-nongnu-devel")
def _(self):
    return self.default_devel()
