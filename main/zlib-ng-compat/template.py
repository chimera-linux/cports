pkgname = "zlib-ng-compat"
pkgver = "2.2.1"
# compat version
_cver = "1.3.1"
pkgrel = 2
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--shared",
    "--zlib-compat",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
# we need to explicitly provide higher ver or apk won't upgrade it,
# even with provider_priority set which is strange but it is how it is
provides = [
    f"so:libz.so.1={_cver}.99",
    f"zlib={_cver}-r99",
]
replaces = [f"zlib<{_cver}-r99"]
pkgdesc = "Implementation of zlib compression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ec6a76169d4214e2e8b737e0850ba4acb806c69eeace6240ed4481b9f5c57cdf"
tool_flags = {"CFLAGS": ["-fPIC"]}
compression = "deflate"
# sigh, carried over from zlib's old buildsystem
options = ["bootstrap", "linkundefver"]


@subpackage("zlib-ng-compat-devel-static")
def _static(self):
    self.provides = [f"zlib-devel-static={_cver}-r99"]
    self.replaces = [f"zlib-devel-static<{_cver}-r99"]

    return ["usr/lib/*.a"]


@subpackage("zlib-ng-compat-devel")
def _devel(self):
    self.provides = [f"zlib-devel={_cver}-r99"]
    self.replaces = [f"zlib-devel<{_cver}-r99"]

    return self.default_devel()


@subpackage("zlib-dbg")
def _dbg(self):
    self.subdesc = "transitional debug package"
    # prevent cbuild from thinking it's a depcycle
    self.depends = [f"virtual:zlib-ng-compat-dbg={self.full_pkgver}!base-files"]
    self.options = ["empty"]
    return []
