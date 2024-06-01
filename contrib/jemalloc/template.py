pkgname = "jemalloc"
pkgver = "5.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-lg-hugepage=21"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
pkgdesc = "General purpose allocator library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://jemalloc.net"
source = f"https://github.com/jemalloc/jemalloc/releases/download/{pkgver}/jemalloc-{pkgver}.tar.bz2"
sha256 = "2db82d1e7119df3e71b7640219b6dfe84789bc0537983c3b7ac4f7189aecfeaa"

match self.profile().arch:
    case "aarch64" | "ppc64" | "ppc64le":
        configure_args += ["--with-lg-page=16"]
    case _:
        configure_args += ["--with-lg-page=12"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("jemalloc-devel")
def _devel(self):
    return self.default_devel()
