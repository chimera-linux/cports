pkgname = "zlib-ng-compat"
pkgver = "2.2.5"
# compat version
_cver = "1.3.1"
pkgrel = 0
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
provides = [f"so:libz.so.1={_cver}.99"]
renames = [f"zlib={_cver}-r99"]
pkgdesc = "Implementation of zlib compression library"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5b3b022489f3ced82384f06db1e13ba148cbce38c7941e424d6cb414416acd18"
tool_flags = {"CFLAGS": ["-fPIC"]}
compression = "deflate"
# sigh, carried over from zlib's old buildsystem
options = ["bootstrap", "linkundefver"]

if self.profile().cross:
    configure_env["CHOST"] = self.profile().triplet


@subpackage("zlib-ng-compat-devel")
def _(self):
    self.renames = [f"zlib-devel={_cver}-r99"]

    return self.default_devel()
