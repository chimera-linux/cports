pkgname = "joe"
pkgver = "4.8"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autojoe"]
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Curses-based text editor"
license = "GPL-2.0-or-later"
url = "https://joe-editor.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/joe-editor/JOE%20sources/joe-{pkgver}/joe-{pkgver}.tar.gz"
sha256 = "6995b28ee20dcdbbcb5a45a4c110642dc96d67748aea27450c74cdb4dd07cc20"
# FIXME
hardening = ["!int", "vis", "cfi"]
options = ["etcfiles"]
