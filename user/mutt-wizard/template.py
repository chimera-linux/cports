pkgname = "mutt-wizard"
pkgver = "3.3.1"
pkgrel = 0
build_style = "makefile"
depends = [
    "neomutt",
    "curl",
    "isync",
    "msmtp",
    "password-store",
    "ca-certificates",
    "gettext",
]
pkgdesc = "Automatically configure neomutt and isync"
license = "GPL-3.0-or-later"
url = "https://github.com/LukeSmithxyz/mutt-wizard"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4091fba053786d4143249e61dfddfd679c15f561ec34af17f130a3ca80c39b53"
