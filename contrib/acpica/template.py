pkgname = "acpica"
pkgver = "20230628"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_env = {"NOWERROR": "TRUE"}
make_use_env = True
hostmakedepends = [
    "bison",
    "flex",
    "gmake",
]
pkgdesc = "ACPICA utilities"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSD-3-Clause OR GPL-2.0-only OR Intel-ACPI"
url = "https://www.acpica.org"
source = f"https://downloadmirror.intel.com/783549/acpica-unix-{pkgver}.tar.gz"
sha256 = "86876a745e3d224dcfd222ed3de465b47559e85811df2db9820ef09a9dff5cce"
hardening = ["cfi", "vis"]
# no tests (there's a test suite in tests/, but no), no license file in src tree
options = ["!check", "!distlicense"]
