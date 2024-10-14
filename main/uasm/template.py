pkgname = "uasm"
pkgver = "2.57"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["-f", "Makefile-Linux-GCC-64.mak"]
make_use_env = True
pkgdesc = "MASM-compatible assembler"
maintainer = "psykose <alice@ayaya.dev>"
license = "CC-BY-SA-3.0 AND Watcom-1.0"
url = "https://www.terraspace.co.uk/uasm.html"
source = (
    f"https://github.com/Terraspace/UASM/archive/refs/tags/v{pkgver}r.tar.gz"
)
sha256 = "09fa69445f2af47551e82819d024e6b4b629fcfd47af4a22ccffbf37714230e5"
# silence
# broken with fortify somewhere, but doesn't matter much for a assembler..
tool_flags = {"CFLAGS": ["-w", "-U_FORTIFY_SOURCE"]}
hardening = ["!int"]
# no tests
options = ["!check"]


def install(self):
    self.install_bin("GccUnixR/uasm")
    self.install_license("License.txt")
