pkgname = "cloc"
pkgver = "2.08"
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
sha256 = "8099b6275c124f662690f2db3581cd2ad4e9ad4e08332288719838ded00d1da5"
