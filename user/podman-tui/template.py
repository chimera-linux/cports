pkgname = "podman-tui"
pkgver = "1.9.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "btrfs-progs-devel",
    "linux-headers",
    "sqlite-devel",
]
checkdepends = [
    "gpgme-devel",
    "pkgconf",
]
go_build_tags = [
    "btrfs_noversion",
    "containers_image_openpgp",
    "exclude_graphdriver_btrfs",
    "exclude_graphdriver_devicemapper",
    "libsqlite3",
    "remote",
]
go_check_tags = [*go_build_tags]
pkgdesc = "Podman terminal UI"
license = "Apache-2.0"
url = "https://github.com/containers/podman-tui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7a0e89d71a18527f01be061c8d449823770cff768b6d716cef96b979f3672de7"


def post_extract(self):
    # fails on builder, works in ci
    self.rm("ui/dialogs/progress_test.go")
