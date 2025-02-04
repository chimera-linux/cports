pkgname = "podman-tui"
pkgver = "1.3.0"
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
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/containers/podman-tui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a56d0f98e9537cefec1db2e685afc4f0453fcf0272a5f922f3ca04b3b2f9f59"
