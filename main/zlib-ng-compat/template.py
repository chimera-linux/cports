pkgname = "zlib-ng-compat"
pkgver = "2.2.3"
# compat version
_cver = "1.3.1"
pkgrel = 2
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--shared",
    "--zlib-compat",
]
configure_env = {}
hostmakedepends = ["pkgconf"]
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
sha256 = "f2fb245c35082fe9ea7a22b332730f63cf1d42f04d84fe48294207d033cba4dd"
tool_flags = {"CFLAGS": ["-fPIC"]}
compression = "deflate"
# sigh, carried over from zlib's old buildsystem
options = ["bootstrap", "linkundefver"]

if self.profile().cross:
    configure_env["CHOST"] = self.profile().triplet


@subpackage("zlib-ng-compat-devel-static")
def _(self):
    self.provides = [f"zlib-devel-static={_cver}-r99"]
    self.replaces = [f"zlib-devel-static<{_cver}-r99"]

    return ["usr/lib/*.a"]


@subpackage("zlib-ng-compat-devel")
def _(self):
    self.provides = [f"zlib-devel={_cver}-r99"]
    self.replaces = [f"zlib-devel<{_cver}-r99"]

    return self.default_devel()
