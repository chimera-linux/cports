pkgname = "podman-tui"
pkgver = "1.2.3"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "libbtrfs-devel",
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz>1.2.3-2.tar.gz"
sha256 = "d513362b270672c688407673326a8b9d850f4351e07cd3841ca321a84d9f5622"
