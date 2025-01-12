pkgname = "tessen"
pkgver = "2.2.3"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = [
    "fuzzel",
    "libnotify",
    "pass-otp",
    "password-store",
    "wl-clipboard",
    "wtype",
]
pkgdesc = "Interactive menu to autotype and copy pass data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-2.0-only"
url = "https://sr.ht/~ayushnix/tessen"
source = f"https://git.sr.ht/~ayushnix/tessen/archive/v{pkgver}.tar.gz"
sha256 = "a672b564527f5b50fce65b9c3ba7616c326d5bd6d1a2479888fd437b37ecde1e"
# checks require shellcheck which isn't packaged (yet)
options = ["!check"]
