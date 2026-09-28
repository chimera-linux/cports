pkgname = "containers-common"
pkgver = "0.68.1"
pkgrel = 0
make_build_args = ["-C", "docs"]
make_install_args = [*make_build_args]
hostmakedepends = ["go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
license = "Apache-2.0"
url = "https://github.com/containers/container-libs"
_shortnames_ver = "2025.03.19"
source = [
    f"{url}/archive/refs/tags/common/v{pkgver}.tar.gz",
    f"{url.removesuffix('container-libs')}/shortnames/archive/refs/tags/v{_shortnames_ver}.tar.gz",
]
source_paths = [
    ".",
    "shortnames",
]
sha256 = [
    "6cfc76c4db34c30e560ab1bf5f297964fc755e8448a71f4b1ed8a68026431788",
    "1a2db4dca75b04d54623087972888459363392b9c4f64b6d0ac2f4b78cba3e45",
]
# no tests
options = ["etcfiles", "!check"]


def build(self):
    self.do("make", wrksrc="common/docs")
    self.do("make", wrksrc="storage/docs")
    self.do("make", "docs", wrksrc="image")


def install(self):
    self.install_dir("etc/containers/certs.d")
    self.install_dir("etc/containers/oci/hooks.d")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    with self.pushd("common"):
        self.install_file("pkg/config/containers.conf", "etc/containers")
        self.install_file("pkg/config/containers.conf", "usr/share/containers")
        self.install_file("pkg/seccomp/seccomp.json", "etc/containers")
        self.install_file("pkg/seccomp/seccomp.json", "usr/share/containers")
        self.do(
            "make",
            "install",
            "PREFIX=/usr",
            f"DESTDIR={self.chroot_destdir}",
            wrksrc="docs",
        )

    with self.pushd("storage"):
        self.install_file("storage.conf", "etc/containers")
        self.install_file("storage.conf", "usr/share/containers")
        self.do(
            "make", "install", f"DESTDIR={self.chroot_destdir}", wrksrc="docs"
        )

    with self.pushd("image"):
        self.install_file("registries.conf", "etc/containers")
        self.do("make", "install", f"DESTDIR={self.chroot_destdir}")

    with self.pushd("shortnames"):
        self.install_file(
            "shortnames.conf",
            "etc/containers/registries.conf.d",
            name="00-shortnames.conf",
        )
