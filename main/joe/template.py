pkgname = "joe"
pkgver = "4.6"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = ["./autojoe"]
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Curses-based text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://joe-editor.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/joe-editor/JOE%20sources/joe-{pkgver}/joe-{pkgver}.tar.gz"
sha256 = "495a0a61f26404070fe8a719d80406dc7f337623788e445b92a9f6de512ab9de"
# FIXME
hardening = ["!int", "vis", "cfi"]
