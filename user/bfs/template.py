pkgname = "bfs"
pkgver = "4.1"
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
sha256 = "7a2ccafc87803b6c42009019e0786cb1307f492c2d61d2fcb0be5dcfdd0049da"
hardening = ["cfi", "vis"]
