pkgname = "bfs"
pkgver = "4.0.7"
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
sha256 = "37b11768b9b9bb50c7016d261317a4cd1ce047751681cfad528ccd700a65cd9e"
hardening = ["cfi", "vis"]
