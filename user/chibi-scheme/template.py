pkgname = "chibi-scheme"
pkgver = "0.11"
pkgrel = 0
pkgdesc = "Minimal (R7RS) Scheme implementation for use as an extension language"

license = "BSD-3-Clause"
options = ["!distlicense"]
build_style = "makefile"
make_check_target = "test"
tool_flags = {"CFLAGS": ["-O0"]} # R7RS quotient fails otherwise
hostmakedepends = ["pkgconf"]

url = "https://github.com/ashinn/chibi-scheme"
source = f"{url}/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b4404d5304b51b243684702fa7b5f2d82f77cb7ef470bcfca1d94f8ed7660342"

hardening = ["!int"]# illegal instruction otherwise
