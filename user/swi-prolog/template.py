pkgname = "swi-prolog"
pkgver = "11.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DSWIPL_PACKAGES_JAVA=OFF",
    "-DUSE_TCMALLOC=OFF",
]
# The epilog tab-follows-cd tests need the xpce event loop: after the
# shell reads a line, a 0.25 s one-shot timer runs ->check_foreground,
# which relabels the tab via ->activity_changed.  The data is fine (the
# terminal's working_directory correctly follows the shell via
# /proc/<pid>/cwd in the chroot), but the timer/redraw chain does not
# complete headlessly (SDL dummy driver), and even a manual
# ->check_foreground deadlocks there.  Only the GUI notification is
# affected; exclude rather than weaken the tests.
make_check_args = ["-E", "xpce:epilog_tabs"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "cairo-devel",
    "gmp-devel",
    "libarchive-devel",
    "libedit-devel",
    "libyaml-devel",
    "ncurses-devel",
    "openssl3-devel",
    "pango-devel",
    "pcre2-devel",
    "python-devel",
    "sdl3-devel",
    "sdl3_image-devel",
    "unixodbc-devel",
    "utf8proc-devel",
    "zlib-ng-compat-devel",
]
# XPCE tests measure Pango font metrics and segfault on a fontless chroot.
checkdepends = ["python", "fonts-dejavu"]
pkgdesc = "Versatile implementation of the Prolog programming language"
license = "BSD-2-Clause AND LGPL-3.0-or-later"
url = "https://www.swi-prolog.org"
source = f"{url}/download/stable/src/swipl-{pkgver}.tar.gz"
sha256 = "64b9e2b8a862ee56dd54cf6820775111afc87310511c8f03f6fd978614e37c33"
# LTO hides the marker strings CMake reads from CheckTypeSize objects.
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")
