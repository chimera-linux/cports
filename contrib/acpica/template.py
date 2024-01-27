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
# the test script is fucking garbage; it assumes that everything is
# built and placed into some magic bin directory, WHICH IT ISN'T! don't
# even bother fixing this, if intel can't get their shit together then
# you don't need to either
options = ["!check", "!distlicense"]
