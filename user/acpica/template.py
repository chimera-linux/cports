pkgname = "acpica"
pkgver = "20260408"
pkgrel = 0
build_style = "makefile"
# OPT_CFLAGS= drops upstream's warnings (incl. -Werror and clang-unknown GCC
# flags), -O2 and -D_FORTIFY_SOURCE; cbuild provides all three itself
make_build_args = ["OPT_CFLAGS="]
make_use_env = True
hostmakedepends = ["bison", "flex"]
pkgdesc = "Intel ACPI Component Architecture utilities"
license = "GPL-2.0-only OR BSD-3-Clause OR Intel-ACPI"
url = "https://www.acpica.org"
source = f"https://github.com/acpica/acpica/releases/download/{pkgver}/acpica-unix-{pkgver}.tar.gz"
sha256 = "e66ceb26d6d514ce164fe22f5a4f7ca165cc38349d7a97f41a21f19b364647a2"
# !check: upstream has no "check" make target
# !distlicense: the unix release tarball ships no standalone license file
# (license text is embedded in the source headers)
options = ["!check", "!distlicense"]
