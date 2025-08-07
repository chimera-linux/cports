pkgname = "containers-common"
pkgver = "0.64.1"
pkgrel = 0
make_build_args = ["-C", "docs"]
make_install_args = [*make_build_args]
hostmakedepends = ["go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
license = "Apache-2.0"
url = "https://github.com/containers/common"
_base_url = url.removesuffix("/common")
_common_ver = pkgver
_storage_ver = "1.59.1"
_image_ver = "5.36.1"
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
    "414def665a172a4d79366dc594e5313d43d672ba19009aa2a3dd78272e277506",
    "2d4b0e5f66c83c776c6dab81fd52bee2aac72832ef3af4e6a1e081aaf1f87f30",
    "8ea547fe0f2dcfaa458f9e2d584eaacd504572bdb33ce0e98e70fffbc851c519",
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
