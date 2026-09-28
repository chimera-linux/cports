pkgname = "bfs"
pkgver = "4.1.4"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--enable-release",
    "--with-libacl",
    "--with-libcap",
    "--with-liburing",
    "--with-oniguruma",
]
# the integration-tests fail to run with cbuild
make_check_target = "unit-tests"
hostmakedepends = ["pkgconf"]
makedepends = ["acl-devel", "libcap-devel", "liburing-devel", "oniguruma-devel"]
checkdepends = ["bash"]
pkgdesc = "Breadth-first version of the UNIX find command"
license = "0BSD"
url = "https://github.com/tavianator/bfs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0cac6849efb8a9447268fb273de3fab38f8460adb26a1770934e3f325fab8f5d"
hardening = ["cfi", "vis"]
