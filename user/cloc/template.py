pkgname = "cloc"
pkgver = "2.04"
pkgrel = 0
build_style = "makefile"
make_dir = "Unix"
make_check_target = "test"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = [
    "perl-algorithm-diff",
    "perl-digest-md5",
    "perl-parallel-forkmanager",
    "perl-regexp-common",
]
checkdepends = [
    *depends,
    "git",
    "unzip",
]
pkgdesc = "Count lines of source code"
license = "GPL-2.0-or-later"
url = "https://github.com/AlDanial/cloc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3e6f25000d920fdee1a57575c185236286ab5e05fda7b6ab2e36c34f1bb6afbc"
