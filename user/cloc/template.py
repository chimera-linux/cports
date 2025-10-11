pkgname = "cloc"
pkgver = "2.06"
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
    "git",
    "unzip",
    *depends,
]
pkgdesc = "Count lines of source code"
license = "GPL-2.0-or-later"
url = "https://github.com/AlDanial/cloc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "10d78427fda66aaa10ec733adb03d910c49376fe9068aacebb17aa657a7a3a05"
