pkgname = "containers-common"
pkgver = "0.62.2"
pkgrel = 0
make_build_args = ["-C", "docs"]
make_install_args = [*make_build_args]
hostmakedepends = ["go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
license = "Apache-2.0"
url = "https://github.com/containers/common"
_base_url = url.removesuffix("/common")
_common_ver = pkgver
_storage_ver = "1.57.2"
_image_ver = "5.34.2"
_shortnames_ver = "2025.03.19"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
source_paths = [
    "common",
    "storage",
    "image",
    "shortnames",
]
sha256 = [
    "9ac8c06ee79aacbf36a607c5224a851f570240c7d7b6097d53078d47e62558c1",
    "04bc2578c15638981626a617f833ec8fc2aa08737844a78f9c9a35fbd0112505",
    "14254d2216b47ff383649ba67d948aa3c8a4a4cc52d483f27c18a02d78f70219",
    "1a2db4dca75b04d54623087972888459363392b9c4f64b6d0ac2f4b78cba3e45",
]
# no tests
options = ["!check"]


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
