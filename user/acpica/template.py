pkgname = "acpica"
pkgver = "20260408"
pkgrel = 0
build_style = "makefile"
# disable builtin flags that are supplied by cbuild (opt, fortify)
make_build_args = ["OPT_CFLAGS="]
make_use_env = True
hostmakedepends = ["bison", "flex"]
pkgdesc = "Intel ACPI Component Architecture utilities"
license = "GPL-2.0-only OR BSD-3-Clause OR Intel-ACPI"
url = "https://www.acpica.org"
source = f"https://github.com/acpica/acpica/releases/download/{pkgver}/acpica-unix-{pkgver}.tar.gz"
sha256 = "e66ceb26d6d514ce164fe22f5a4f7ca165cc38349d7a97f41a21f19b364647a2"
# no tests; no license file
options = ["!check", "!distlicense"]
