pkgname = "libunwind-nongnu"
pkgver = "1.8.1"
pkgrel = 0
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
pkgdesc = "C library for unwind stacks"
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


def post_extract(self):
    # bsd patch doesn't support renames
    self.mv(
        "src/unwind/libunwind.pc.in",
        "src/unwind/libunwind-nongnu.pc.in",
    )


def post_install(self):
    self.install_license("COPYING")
    # test programs (installed with tests enabled)
    self.rm(self.destdir / "usr/libexec/libunwind", recursive=True, force=True)


@subpackage("libunwind-nongnu-devel")
def _devel(self):
    return self.default_devel()
