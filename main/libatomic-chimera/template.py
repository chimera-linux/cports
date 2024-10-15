pkgname = "libatomic-chimera"
pkgver = "0.90.0"
pkgrel = 1
build_style = "makefile"
pkgdesc = "ABI-compatible GNU libatomic alternative"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/chimera-linux/libatomic-chimera"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fccbd8c0ef7fd473275f835b3fca9275fb27a0c196cdcdff1f6d14ab12ed3a53"
options = ["bootstrap", "!lto"]

if self.profile().arch == "aarch64":
    # avoid emitting dependencies on builtins
    tool_flags = {"CFLAGS": ["-mno-outline-atomics"]}


@subpackage("libatomic-chimera-devel")
def _(self):
    return self.default_devel()
