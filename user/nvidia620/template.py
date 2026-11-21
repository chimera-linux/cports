pkgname = "nvidia620"
pkgver = "620.70.06"
pkgrel = 0
_basename = f"NVIDIA-Linux-{self.profile.arch}-{pkgver}"
archs = ["aarch64", "x86_64"]
hostmakedepends = ["patchelf", "python"]
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
    self.with_pkgver("nvidia620-ckms"),
    self.with_pkgver("nvidia620-firmware"),
    self.with_pkgver("nvidia620-libs"),
]
provides = [self.with_pkgver("nvidia")]
pkgdesc = "NVIDIA Linux drivers - 620.x"
license = "custom:nvidia"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"!https://download.nvidia.com/XFree86/Linux-{self.profile.arch}/{pkgver}/{_basename}.run"
hardening = ["!pie"]

_nvcompat_so = "libnvcompat.so.0"

match self.profile.arch:
    case "aarch64":
        sha256 = (
            "3fa65a9271e0dde2a4e58c4965c38885a02a3a42accdcb26fc817410607f3e03"
        )
        _ldso = "ld-linux-aarch64.so.1"
    case "x86_64":
        sha256 = (
            "29118e3abd08c07559bcca3d9c76238d039490af0362a2e5bcfcbe7204afd4b1"
        )
        _ldso = "ld-linux-x86-64.so.2"


def _sanitize_elf(self, path):
    self.log(f"sanitizing ELF file '{path}'...")
    _sanargs = [
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
    ]
    if self.do("python", "check-mutex.py", path, check=False).returncode == 0:
        _sanargs += [
            # remap mutex symbols
            "--rename-dynamic-symbols",
            "libnvcompat.map",
        ]
    self.do("patchelf", *_sanargs, path)
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
    self.cp(self.files_path / "check-mutex.py", ".")


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
    # reverse dependency only on aarch64
    if self.profile.arch == "aarch64":
        _install_lib(self, "libnvidia-rmapi-tegra")
    # libnvidia-api.so.1 pulls in libstdc++ for operator new
    self.do(
        "patchelf",
        "--replace-needed",
        "libstdc++.so.6",
        "libc++abi.so.1",
        self.chroot_destdir / "usr/lib/libnvidia-api.so.1",
    )
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
    self.install_files("kernel-open", "usr/src", name=f"nvidia-{pkgver}")
    self.install_file(
        self.files_path / "ckms.ini",
        f"usr/src/nvidia-{pkgver}",
        template={"VERSION": pkgver},
    )
    # docs
    self.install_license("LICENSE")
    self.install_file("README.txt", f"usr/share/doc/{pkgname}")
    self.install_file("NVIDIA_Changelog", f"usr/share/doc/{pkgname}")


@subpackage("nvidia620-firmware")
def _(self):
    self.subdesc = "firwmare"
    self.provides = [self.with_pkgver("nvidia-firmware")]

    return ["usr/lib/firmware"]


@subpackage("nvidia620-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends += ["ckms", "gmake"]
    self.provides = [self.with_pkgver("nvidia-ckms")]

    return ["usr/lib/modprobe.d", "usr/src"]


@subpackage("nvidia620-opencl")
def _(self):
    self.subdesc = "OpenCL"
    self.depends += ["ocl-icd"]
    self.provides = [self.with_pkgver("nvidia-opencl")]
    self.options = ["etcfiles"]

    return ["etc/OpenCL", "usr/lib/libnvidia-opencl*"]


@subpackage("nvidia620-libs")
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
