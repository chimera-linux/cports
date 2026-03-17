pkgname = "atop"
pkgver = "2.12.1"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "SBINPATH=/usr/bin",
]
make_install_target = "genericinstall"
make_install_args = make_build_args
makedepends = [
    "clang",
    "glib-devel",
    "gmake",
    "linux-headers",
    "ncurses-devel",
    "pkgconf",
    "zlib-ng-compat-devel",
]
pkgdesc = "ASCII full-screen performance monitor"
license = "GPL-2.0-only"
url = "https://github.com/Atoptool/atop"
source = f"https://github.com/Atoptool/atop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0f49f3aa5e3449f8c1cf10ac08036e2b67887640fe7980b8bc6ca9fd84d46fdf"
# Dies with 0x0c on startup. Later investigation is needed.
hardening = ["!int"]
# `atop` does not implement `make check` or similar
options = ["!check"]
