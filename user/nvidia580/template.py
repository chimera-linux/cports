pkgname = "nvidia580"
pkgver = "580.196.07"
pkgrel = 0
_basename = f"NVIDIA-Linux-{self.profile.arch}-{pkgver}"
archs = ["aarch64", "x86_64"]
hostmakedepends = ["patchelf"]
# we need all these things to satisfy the scanner
makedepends = [
    "dinit-chimera",
    "gcompat-libs",
    "libgcc-chimera",
    "libx11",
    "libxext",
]
depends = [
    "nvidia-modprobe",
    "nvidia-persistenced",
    "nvidia-settings",
    "nvidia-xconfig",
    self.with_pkgver("nvidia580-ckms"),
    self.with_pkgver("nvidia580-firmware"),
    self.with_pkgver("nvidia580-libs"),
]
provides = [self.with_pkgver("nvidia")]
pkgdesc = "NVIDIA Linux drivers - 580.x"
license = "custom:nvidia"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"!https://download.nvidia.com/XFree86/Linux-{self.profile.arch}/{pkgver}/{_basename}.run"
hardening = ["!pie"]

_nvcompat_so = "libnvcompat.so.0"

match self.profile.arch:
    case "aarch64":
        sha256 = (
            "5b7d2319a1e5228cb47a67e07733a5abfb614cd8d4350a750211022343d27eed"
        )
        _ldso = "ld-linux-aarch64.so.1"
    case "x86_64":
        sha256 = (
            "0aab0518db53cf73c412dc7f32bbc850ca95e839d8923d0de4bff42c1c9169ce"
        )
        _ldso = "ld-linux-x86-64.so.2"


def _sanitize_elf(self, path):
    self.log(f"sanitizing ELF file '{path}'...")
    self.do(
        "patchelf",
        # drop stuff that's a part of libc on musl
        "--remove-needed",
        _ldso,
        "--remove-needed",
        "libdl.so.2",
        "--remove-needed",
        "libm.so.6",
        "--remove-needed",
        "libpthread.so.0",
        "--remove-needed",
        "librt.so.1",
        # replace libc
        "--replace-needed",
        "libc.so.6",
        "libc.so",
        # add libnvcompat
        "--add-needed",
        _nvcompat_so,
        # remap symbols
        "--rename-dynamic-symbols",
        "libnvcompat.map",
        # target file
        path,
    )
    return path


def _install_lib(self, libn, subdir=None):
    if not (self.cwd / libn).exists():
        libn = f"{libn}.so.{pkgver}"
    # start by installing the file
    dest = "usr/lib"
    if subdir:
        dest = f"{dest}/{subdir}"
    self.install_file(libn, dest, mode=0o755)
    # unglibcify each file with standard rules
    cdest = _sanitize_elf(self, self.chroot_destdir / dest / libn)
    # check if we have a soname and if yes install all the links
    soname = self.do(
        "patchelf", "--print-soname", cdest, capture_output=True, check=False
    )
    if soname.returncode == 0 and len(soname.stdout.strip()) > 0:
        sostr = soname.stdout.strip().decode()
        if sostr != libn:
            self.log(f"creating SONAME symlink for '{cdest}' ({sostr})...")
            self.ln_s(libn, self.destdir / dest / sostr)
            self.log(f"creating raw .so link for '{cdest}'...")
            self.ln_s(
                sostr,
                self.destdir / dest / (sostr[0 : sostr.rfind(".so")] + ".so"),
            )


def _install_bin(self, binn):
    self.install_bin(binn)
    # optional manpage
    if (self.cwd / f"{binn}.1.gz").exists():
        self.do("gzip", "-d", f"{binn}.1.gz")
        self.install_man(f"{binn}.1")
    # sanitize and update interpreter
    bdest = _sanitize_elf(self, self.chroot_destdir / "usr/bin" / binn)
    self.do(
        "patchelf",
        "--set-interpreter",
        f"/lib/ld-musl-{self.profile.arch}.so.1",
        bdest,
    )


def extract(self):
    self.cp(self.sources_path / f"{_basename}.run", ".")
    self.do("sh", f"{_basename}.run", "--extract-only")
    self.rm(f"{_basename}.run")
    self.mv(f"{_basename}/*", ".", glob=True)
    self.cp(self.files_path / "libnvcompat.c", ".")
    self.cp(self.files_path / "libnvcompat.map", ".")


def build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(
        ["libnvcompat.c"],
        _nvcompat_so,
        ldflags=[
            "-nodefaultlibs",
            "-shared",
            f"-Wl,-soname,{_nvcompat_so}",
            "-Wl,--no-as-needed",
            "-l:libgcompat.so.0",
        ],
    )


def install(self):
    # compat library
    self.install_lib("libnvcompat.so.0")
    # firmware
    self.install_files("firmware", "usr/lib/firmware/nvidia", name=pkgver)
    # core libraries
    for nvlib in [
        "allocator",
        "api.so.1",
        "cfg",
        "eglcore",
        "encode",
        "fbc",
        "glcore",
        "glsi",
        "glvkspirv",
        "gpucomp",
        "ml",
        "ngx",
        "nvvm",
        "opencl",
        "opticalflow",
        "ptxjitcompiler",
        "rtcore",
        "tls",
    ]:
        _install_lib(self, f"libnvidia-{nvlib}")
    # glvnd libraries
    for gllib in ["EGL", "GLESv1_CM", "GLESv2", "GLX"]:
        _install_lib(self, f"lib{gllib}_nvidia")
    self.install_link("usr/lib/libGLX_indirect.so.0", "libGLX_nvidia.so.0")
    self.install_dir("usr/lib/gbm")
    self.install_link(
        "usr/lib/gbm/nvidia-drm_gbm.so", "../libnvidia-allocator.so.1"
    )
    # vdpau library
    _install_lib(self, "libvdpau_nvidia", "vdpau")
    # cuda libraries
    _install_lib(self, "libcuda")
    _install_lib(self, "libnvcuvid")
    # optix ray tracing engine
    _install_lib(self, "libnvoptix")
    self.install_file("nvoptix.bin", "usr/share/nvidia")
    # xorg driver
    _install_lib(self, "nvidia_drv.so", "xorg/modules/drivers")
    _install_lib(self, "libglxserver_nvidia", "nvidia/xorg")
    self.install_link(
        "usr/lib/nvidia/xorg/libglxserver_nvidia.so.1",
        f"libglxserver_nvidia.so.{pkgver}",
    )
    self.install_link(
        "usr/lib/nvidia/xorg/libglxserver_nvidia.so", "libglxserver_nvidia.so.1"
    )
    self.install_file(
        self.files_path / "nvidia-drm-outputclass.conf",
        "usr/share/X11/xorg.conf.d",
        name="10-nvidia-drm-outputclass.conf",
    )
    # tools
    _install_bin(self, "nvidia-cuda-mps-control")
    _install_bin(self, "nvidia-cuda-mps-server")
    _install_bin(self, "nvidia-debugdump")
    _install_bin(self, "nvidia-ngx-updater")
    _install_bin(self, "nvidia-powerd")
    _install_bin(self, "nvidia-smi")
    self.install_bin("nvidia-bug-report.sh", name="nvidia-bug-report")
    self.install_bin("systemd/nvidia-sleep.sh")
    self.install_bin(self.files_path / "prime-run")
    self.install_file(
        self.files_path / "nvidia-sleep.sh",
        "usr/lib/elogind/system-sleep",
        name="nvidia.sh",
        mode=0o755,
    )
    self.install_file("nvidia-dbus.conf", "usr/share/dbus-1/system.d")
    self.install_service(self.files_path / "nvidia-powerd")
    # vendor configs
    self.install_file("10_nvidia.json", "usr/share/glvnd/egl_vendor.d")
    self.install_file("nvidia_icd.json", "usr/share/vulkan/icd.d")
    self.install_file("nvidia_layers.json", "usr/share/vulkan/implicit_layer.d")
    self.install_file("nvidia.icd", "etc/OpenCL/vendors")
    # application profiles for nvidia-settings
    self.install_file(
        f"nvidia-application-profiles-{pkgver}-key-documentation",
        "usr/share/nvidia",
    )
    self.install_file(
        f"nvidia-application-profiles-{pkgver}-rc", "usr/share/nvidia"
    )
    # nouveau blocker
    self.install_file(
        self.files_path / "modprobe.conf",
        "usr/lib/modprobe.d",
        name="nvidia.conf",
    )
    # ngx
    if self.profile.arch == "x86_64":
        self.install_file("_nvngx.dll", "usr/lib/nvidia/wine", mode=0o755)
        self.install_file("nvngx.dll", "usr/lib/nvidia/wine", mode=0o755)
    # kernel source
    self.install_files("kernel", "usr/src", name=f"nvidia-{pkgver}")
    self.install_file(
        self.files_path / "ckms.ini",
        f"usr/src/nvidia-{pkgver}",
        template={"VERSION": pkgver},
    )
    # docs
    self.install_license("LICENSE")
    self.install_file("README.txt", f"usr/share/doc/{pkgname}")
    self.install_file("NVIDIA_Changelog", f"usr/share/doc/{pkgname}")


@subpackage("nvidia580-firmware")
def _(self):
    self.subdesc = "firwmare"
    self.provides = [self.with_pkgver("nvidia-firmware")]

    return ["usr/lib/firmware"]


@subpackage("nvidia580-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends += ["ckms", "gmake"]
    self.provides = [self.with_pkgver("nvidia-ckms")]

    return ["usr/lib/modprobe.d", "usr/src"]


@subpackage("nvidia580-opencl")
def _(self):
    self.subdesc = "OpenCL"
    self.depends += ["ocl-icd"]
    self.provides = [self.with_pkgver("nvidia-opencl")]
    self.options = ["etcfiles"]

    return ["etc/OpenCL", "usr/lib/libnvidia-opencl*"]


@subpackage("nvidia580-libs")
def _(self):
    self.subdesc = "common libraries"
    self.depends += [
        "libglvnd",
        "musl-nvidia",
        "nvidia-egl-gbm",
        "nvidia-egl-wayland",
    ]
    self.provides = [self.with_pkgver("nvidia-libs")]

    retv = [
        "usr/lib/*.so*",
        "usr/lib/gbm",
        "usr/lib/vdpau",
    ]
    if self.rparent.profile.arch == "x86_64":
        retv += ["usr/lib/nvidia/wine"]
    return retv
