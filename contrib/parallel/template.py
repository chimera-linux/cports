pkgname = "parallel"
pkgver = "20240422"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
]
depends = ["perl"]
pkgdesc = "Shell tool for executing jobs in parallel"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/parallel"
source = f"https://ftp.gnu.org/gnu/parallel/parallel-{pkgver}.tar.bz2"
sha256 = "783888203ede2b92ced31eb3e809ca3a9d89f4508fdcb11830bfb35754882467"
