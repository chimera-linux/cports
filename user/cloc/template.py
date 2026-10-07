pkgname = "cloc"
pkgver = "2.10"
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
sha256 = "a8fac35f4cf42728765580ba11afc2568ad205509a22204663f526169548436d"
