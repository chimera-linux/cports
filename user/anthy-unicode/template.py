pkgname = "anthy-unicode"
pkgver = "1.0.0.20260213"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlisp_dir=/usr/share/emacs/site-lisp"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Japanese character set input library for Unicode"
license = "LGPL-2.1-or-later AND GPL-2.0-only"
url = "https://github.com/fujiwarat/anthy-unicode/wiki"
source = f"https://github.com/fujiwarat/anthy-unicode/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1d79da684ba4b8bee82e55987361cceb970678045a26ad0b5435de44510b3252"
hardening = ["!int"]
options = ["etcfiles", "!cross"]


@subpackage("anthy-unicode-libs")
def _(self):
    self.subdesc = "libraries"

    return ["usr/lib/*.so.*"]


@subpackage("anthy-unicode-devel-static")
def _(self):
    return self.default_static()


@subpackage("anthy-unicode-devel")
def _(self):
    return self.default_devel()


@subpackage("anthy-unicode-emacs")
def _(self):
    self.subdesc = "emacs support"
    self.depends = [self.parent]
    self.install_if = [self.parent, "emacs"]

    return ["usr/share/emacs/site-lisp/anthy-unicode/*.el"]
