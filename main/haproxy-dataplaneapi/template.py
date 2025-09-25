pkgname = "haproxy-dataplaneapi"
pkgver = "3.2.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X main.GitTag={pkgver}"
    + " -X main.GitCommit="
    + " -X main.GitDirty= ",
    "./cmd/dataplaneapi",
]
hostmakedepends = ["go"]
pkgdesc = "HAProxy Data Plane API"
license = "Apache-2.0"
url = "https://github.com/haproxytech/dataplaneapi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e649d7acccc57a0922837b52044849985d7d1e749286c4d76b43fa0173afd8e6"
