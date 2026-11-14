pkgname = "cloc"
pkgver = "2.12"
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
sha256 = "e49b2ccad4c9c80e0c3f2a5c662c4097c73faf9867607a892f8e4c6dd1c7d861"
