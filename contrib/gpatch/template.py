pkgname = "gpatch"
pkgver = "2.7.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-prefix=g"]
# test suite relies on BASH_LINENO
configure_env = {"CONFIG_SHELL": "/usr/bin/bash"}
hostmakedepends = ["automake", "bash"]
makedepends = ["attr-devel"]
pkgdesc = "GNU patch"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://savannah.gnu.org/projects/patch"
source = f"https://ftp.gnu.org/gnu/patch/patch-{pkgver}.tar.gz"
sha256 = "8cf86e00ad3aaa6d26aca30640e86b0e3e1f395ed99f189b06d4c9f74bc58a4e"
